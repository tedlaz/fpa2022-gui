# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fpagui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QToolBar,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 621)
        self.actionopenfpa = QAction(MainWindow)
        self.actionopenfpa.setObjectName(u"actionopenfpa")
        icon = QIcon()
        icon.addFile(u":/images/images/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionopenfpa.setIcon(icon)
        self.actionselectfont = QAction(MainWindow)
        self.actionselectfont.setObjectName(u"actionselectfont")
        icon1 = QIcon()
        icon1.addFile(u":/images/images/font.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionselectfont.setIcon(icon1)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.isozygio_tab = QWidget()
        self.isozygio_tab.setObjectName(u"isozygio_tab")
        self.verticalLayout_5 = QVBoxLayout(self.isozygio_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.isozygio = QPlainTextEdit(self.isozygio_tab)
        self.isozygio.setObjectName(u"isozygio")
        font = QFont()
        font.setFamilies([u"Fira Code Retina"])
        font.setPointSize(7)
        self.isozygio.setFont(font)
        self.isozygio.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.isozygio.setPlainText(u"")
        self.isozygio.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_5.addWidget(self.isozygio)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.isozygio_tab)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.le_eponymia = QLineEdit(self.isozygio_tab)
        self.le_eponymia.setObjectName(u"le_eponymia")
        self.le_eponymia.setFrame(False)
        self.le_eponymia.setReadOnly(True)

        self.horizontalLayout.addWidget(self.le_eponymia)

        self.label_2 = QLabel(self.isozygio_tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.le_apo = QLineEdit(self.isozygio_tab)
        self.le_apo.setObjectName(u"le_apo")
        self.le_apo.setFrame(False)
        self.le_apo.setReadOnly(True)

        self.horizontalLayout.addWidget(self.le_apo)

        self.label_3 = QLabel(self.isozygio_tab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.le_eos = QLineEdit(self.isozygio_tab)
        self.le_eos.setObjectName(u"le_eos")
        self.le_eos.setFrame(False)
        self.le_eos.setReadOnly(True)

        self.horizontalLayout.addWidget(self.le_eos)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.isozygio_tab)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.le_account = QLineEdit(self.isozygio_tab)
        self.le_account.setObjectName(u"le_account")
        self.le_account.setFrame(False)
        self.le_account.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.le_account)

        self.label_5 = QLabel(self.isozygio_tab)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.le_per = QLineEdit(self.isozygio_tab)
        self.le_per.setObjectName(u"le_per")
        self.le_per.setFrame(False)
        self.le_per.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.le_per)

        self.label_6 = QLabel(self.isozygio_tab)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.le_debit = QLineEdit(self.isozygio_tab)
        self.le_debit.setObjectName(u"le_debit")
        self.le_debit.setFrame(False)
        self.le_debit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.le_debit)

        self.label_7 = QLabel(self.isozygio_tab)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.le_credit = QLineEdit(self.isozygio_tab)
        self.le_credit.setObjectName(u"le_credit")
        self.le_credit.setFrame(False)
        self.le_credit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.le_credit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.btn_parse = QPushButton(self.isozygio_tab)
        self.btn_parse.setObjectName(u"btn_parse")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_parse.sizePolicy().hasHeightForWidth())
        self.btn_parse.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_parse.setFont(font1)
        self.btn_parse.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_parse.setStyleSheet(u"QPushButton{\n"
"  background: rgb(0, 170, 255);\n"
"  border: 2px solid rgb(0, 170, 200);\n"
"  padding: 10px;\n"
"  border-radius: 14px;\n"
"  color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(26, 221, 107);\n"
"	 border: 2px solid rgb(26, 150, 107);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.btn_parse)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.isozygio_tab, "")
        self.transformations_tab = QWidget()
        self.transformations_tab.setObjectName(u"transformations_tab")
        self.verticalLayout_4 = QVBoxLayout(self.transformations_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.accounts = QTableWidget(self.transformations_tab)
        self.accounts.setObjectName(u"accounts")

        self.verticalLayout_4.addWidget(self.accounts)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btnmatch = QPushButton(self.transformations_tab)
        self.btnmatch.setObjectName(u"btnmatch")

        self.horizontalLayout_4.addWidget(self.btnmatch)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.transformations_tab, "")
        self.fpa_tab = QWidget()
        self.fpa_tab.setObjectName(u"fpa_tab")
        self.verticalLayout_3 = QVBoxLayout(self.fpa_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.fpa = QTextEdit(self.fpa_tab)
        self.fpa.setObjectName(u"fpa")
        self.fpa.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.fpa)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.btnprint = QPushButton(self.fpa_tab)
        self.btnprint.setObjectName(u"btnprint")

        self.horizontalLayout_5.addWidget(self.btnprint)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.fpa_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionopenfpa)
        self.toolBar.addAction(self.actionselectfont)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0399\u03c3\u03bf\u03b6\u03cd\u03b3\u03b9\u03bf \u03c3\u03b5 \u03a6\u03a0\u0391", None))
        self.actionopenfpa.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.actionselectfont.setText(QCoreApplication.translate("MainWindow", u"selectfont", None))
#if QT_CONFIG(tooltip)
        self.actionselectfont.setToolTip(QCoreApplication.translate("MainWindow", u"\u0395\u03c0\u03b9\u03bb\u03bf\u03b3\u03ae \u03b3\u03c1\u03b1\u03bc\u03bc\u03b1\u03c4\u03bf\u03c3\u03b5\u03b9\u03c1\u03ac\u03c2", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0395\u03c0\u03c9\u03bd\u03c5\u03bc\u03af\u03b1:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0391\u03c0\u03cc:", None))
        self.le_apo.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0388\u03c9\u03c2", None))
        self.le_eos.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u039b\u03bf\u03b3\u03b1\u03c1\u03b9\u03b1\u03c3\u03bc\u03cc\u03c2:", None))
        self.le_account.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03b5\u03c1\u03b9\u03b3\u03c1\u03b1\u03c6\u03ae:", None))
        self.le_per.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u03a7\u03c1\u03ad\u03c9\u03c3\u03b7:", None))
        self.le_debit.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u03a0\u03af\u03c3\u03c4\u03c9\u03c3\u03b7:", None))
        self.le_credit.setText("")
        self.btn_parse.setText(QCoreApplication.translate("MainWindow", u"\u03a5\u03c0\u03bf\u03bb\u03bf\u03b3\u03b9\u03c3\u03bc\u03cc\u03c2 \u03a6\u03a0\u0391", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.isozygio_tab), QCoreApplication.translate("MainWindow", u"\u0399\u03c3\u03bf\u03b6\u03cd\u03b3\u03b9\u03bf", None))
        self.btnmatch.setText(QCoreApplication.translate("MainWindow", u"\u03ad\u03bb\u03b5\u03b3\u03c7\u03bf\u03c2 \u03ba\u03b1\u03b9 \u03c5\u03c0\u03bf\u03bb\u03bf\u03b3\u03b9\u03c3\u03bc\u03cc\u03c2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.transformations_tab), QCoreApplication.translate("MainWindow", u"\u039c\u03b5\u03c4\u03b1\u03c3\u03c7\u03b7\u03bc\u03b1\u03c4\u03b9\u03c3\u03bc\u03bf\u03af", None))
        self.btnprint.setText(QCoreApplication.translate("MainWindow", u"\u0395\u03ba\u03c4\u03cd\u03c0\u03c9\u03c3\u03b7", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fpa_tab), QCoreApplication.translate("MainWindow", u"\u03a6\u03a0\u0391", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

