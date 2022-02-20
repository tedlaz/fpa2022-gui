import os
import re
from collections import namedtuple

from ini_handle import APP_PATH
from utils import grglish_small_nosp

GREEK_NUMBER_RE = r"[\d\.]+,\d{2}"  # r'[0-9]+(\.[0-9]+)?(\,[0-9]+)?')"
GREEK_ACCOUNT_RE = r"[0-9\.]+"


ILine = namedtuple('ILine', 'acc per xre pis ypo normal_ypo')


def is_greek_number(txtval: str) -> bool:
    res = re.fullmatch(GREEK_NUMBER_RE, txtval)
    if res:
        return True
    return False


def is_greek_account(txtval: str) -> bool:
    res = re.fullmatch(GREEK_ACCOUNT_RE, txtval)
    if res:
        return True
    return False


def gr2f(txtNumber: str) -> float:
    """
    Convert Greek formatted number to float
    """
    return float(txtNumber.replace('.', '').replace(',', '.'))


def parse_header(line: str, slic: slice) -> str:
    return line[slic].strip()


def parse_line(line: str, pars) -> ILine:
    acc = line[pars['acc']].strip()
    per = line[pars['per']].strip()
    xre = line[pars['debit']].strip()
    pis = line[pars['credit']].strip()
    if all([is_greek_account(acc), is_greek_number(xre), is_greek_number(pis)]):
        dxre = gr2f(xre)
        dpis = gr2f(pis)
        ypo = round(dxre - dpis, 2)
        omada = acc[0]
        normal_ypo = ypo

        if omada in pars['omades_negative']:
            normal_ypo = -ypo
        return ILine(acc, per, dxre, dpis, ypo, normal_ypo)
    return ILine('', '', 0, 0, 0, 0)


def parse(isozygio_lines: str, pars: dict) -> dict:
    name = ''
    apo = ''
    eos = ''
    lines = []

    for i, line in enumerate(isozygio_lines.split('\n')):

        if i == pars['name']['line_no']:
            name = parse_header(line, pars['name']['slice'])

        if i == pars['apo']['line_no']:
            apo = parse_header(line, pars['apo']['slice'])

        if i == pars['eos']['line_no']:
            eos = parse_header(line, pars['eos']['slice'])

        lin = parse_line(line, pars)

        if lin.acc != '':
            lines.append(lin)
    gname = grglish_small_nosp(name)
    gpath = os.path.join(APP_PATH, gname)

    return {'name': name, 'gname': gpath, 'apo': apo, 'eos': eos, 'lines': lines}


def filter_low_level(accounts: list, pars: dict) -> list:
    """
    Παίρνουμε μόνο τους κινούμενους λογαριασμούς και όχι ανωτεροβάθμιους
    """
    low_level = []
    for i, acc in enumerate(accounts):
        if i == 0:
            low_level.append(acc)
            continue
        if acc.startswith(low_level[-1]):
            low_level.pop()
            low_level.append(acc)
            continue
        else:
            low_level.append(acc)
    return low_level


def filter_fpa(accounts: list, pars: dict) -> list:
    """Μόνο οι λογαριασμοί που πιθανόν έχουν ΦΠΑ"""
    return [a for a in accounts if a[0] in pars['omades']]


def filter_lines(lines: list, filter_func, pars: dict) -> list:
    """Φιλτράρουμε εγγραφές με βάση το λογαριασμό και κάποια συνάρτηση φίλτρο"""
    accounts = [line.acc for line in lines]
    lines_dict = {l.acc: l for l in lines}
    filtered_accounts = filter_func(accounts, pars)
    filtered = [l for a, l in lines_dict.items() if a in filtered_accounts]
    return filtered


def calculate_fpa_from_isozygio(low_level: list, pars: dict) -> float:
    """
    Βρίσκουμε το υπόλοιπο ΦΠΑ περιόδου αφαιρόντας τους λογαριασμούς ΦΠΑ
    τακτοποίησης (συνήθως 54.00.9*)
    """
    total = 0

    for lin in low_level:

        if lin.acc.startswith(pars['fpa_acc_exception']):
            continue

        if lin.acc.startswith(pars['fpa_acc']):
            total += lin.ypo

    return round(-total, 2)


def parse_filtered(isozygio_text: str, pars, pistotiko: float = 0) -> dict:

    # name, apo, eos, lines = parse(isozygio_text, pars)
    parsed = parse(isozygio_text, pars)

    low_level = filter_lines(parsed['lines'], filter_low_level, pars)
    only_fpa = filter_lines(low_level, filter_fpa, pars)

    fpa = calculate_fpa_from_isozygio(low_level, pars)

    parsed['D5400'] = fpa
    parsed['lines'] = only_fpa
    return parsed