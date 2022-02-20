import sys

from PySide6 import QtWidgets

import fpagui

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = fpagui.MainWindow()
    window.show()
    app.exec()
