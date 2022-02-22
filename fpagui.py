import os
import sys
from collections import namedtuple

from PySide6 import QtCore, QtGui, QtPrintSupport, QtWidgets
from PySide6.QtCore import Qt

import fpagui_rc
from calculate2html import html_final
from fpagui_ui import Ui_MainWindow
from ini_handle import APP_PATH, INI
from isozygio_parse import parse_filtered
from moving_codes_e2 import E2CODES
from parse_template import ParserTemplate

IsoSelector = namedtuple('IsoSelector', 'row start end size')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.isozygio.setFont(INI.value('isozygio_font'))

        self.parse_template = ParserTemplate()
        self.open_template_file(
            INI.value('parse_template_file', defaultValue=''))

        self.isozygio_file_name = ''
        self.matched = {}
        self.res = {}
        self.pistotiko = 0
        self.is_template_editing = False
        # self.load_parse_positions_from_ini()
        self.create_connections()

    def create_connections(self):
        self.actionopenfpa.triggered.connect(self.open)
        self.btn_grammatoseira.clicked.connect(self.select_font)
        self.isozygio.selectionChanged.connect(
            self.handleIsozygioSelectionChanged)
        self.isozygio.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.isozygio.customContextMenuRequested.connect(
            self.on_isozygio_context)
        self.btn_parse.clicked.connect(self.handle_parse)
        self.btnmatch.clicked.connect(self.handle_match)
        self.btnprint.clicked.connect(self.printpreviewDialog)
        self.btn_template_toggle.clicked.connect(self.template_toggle)
        self.btn_open_template.clicked.connect(self.select_template_file)
        self.btn_edit_template.clicked.connect(self.edit_template)
        self.btn_recalculate.clicked.connect(self.recalculate)

    def edit_template(self):
        if self.is_template_editing:
            self.fr3_iso_footer.setStyleSheet("")
            self.le_protypo_name.setReadOnly(True)
            self.le_fpa.setReadOnly(True)
            self.le_fpa_ektos.setReadOnly(True)
            self.le_omades.setReadOnly(True)
            self.le_omades_negative.setReadOnly(True)
            self.parse_template.set_name(self.le_protypo_name.text().strip())
            self.parse_template.set_fpa(self.le_fpa.text().strip())
            self.parse_template.set_fpa_exception(
                self.le_fpa_ektos.text().strip())
            self.parse_template.set_omades(self.le_omades.text().strip())
            self.parse_template.set_omades_negative(
                self.le_omades_negative.text().strip())
            if self.parse_template.is_saved2disk == False:
                spath = os.path.join(
                    APP_PATH, f'{self.parse_template.name}.tml')
                self.parse_template.save2file(spath)
                self.lbl_template_name.setText(self.parse_template.name)
                INI.setValue('parse_template_file', spath)
            self.btn_edit_template.setText('Επεξεργασία')
            self.is_template_editing = False
            return

        self.fr3_iso_footer.setStyleSheet(
            "QLineEdit{background-color: rgb(255, 222, 222);}")
        self.le_protypo_name.setReadOnly(False)
        self.le_fpa.setReadOnly(False)
        self.le_fpa_ektos.setReadOnly(False)
        self.le_omades.setReadOnly(False)
        self.le_omades_negative.setReadOnly(False)
        self.btn_edit_template.setText('Αποθήκευση')
        self.is_template_editing = True

    def template_toggle(self):
        if self.fr3_iso_footer.maximumHeight() == 0:
            self.fr3_iso_footer.setMaximumHeight(200)
            self.fr3_iso_footer.setMinimumHeight(200)
            self.btn_template_toggle.setIcon(QtGui.QIcon(
                ':/icons/icons/angle-down-solid.svg'))
        else:
            self.fr3_iso_footer.setMaximumHeight(0)
            self.fr3_iso_footer.setMinimumHeight(0)
            self.btn_template_toggle.setIcon(QtGui.QIcon(
                ':/icons/icons/angle-up-solid.svg'))

    def select_font(self):
        opval = QtWidgets.QFontDialog.MonospacedFonts
        options = QtWidgets.QFontDialog.FontDialogOptions(opval)
        ok, font = QtWidgets.QFontDialog.getFont(
            self.isozygio.font(), self, 'Επιλογή γρμματοσειράς', options)
        if ok:
            self.isozygio.setFont(font)
            INI.setValue('isozygio_font', font)

    def handle_parse(self):
        if not self.isozygio.toPlainText():
            QtWidgets.QMessageBox.critical(
                self,
                "Error",
                "Please open isozygio ..."
            )
            return
        if self.parse_template.is_saved2disk == False:
            QtWidgets.QMessageBox.critical(
                self,
                "Το πρότυπο σάρωσης έχει αλλάξει",
                "Αποθηκεύστε πρώτα τις αλλαγές που έγιναν στο πρότυπο."
            )
            return

        self.res = parse_filtered(
            self.isozygio.toPlainText(), self.parse_template)
        accounts = [f'{i.acc} - {i.per}' for i in self.res['lines']]
        self.accounts.setColumnCount(2)
        self.accounts.setRowCount(len(accounts))
        self.accounts.setHorizontalHeaderLabels(['Λογαριασμός', 'Κωδικός'])
        self.accounts.setColumnWidth(0, 400)

        self.accounts.horizontalHeader().setStretchLastSection(True)

        self.matched = self.load_account_e2_matching()

        e2codes_reverse = {val: key for key, val in E2CODES.items()}
        for i, acc in enumerate(accounts):
            item = QtWidgets.QTableWidgetItem(acc)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            self.accounts.setItem(i, 0, item)
            combo = QtWidgets.QComboBox()
            combo.wheelEvent = lambda event: None
            combo.addItems(E2CODES)
            acclean, *_ = acc.split('-')
            dcode = self.matched.get(acclean.strip(), '-')
            combo.setCurrentText(e2codes_reverse[dcode])
            self.accounts.setCellWidget(i, 1, combo)
        self.accounts.resizeRowsToContents()
        self.accounts.resizeColumnsToContents()
        self.tabWidget.setCurrentIndex(1)
        self.btnmatch.setEnabled(True)
        self.handle_match()

    def set_pistotiko(self):
        self.tabWidget.setCurrentIndex(2)
        # self.fpa.setHtml('')
        pistotiko, ok = QtWidgets.QInputDialog.getDouble(
            self,
            "Πιστωτικό Υπόλοιπο",
            "Ποσό:",
            self.pistotiko,
            0,
            10000000,
            2
        )
        if ok:
            self.pistotiko = pistotiko

    def recalculate(self):
        self.set_pistotiko()
        self.handle_match()

    def handle_match(self):
        row_number = self.accounts.rowCount()
        not_matched = []
        for i in range(row_number):
            account_with_perigrafi = self.accounts.item(i, 0).text()
            acc, *_ = account_with_perigrafi.split('-')
            e2code = E2CODES[self.accounts.cellWidget(i, 1).currentText()]
            if e2code == '-':
                not_matched.append(account_with_perigrafi)
            else:
                self.matched[acc.strip()] = e2code
        if not_matched:
            not_matched_str = '\n'.join(not_matched)
            QtWidgets.QMessageBox.critical(
                self,
                "Δεν έχει γίνει αντιστοίχιση κωδικών λογιστικής",
                ("Οι παρακάτω λογαριασμοί δεν έχουν αντιστοίχιση με κωδικούς ΦΠΑ\n"
                 f"{not_matched_str}"
                 )
            )
            return

        if not self.save_account_e2_matching():
            QtWidgets.QMessageBox.critical(
                self,
                "Λάθος",
                "Δεν έγινε αποθήκευση του αρχείου αντιστοίχισης"
            )
            return
        self.tabWidget.setCurrentIndex(2)
        fpa_final = {
            'epon': self.res['name'],
            'apo': self.res['apo'],
            'eos': self.res['eos'],
            'D401': self.pistotiko,
            'D5400': self.res['D5400'],
        }
        for line in self.res['lines']:
            key = self.matched[line.acc]
            fpa_final[key] = round(fpa_final.get(key, 0) + line.normal_ypo, 2)
        self.fpa.setHtml(html_final(fpa_final))
        self.btnprint.setEnabled(True)

    def load_account_e2_matching(self):
        dict1 = {}
        if os.path.exists(self.res['gname']):
            with open(self.res['gname'], encoding='utf8') as fil:
                for line in fil.readlines():
                    acc, e2code = line.split()
                    dict1[acc] = e2code
            return dict1
        QtWidgets.QMessageBox.critical(
            self, 'Προσοχή', f"Η εταιρεία {self.res['name']} δεν είναι παραμετροποιημένη")
        return dict1

    def save_account_e2_matching(self):
        sort_vals = [f"{k} {self.matched[k]}" for k in sorted(self.matched)]
        try:
            with open(self.res['gname'], 'w', encoding='utf8') as fil:
                fil.write('\n'.join(sort_vals))
            return True
        except Exception:
            return False

    def on_isozygio_context(self, point):
        setcompany = QtGui.QAction(
            'Επωνυμία',
            self,
            statusTip='Γραμμή και θέση επωνυμίας',
            triggered=self.set_company
        )
        setapo = QtGui.QAction(
            'Από',
            self,
            statusTip='Φραμμή και θέση περιόδου από',
            triggered=self.set_apo
        )
        seteos = QtGui.QAction(
            'Έως',
            self,
            statusTip='Γραμμή και θέση περιόδου έως',
            triggered=self.set_eos
        )
        setaccount = QtGui.QAction(
            'Λογαριασμός',
            self,
            statusTip='Θέση λογαριασμού',
            triggered=self.set_account
        )
        setper = QtGui.QAction(
            'Περιγραφή',
            self,
            statusTip='Θέση περιγραφής λογαριασμού',
            triggered=self.set_per
        )
        setdebit = QtGui.QAction(
            'Χρέωση',
            self,
            statusTip='Θέση χρέωσης',
            triggered=self.set_debit
        )
        setcredit = QtGui.QAction(
            'Πίστωση',
            self,
            statusTip='Θέση πίστωσης',
            triggered=self.set_credit
        )

        menu = QtWidgets.QMenu("Menu", self)
        menu.addAction(setcompany)
        menu.addAction(setapo)
        menu.addAction(seteos)
        menu.addAction(setaccount)
        menu.addAction(setper)
        menu.addAction(setdebit)
        menu.addAction(setcredit)
        menu.exec(self.isozygio.mapToGlobal(point))

    def set_company(self):
        data = self.handleIsozygioSelectionChanged()
        self.codata = (data.row, data.start, data.end)
        self.parse_template.set_pname(data.row, data.start, data.end)
        self.le_eponymia.setText(self.parse_template.pname_txt)

    def set_apo(self):
        data = self.handleIsozygioSelectionChanged()
        self.apo = (data.row, data.start, data.end)
        self.parse_template.set_papo(data.row, data.start, data.end)
        self.le_apo.setText(self.parse_template.papo_txt)

    def set_eos(self):
        data = self.handleIsozygioSelectionChanged()
        self.eos = (data.row, data.start, data.end)
        self.parse_template.set_peos(data.row, data.start, data.end)
        self.le_eos.setText(self.parse_template.peos_txt)

    def set_account(self):
        data = self.handleIsozygioSelectionChanged()
        self.account = (data.start, data.end)
        self.parse_template.set_pacc(data.start, data.end)
        self.le_account.setText(self.parse_template.pacc_txt)

    def set_per(self):
        data = self.handleIsozygioSelectionChanged()
        self.per = (data.start, data.end)
        self.parse_template.set_pper(data.start, data.end)
        self.le_per.setText(self.parse_template.pper_txt)

    def set_debit(self):
        data = self.handleIsozygioSelectionChanged()
        self.debit = (data.start, data.end)
        self.parse_template.set_pxre(data.start, data.end)
        self.le_debit.setText(self.parse_template.pxre_txt)

    def set_credit(self):
        data = self.handleIsozygioSelectionChanged()
        self.credit = (data.start, data.end)
        self.parse_template.set_ppis(data.start, data.end)
        self.le_credit.setText(self.parse_template.ppis_txt)

    def select_template_file(self):
        inif = INI.value('parse_template_file', defaultValue='')
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Επιλογή προτύπου', inif, "*.tml")
        if file_name:
            self.open_template_file(file_name)

    def open_template_file(self, file_name: str):
        self.parse_template = ParserTemplate().load_from_file(file_name)
        INI.setValue('parse_template_file', file_name)
        self.lbl_template_name.setText(self.parse_template.name)

        self.le_protypo_name.setText(self.parse_template.name)
        self.le_fpa.setText(self.parse_template.fpa)
        self.le_fpa_ektos.setText(self.parse_template.fpa_exception)
        self.le_omades.setText(self.parse_template.omades)
        self.le_omades_negative.setText(self.parse_template.omades_negative)
        self.le_eponymia.setText(self.parse_template.pname_txt)
        self.le_apo.setText(self.parse_template.papo_txt)
        self.le_eos.setText(self.parse_template.peos_txt)
        self.le_account.setText(self.parse_template.pacc_txt)
        self.le_per.setText(self.parse_template.pper_txt)
        self.le_debit.setText(self.parse_template.pxre_txt)
        self.le_credit.setText(self.parse_template.ppis_txt)

    def open(self):
        # fnam, _ = qw.QFileDialog.getOpenFileName(self, "Open", self.fnam, "")
        inif = INI.value('isozygio_file', defaultValue='')
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open', inif, "*.txt")
        if file_name:
            self.open_isozygio_file(file_name)
        self.handle_parse()

    def open_isozygio_file(self, file_name):
        encoding_from_ini = INI.value('encoding', defaultValue='WINDOWS-1253')
        with open(file_name, encoding=encoding_from_ini) as fil:
            self.isozygio.setPlainText(fil.read())
        INI.setValue('isozygio_file', file_name)
        self.fpa.setHtml('')
        self.accounts.setRowCount(0)
        self.accounts.setColumnCount(0)
        self.tabWidget.setCurrentIndex(0)
        self.isozygio_file_name = file_name
        self.btn_parse.setEnabled(True)
        self.btnprint.setEnabled(False)
        self.btnmatch.setEnabled(False)

    def handleIsozygioSelectionChanged(self) -> IsoSelector:
        cursor = self.isozygio.textCursor()
        row = cursor.blockNumber()
        size = cursor.selectionEnd() - cursor.selectionStart()
        if cursor.position() == cursor.selectionStart():
            start = cursor.columnNumber()
            end = start + size
            # print(row, start, end, size)
            return IsoSelector(row, start, end, size)
        start = cursor.columnNumber() - size
        end = cursor.columnNumber()
        # print(row, start, end, size)
        return IsoSelector(row, start, end, size)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        dropped_txt = event.mimeData().text().replace('file:///', '')
        if not dropped_txt.lower().endswith('.txt'):
            QtWidgets.QMessageBox.critical(
                self,
                "Λάθος",
                "Παρακαλώ δώστε τουλάχιστον ένα αρχείο κειμένου")
        if os.path.exists(dropped_txt):
            self.open_isozygio_file(dropped_txt)
        self.handle_parse()

    def printpreviewDialog(self):
        if self.isozygio_file_name == '':
            return
        fname = '.'.join(self.isozygio_file_name.split('.')[:-1])
        pdfname = f'{fname}.pdf'
        printer = QtPrintSupport.QPrinter(
            QtPrintSupport.QPrinter.HighResolution)
        printer.setPageSize(QtGui.QPageSize.A3)
        printer.setColorMode(QtPrintSupport.QPrinter.Color)
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        fileName, filtr = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                "Αποθήκευση",
                                                                pdfname,
                                                                "PDF Files (*.pdf)")
        if fileName:
            printer.setOutputFileName(fileName)
            self.fpa.print_(printer)
