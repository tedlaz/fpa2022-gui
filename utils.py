def remove_special_chars(txt: str) -> str:
    fin = txt
    for special in '.-_ !@#$%^&*()?,.?;':
        fin = fin.replace(special, '')
    return fin


def greeklish_small(txt: str) -> str:
    gr = 'αάβγδεέζηήθιίϊκλμνξοόπρστυύφχψω'
    en = 'aabgdeezhΗ8iiiklmnjooprstyyfxcv'
    fin = txt.lower()
    fin2 = [en[gr.index(i)] if i in gr else i for i in fin]
    return ''.join(fin2)


def grglish_small_nosp(txt):
    """
    Greekglish small with special chars removed
    """
    nospecials = remove_special_chars(txt)
    return greeklish_small(nospecials)


if __name__ == '__main__':
    print(grglish_small_nosp('Δ.ΧΑΡΑΜΙΔΟΠΟΥΛΟΣ-Σ.ΛΙΒΙΕΡΑΤΟΣ ΕΠΕ'))
