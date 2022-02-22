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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolBar, QVBoxLayout, QWidget)
import fpagui_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 650)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.actionopenfpa = QAction(MainWindow)
        self.actionopenfpa.setObjectName(u"actionopenfpa")
        icon = QIcon()
        icon.addFile(u":/icons/icons/folder-open-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionopenfpa.setIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.isozygio_tab = QWidget()
        self.isozygio_tab.setObjectName(u"isozygio_tab")
        self.verticalLayout_5 = QVBoxLayout(self.isozygio_tab)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.fr1_iso_head = QFrame(self.isozygio_tab)
        self.fr1_iso_head.setObjectName(u"fr1_iso_head")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr1_iso_head.sizePolicy().hasHeightForWidth())
        self.fr1_iso_head.setSizePolicy(sizePolicy)
        self.fr1_iso_head.setFrameShape(QFrame.NoFrame)
        self.fr1_iso_head.setFrameShadow(QFrame.Plain)
        self.fr1_iso_head.setLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.fr1_iso_head)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.isozygio = QPlainTextEdit(self.fr1_iso_head)
        self.isozygio.setObjectName(u"isozygio")
        font = QFont()
        font.setFamilies([u"Fira Code Retina"])
        font.setPointSize(7)
        self.isozygio.setFont(font)
        self.isozygio.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.isozygio.setPlainText(u"")
        self.isozygio.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_3.addWidget(self.isozygio)


        self.verticalLayout_5.addWidget(self.fr1_iso_head)

        self.fr2_iso_line = QFrame(self.isozygio_tab)
        self.fr2_iso_line.setObjectName(u"fr2_iso_line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fr2_iso_line.sizePolicy().hasHeightForWidth())
        self.fr2_iso_line.setSizePolicy(sizePolicy1)
        self.fr2_iso_line.setMaximumSize(QSize(16777, 25))
        self.fr2_iso_line.setStyleSheet(u"QFrame{\n"
"background-color:rgb(240, 240, 240);\n"
"}")
        self.fr2_iso_line.setFrameShape(QFrame.NoFrame)
        self.fr2_iso_line.setFrameShadow(QFrame.Plain)
        self.fr2_iso_line.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.fr2_iso_line)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_grammatoseira = QPushButton(self.fr2_iso_line)
        self.btn_grammatoseira.setObjectName(u"btn_grammatoseira")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/font-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_grammatoseira.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.btn_grammatoseira)

        self.lbl_template_name = QLabel(self.fr2_iso_line)
        self.lbl_template_name.setObjectName(u"lbl_template_name")
        self.lbl_template_name.setFrameShape(QFrame.WinPanel)
        self.lbl_template_name.setFrameShadow(QFrame.Sunken)
        self.lbl_template_name.setLineWidth(1)

        self.horizontalLayout_6.addWidget(self.lbl_template_name)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.btn_template_toggle = QPushButton(self.fr2_iso_line)
        self.btn_template_toggle.setObjectName(u"btn_template_toggle")
        self.btn_template_toggle.setMinimumSize(QSize(100, 0))
        self.btn_template_toggle.setBaseSize(QSize(50, 0))
        self.btn_template_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/angle-up-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_template_toggle.setIcon(icon2)
        self.btn_template_toggle.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_template_toggle)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.btn_parse = QPushButton(self.fr2_iso_line)
        self.btn_parse.setObjectName(u"btn_parse")
        self.btn_parse.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_parse.sizePolicy().hasHeightForWidth())
        self.btn_parse.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.btn_parse.setFont(font1)
        self.btn_parse.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_parse.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/gears-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_parse.setIcon(icon3)

        self.horizontalLayout_6.addWidget(self.btn_parse, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.fr2_iso_line)

        self.fr3_iso_footer = QFrame(self.isozygio_tab)
        self.fr3_iso_footer.setObjectName(u"fr3_iso_footer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fr3_iso_footer.sizePolicy().hasHeightForWidth())
        self.fr3_iso_footer.setSizePolicy(sizePolicy3)
        self.fr3_iso_footer.setMinimumSize(QSize(0, 0))
        self.fr3_iso_footer.setMaximumSize(QSize(16777214, 0))
        self.fr3_iso_footer.setBaseSize(QSize(0, 0))
        self.fr3_iso_footer.setFrameShape(QFrame.NoFrame)
        self.fr3_iso_footer.setFrameShadow(QFrame.Raised)
        self.fr3_iso_footer.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.fr3_iso_footer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_12 = QLabel(self.fr3_iso_footer)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)

        self.le_protypo_name = QLineEdit(self.fr3_iso_footer)
        self.le_protypo_name.setObjectName(u"le_protypo_name")
        self.le_protypo_name.setFrame(False)
        self.le_protypo_name.setReadOnly(True)

        self.gridLayout.addWidget(self.le_protypo_name, 0, 1, 1, 1)

        self.label_8 = QLabel(self.fr3_iso_footer)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.le_fpa = QLineEdit(self.fr3_iso_footer)
        self.le_fpa.setObjectName(u"le_fpa")
        self.le_fpa.setFrame(False)
        self.le_fpa.setReadOnly(True)

        self.gridLayout.addWidget(self.le_fpa, 1, 1, 1, 1)

        self.label_9 = QLabel(self.fr3_iso_footer)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)

        self.le_fpa_ektos = QLineEdit(self.fr3_iso_footer)
        self.le_fpa_ektos.setObjectName(u"le_fpa_ektos")
        self.le_fpa_ektos.setFrame(False)
        self.le_fpa_ektos.setReadOnly(True)

        self.gridLayout.addWidget(self.le_fpa_ektos, 1, 3, 1, 1)

        self.label_10 = QLabel(self.fr3_iso_footer)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.le_omades = QLineEdit(self.fr3_iso_footer)
        self.le_omades.setObjectName(u"le_omades")
        self.le_omades.setFrame(False)
        self.le_omades.setReadOnly(True)

        self.gridLayout.addWidget(self.le_omades, 2, 1, 1, 1)

        self.label_11 = QLabel(self.fr3_iso_footer)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)

        self.le_omades_negative = QLineEdit(self.fr3_iso_footer)
        self.le_omades_negative.setObjectName(u"le_omades_negative")
        self.le_omades_negative.setFrame(False)
        self.le_omades_negative.setReadOnly(True)

        self.gridLayout.addWidget(self.le_omades_negative, 2, 3, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_open_template = QPushButton(self.fr3_iso_footer)
        self.btn_open_template.setObjectName(u"btn_open_template")
        self.btn_open_template.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btn_open_template)

        self.btn_edit_template = QPushButton(self.fr3_iso_footer)
        self.btn_edit_template.setObjectName(u"btn_edit_template")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/pen-to-square-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_template.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.btn_edit_template)

        self.btn_new_template = QPushButton(self.fr3_iso_footer)
        self.btn_new_template.setObjectName(u"btn_new_template")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/folder-plus-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_template.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.btn_new_template)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.label_13 = QLabel(self.fr3_iso_footer)
        self.label_13.setObjectName(u"label_13")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_13.setFont(font2)

        self.verticalLayout_6.addWidget(self.label_13)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.fr3_iso_footer)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.le_eponymia = QLineEdit(self.fr3_iso_footer)
        self.le_eponymia.setObjectName(u"le_eponymia")
        self.le_eponymia.setFrame(False)
        self.le_eponymia.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_eponymia, 0, 1, 1, 1)

        self.label_2 = QLabel(self.fr3_iso_footer)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.le_apo = QLineEdit(self.fr3_iso_footer)
        self.le_apo.setObjectName(u"le_apo")
        self.le_apo.setFrame(False)
        self.le_apo.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_apo, 0, 3, 1, 1)

        self.label_3 = QLabel(self.fr3_iso_footer)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 4, 1, 1)

        self.le_eos = QLineEdit(self.fr3_iso_footer)
        self.le_eos.setObjectName(u"le_eos")
        self.le_eos.setFrame(False)
        self.le_eos.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_eos, 0, 5, 1, 1)

        self.label_4 = QLabel(self.fr3_iso_footer)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.le_account = QLineEdit(self.fr3_iso_footer)
        self.le_account.setObjectName(u"le_account")
        self.le_account.setFrame(False)
        self.le_account.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_account, 1, 1, 1, 1)

        self.label_5 = QLabel(self.fr3_iso_footer)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 2, 1, 1)

        self.le_per = QLineEdit(self.fr3_iso_footer)
        self.le_per.setObjectName(u"le_per")
        self.le_per.setFrame(False)
        self.le_per.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_per, 1, 3, 1, 1)

        self.label_6 = QLabel(self.fr3_iso_footer)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 4, 1, 1)

        self.le_debit = QLineEdit(self.fr3_iso_footer)
        self.le_debit.setObjectName(u"le_debit")
        self.le_debit.setFrame(False)
        self.le_debit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_debit, 1, 5, 1, 1)

        self.label_7 = QLabel(self.fr3_iso_footer)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 1, 6, 1, 1)

        self.le_credit = QLineEdit(self.fr3_iso_footer)
        self.le_credit.setObjectName(u"le_credit")
        self.le_credit.setFrame(False)
        self.le_credit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.le_credit, 1, 7, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.fr3_iso_footer)

        self.tabWidget.addTab(self.isozygio_tab, "")
        self.transformations_tab = QWidget()
        self.transformations_tab.setObjectName(u"transformations_tab")
        self.verticalLayout_4 = QVBoxLayout(self.transformations_tab)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.accounts = QTableWidget(self.transformations_tab)
        self.accounts.setObjectName(u"accounts")

        self.verticalLayout_4.addWidget(self.accounts)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btnmatch = QPushButton(self.transformations_tab)
        self.btnmatch.setObjectName(u"btnmatch")
        self.btnmatch.setEnabled(False)
        self.btnmatch.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.btnmatch)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.transformations_tab, "")
        self.fpa_tab = QWidget()
        self.fpa_tab.setObjectName(u"fpa_tab")
        self.verticalLayout_3 = QVBoxLayout(self.fpa_tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fpa = QTextEdit(self.fpa_tab)
        self.fpa.setObjectName(u"fpa")
        self.fpa.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.fpa)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.btn_recalculate = QPushButton(self.fpa_tab)
        self.btn_recalculate.setObjectName(u"btn_recalculate")
        self.btn_recalculate.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.btn_recalculate)

        self.horizontalSpacer_7 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.btnprint = QPushButton(self.fpa_tab)
        self.btnprint.setObjectName(u"btnprint")
        self.btnprint.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/file-pdf-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnprint.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.btnprint)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.fpa_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionopenfpa)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u03a0\u03b5\u03c1\u03b9\u03bf\u03b4\u03b9\u03ba\u03ae \u0394\u03ae\u03bb\u03c9\u03c3\u03b7 \u03a6\u03a0\u0391 \u03b1\u03c0\u03cc \u03b9\u03c3\u03bf\u03b6\u03cd\u03b3\u03b9\u03bf", None))
        self.actionopenfpa.setText(QCoreApplication.translate("MainWindow", u"open", None))
