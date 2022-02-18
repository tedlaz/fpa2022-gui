import os

from ini_handle import APP_PATH


def parse2dict():
    file_name = os.path.join(APP_PATH, 'moving_codes_e2.txt')
    final = {}

    with open(file_name, encoding='utf8') as fil:

        for line in fil.readlines():

            if len(line) < 7:
                continue

            code, *per = line.split()
            final[' '.join(per)] = code

    return final


def create_python_file():
    fname = os.path.join(APP_PATH, 'moving_codes_e2.py')
    dic = parse2dict()
    if not dic:
        return
    with open(fname, 'w', encoding='utf8') as fil:
        fil.write('e2codes = {\n')
        fil.write(
            '\n'.join([f"    '{key}': '{val}'," for key, val in dic.items()]))
        fil.write('\n}')


if __name__ == '__main__':
    create_python_file()
