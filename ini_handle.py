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


initial_ini = """[General]
encoding=WINDOWS-1253
isozygio_font=
parse_template_file=
"""


if not os.path.isfile(INI_PATH):
    with open(INI_PATH, 'w', encoding='utf8') as fil:
        fil.write(initial_ini)


INI = QSettings(INI_PATH, QSettings.IniFormat)