#if QT_CONFIG(tooltip)
        self.btn_grammatoseira.setToolTip(QCoreApplication.translate("MainWindow", u"\u0395\u03c0\u03b9\u03bb\u03bf\u03b3\u03ae \u03b3\u03c1\u03b1\u03bc\u03bc\u03b1\u03c4\u03bf\u03c3\u03b5\u03b9\u03c1\u03ac\u03c2 \u03b5\u03bc\u03c6\u03ac\u03bd\u03b9\u03c3\u03b7\u03c2 \u03b9\u03c3\u03bf\u03b6\u03c5\u03b3\u03af\u03bf\u03c5", None))
#endif // QT_CONFIG(tooltip)
        self.btn_grammatoseira.setText(QCoreApplication.translate("MainWindow", u"\u0393\u03c1\u03b1\u03bc\u03bc\u03b1\u03c4\u03bf\u03c3\u03b5\u03b9\u03c1\u03ac", None))
#if QT_CONFIG(tooltip)
        self.lbl_template_name.setToolTip(QCoreApplication.translate("MainWindow", u"\u03a0\u03c1\u03cc\u03c4\u03c5\u03c0\u03bf \u03c3\u03ac\u03c1\u03c9\u03c3\u03b7\u03c2", None))
#endif // QT_CONFIG(tooltip)
        self.lbl_template_name.setText(QCoreApplication.translate("MainWindow", u"default", None))
