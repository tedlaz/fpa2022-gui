import os
import sys

from PySide6.QtCore import QSettings

INI_FILE_NAME = 'fpagui.ini'

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    APP_PATH = os.path.dirname(sys.executable)
    INI_PATH = os.path.join(APP_PATH, INI_FILE_NAME)
else:
    APP_PATH = os.path.dirname(__file__)
    INI_PATH = os.path.join(APP_PATH, INI_FILE_NAME)


ACCOUNT_MATCH = os.path.join(APP_PATH, 'acc_match.txt')

initial_ini = """[General]
encoding=WINDOWS-1253

[PARSE]
name=1 19 80
apo=4 79  105
eos=4 115 146
acc=1   25
per=27  51
xre=97  112
pis=113 128

[FPA]
fpa_acc=54.00
fpa_acc_exception=54.00.9
omades=1267
omades_negative=7

"""


if not os.path.isfile(INI_PATH):
    with open(INI_PATH, 'w', encoding='utf8') as fil:
        fil.write(initial_ini)


INI = QSettings(INI_PATH, QSettings.IniFormat)


def ini2dic_int_tuple(mainkey):
    """
    returns dictionary: {keyval1: [a1, a2, ...], keyval2: [b1, ..]}
    """
    fdict = {}
    INI.beginGroup(mainkey)
    for key in INI.allKeys():
        fdict[key] = tuple([int(i) for i in INI.value(key).split()])
    INI.endGroup()
    return fdict


def ini2dic(mainkey):
    """
    returns dictionary: {keyval1: [a1, a2, ...], keyval2: [b1, ..]}
    """
    fdict = {}
    INI.beginGroup(mainkey)
    for key in INI.allKeys():
        fdict[key] = INI.value(key).split()
    INI.endGroup()
    return fdict


PARSE_POSITIONS = ini2dic_int_tuple('parse')
