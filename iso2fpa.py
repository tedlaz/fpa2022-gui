import sys

from PySide6 import QtCore, QtGui, QtWidgets

import fpagui

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/icons/icons/iso2fpa.png'))
    window = fpagui.MainWindow()
    window.show()
    app.exec()