#if QT_CONFIG(tooltip)
        self.btn_template_toggle.setToolTip(QCoreApplication.translate("MainWindow", u"\u0386\u03bd\u03bf\u03b9\u03b3\u03bc\u03b1-\u03ba\u03bb\u03b5\u03af\u03c3\u03b9\u03bc\u03bf \u03c6\u03cc\u03c1\u03bc\u03b1\u03c2 \u03c0\u03c1\u03bf\u03c4\u03cd\u03c0\u03bf\u03c5 \u03c3\u03ac\u03c1\u03c9\u03c3\u03b7\u03c2", None))
#endif // QT_CONFIG(tooltip)
        self.btn_template_toggle.setText("")
#if QT_CONFIG(tooltip)
        self.btn_parse.setToolTip(QCoreApplication.translate("MainWindow", u"\u03a3\u03ac\u03c1\u03c9\u03c3\u03b7 \u03b1\u03c1\u03c7\u03b5\u03af\u03bf\u03c5 \u03ba\u03b5\u03b9\u03bc\u03ad\u03bd\u03bf\u03c5 \u0399\u03c3\u03bf\u03b6\u03c5\u03b3\u03af\u03bf\u03c5", None))
#endif // QT_CONFIG(tooltip)
        self.btn_parse.setText(QCoreApplication.translate("MainWindow", u"\u03a3\u03ac\u03c1\u03c9\u03c3\u03b7", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u038c\u03bd\u03bf\u03bc\u03b1 \u03c0\u03c1\u03bf\u03c4\u03cd\u03c0\u03bf\u03c5", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u039b\u03bf\u03b3\u03b1\u03c1\u03b9\u03b1\u03c3\u03bc\u03cc\u03c2 \u03a6\u03a0\u0391", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u039b/\u03bc\u03bf\u03c2 \u03a6\u03a0\u0391 \u03b5\u03be\u03b1\u03b9\u03c1\u03bf\u03cd\u03bc\u03b5\u03bd\u03bf\u03c2", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u039f\u03bc\u03ac\u03b4\u03b5\u03c2 \u039b\u03bf\u03b3\u03b1\u03c1\u03b9\u03b1\u03c3\u03bc\u03ce\u03bd", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0391\u03bd\u03c4\u03af\u03b8\u03b5\u03c4\u03b5\u03c2 \u039f\u03bc\u03ac\u03b4\u03b5\u03c2", None))
        self.btn_open_template.setText(QCoreApplication.translate("MainWindow", u"\u0395\u03c0\u03b9\u03bb\u03bf\u03b3\u03ae \u03c0\u03c1\u03bf\u03c4\u03cd\u03c0\u03bf\u03c5", None))
        self.btn_edit_template.setText(QCoreApplication.translate("MainWindow", u"\u0395\u03c0\u03b5\u03be\u03b5\u03c1\u03b3\u03b1\u03c3\u03af\u03b1", None))
        self.btn_new_template.setText(QCoreApplication.translate("MainWindow", u"\u039d\u03ad\u03bf", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0398\u03ad\u03c3\u03b5\u03b9\u03c2 \u03c0\u03b5\u03b4\u03af\u03c9\u03bd \u03c3\u03c4\u03bf \u03b1\u03c1\u03c7\u03b5\u03af\u03bf \u03b9\u03c3\u03bf\u03b6\u03c5\u03b3\u03af\u03bf\u03c5", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.isozygio_tab), QCoreApplication.translate("MainWindow", u"\u0399\u03c3\u03bf\u03b6\u03cd\u03b3\u03b9\u03bf", None))
        self.btnmatch.setText(QCoreApplication.translate("MainWindow", u"\u0388\u03bb\u03b5\u03b3\u03c7\u03bf\u03b9 \u03b1\u03bd\u03c4\u03b9\u03c3\u03c4\u03bf\u03af\u03c7\u03b9\u03c3\u03b7\u03c2 \u03ba\u03b1\u03b9 \u03c5\u03c0\u03bf\u03bb\u03bf\u03b3\u03b9\u03c3\u03bc\u03cc\u03c2 \u03a6\u03a0\u0391", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.transformations_tab), QCoreApplication.translate("MainWindow", u"\u039c\u03b5\u03c4\u03b1\u03c3\u03c7\u03b7\u03bc\u03b1\u03c4\u03b9\u03c3\u03bc\u03bf\u03af", None))
        self.btn_recalculate.setText(QCoreApplication.translate("MainWindow", u"\u0395\u03c0\u03b1\u03bd\u03c5\u03c0\u03bf\u03bb\u03bf\u03b3\u03b9\u03c3\u03bc\u03cc\u03c2 \u03bc\u03b5 \u03c0\u03b9\u03c3\u03c4\u03c9\u03c4\u03b9\u03ba\u03cc \u03c0\u03c1\u03bf\u03b7\u03b3.\u03c0\u03b5\u03c1\u03b9\u03cc\u03b4\u03bf\u03c5", None))
        self.btnprint.setText(QCoreApplication.translate("MainWindow", u"\u0395\u03be\u03b1\u03b3\u03c9\u03b3\u03ae \u03c3\u03b5 PDF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fpa_tab), QCoreApplication.translate("MainWindow", u"\u03a6\u03a0\u0391", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

