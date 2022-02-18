import f2parameters as f2p


def dec2str(val):
    """
    Returns string with Greek Formatted decimal (12345.67 becomes 12.345,67)
    """
    if val == 0:
        return ""
    return f"{val:,.2f}".replace(".", "|").replace(",", ".").replace("|", ",")


def dict2gr(adic: dict) -> dict:
    """
    Μετατρέπει τις τιμές του adic που το κλειδί τους ξεκινά απο D σε Ελληνικό
    φορμάτ. Η παραδοχή είναι ότι όλες αυτές οι τιμές είναι Δεκαδικές.
    """
    final = {}
    for key, val in adic.items():
        if key.startswith('D'):
            final[key] = dec2str(val)
            continue
        final[key] = val
    return final


def parse(text, dname):
    """
    Παρσάρουμε τις τιμές κειμένου
    το "D123 * D345 + 3" γίνεται "dname['D123'] * dname['D345'] + 3"
    """
    tokens = text.split()
    expr = []
    for token in tokens:
        if token.startswith('D'):
            expr.append(f"{dname}['{token}']")
            continue
        expr.append(token)
    return ' '.join(expr)


def calculate(values: dict) -> dict:
    res = {}
    for key, val in f2p.PARAMS.items():

        if val == 's':  # Είναι τιμές κειμένου οπότε δεν κάνει τίποτα
            res[key] = values.get(key, '')
            continue

        if val == '':  # Αν η τιμή είναι '' θεωρούνται απλά αριθμοί
            res[key] = values.get(key, 0)
            continue

        res[key] = round(eval(parse(val, 'res')), 2)

    return res


def html_final(vals: dict) -> str:
    results = calculate(vals)
    html = f2p.F2_HTML.format(**dict2gr(results))
    return html
