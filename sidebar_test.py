import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import *


class PopupMenu(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle('Example popup menu')
        self.resize(300, 300)

        self.label = QLabel(self)
        self.label.setText("MENU")

        self.popup_menu = QLabel(self)
        self.popup_menu.resize(180, 100)
        self.popup_menu.setText("Hello PyQt5!")
        self.popup_menu.setStyleSheet("border: 2px solid grey; font: italic 75 16pt Verdana;\
        text-align: center; border-radius: 10px;\
        background-color: lightblue; width: 10px;")

        self.popup_menu.hide()

        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignCenter)
        hbox.addStretch(2)
        hbox.addWidget(self.label)
        hbox.addWidget(self.popup_menu)

        self.label.installEventFilter(self)

    def eventFilter(self, obj, event):

        # If the mouse is over the widget
        if event.type() == 10:
            self.popup_menu.show()

        # If the mouse has left the widget area
        elif event.type() == 11:
            pass
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PopupMenu()
    window.show()
    sys.exit(app.exec_())
