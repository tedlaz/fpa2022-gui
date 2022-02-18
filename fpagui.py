import sys
from collections import namedtuple

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt

from calculate2html import html_final
from fpagui_ui import Ui_MainWindow
from ini_handle import ACCOUNT_MATCH, INI, PARSE_POSITIONS
from isozygio_parse import parse, parse_filtered
from moving_codes_e2 import e2codes

IsoSelector = namedtuple('IsoSelector', 'row start end size')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.matched = {}
        self.create_connections()

        self.codata = PARSE_POSITIONS['name']
        self.le_eponymia.setText(f'{self.codata}')
        self.apo = PARSE_POSITIONS['apo']
        self.le_apo.setText(f'{self.apo}')
        self.eos = PARSE_POSITIONS['eos']
        self.le_eos.setText(f'{self.eos}')
        self.account = PARSE_POSITIONS['acc']
        self.le_account.setText(f'{self.account}')
        self.per = PARSE_POSITIONS['per']
        self.le_per.setText(f'{self.per}')
        self.debit = PARSE_POSITIONS['xre']
        self.le_debit.setText(f'{self.debit}')
        self.credit = PARSE_POSITIONS['pis']
        self.le_credit.setText(f'{self.credit}')

    def create_pars_parameters(self):
        pars = {}

        lin, start, end = self.codata
        pars['name'] = {'line_no': lin, 'slice': slice(start, end)}

        lin, start, end = self.apo
        pars['apo'] = {'line_no': lin, 'slice': slice(start, end)}

        lin, start, end = self.eos
        pars['eos'] = {'line_no': lin, 'slice': slice(start, end)}

        pars['acc'] = slice(self.account[0], self.account[1])
        pars['per'] = slice(self.per[0], self.per[1])
        pars['debit'] = slice(self.debit[0], self.debit[1])
        pars['credit'] = slice(self.credit[0], self.credit[1])
        pars['fpa_acc'] = INI.value('fpa/fpa_acc', defaultValue='54.00')
        pars['fpa_acc_exception'] = INI.value(
            'fpa/fpa_acc_exception', defaultValue='54.00.9')
        pars['omades'] = INI.value('fpa/omades', defaultValue='1267')
        pars['omades_negative'] = INI.value(
            'fpa/negative_omades', defaultValue='7')

        return pars

    def create_connections(self):
        self.actionOpen.triggered.connect(self.open)
        self.actionopenfpa.triggered.connect(self.open_fpa)
        self.isozygio.selectionChanged.connect(
            self.handleIsozygioSelectionChanged)
        self.isozygio.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.isozygio.customContextMenuRequested.connect(
            self.on_isozygio_context)
        self.btn_parse.clicked.connect(self.handle_parse)
        self.btnmatch.clicked.connect(self.handle_match)

    def handle_parse(self):
        if not self.isozygio.toPlainText():
            QtWidgets.QMessageBox.critical(
                self,
                "Error",
                "Please open isozygio ..."
            )
            return
        if not all([self.codata, self.apo, self.eos, self.account, self.per, self.debit, self.credit]):
            QtWidgets.QMessageBox.critical(
                self,
                "Error",
                "Please provide all positions in order to proceed"
            )
            return
        pars = self.create_pars_parameters()
        self.res = parse_filtered(self.isozygio.toPlainText(), pars)
        accounts = [f'{i.acc} - {i.per}' for i in self.res['lines']]
        self.trans.setPlainText(str(self.res))
        self.accounts.setColumnCount(2)
        self.accounts.setRowCount(len(accounts))
        self.accounts.setHorizontalHeaderLabels(['Λογαριασμός', 'Κωδικός'])
        self.matched = self.load_account_e2_matching()
        e2codes_reverse = {val: key for key, val in e2codes.items()}
        for i, acc in enumerate(accounts):
            self.accounts.setItem(i, 0, QtWidgets.QTableWidgetItem(acc))
            combo = QtWidgets.QComboBox()
            for item in e2codes.keys():
                combo.addItem(item)
            acclean, *_ = acc.split('-')
            dcode = self.matched.get(acclean.strip(), '-')
            combo.setCurrentText(e2codes_reverse[dcode])
            self.accounts.setCellWidget(i, 1, combo)
        self.tabWidget.setCurrentIndex(1)
        self.handle_match()

    def handle_match(self):
        row_number = self.accounts.rowCount()
        not_matched = []
        for i in range(row_number):
            account_with_perigrafi = self.accounts.item(i, 0).text()
            acc, *_ = account_with_perigrafi.split('-')
            e2code = e2codes[self.accounts.cellWidget(i, 1).currentText()]
            if e2code == '-':
                not_matched.append(account_with_perigrafi)
            else:
                self.matched[acc.strip()] = e2code
        if not_matched:
            not_matched_str = '\n'.join(not_matched)
            QtWidgets.QMessageBox.critical(
                self,
                "Error",
                ("Οι παρακάτω λογαριασμοί δεν έχουν αντιστοίχιση με κωδικούς ΦΠΑ\n"
                 f"{not_matched_str}"
                 )
            )
            return
        self.save_account_e2_matching()
        fpa_final = {
            'epon': self.res['name'],
            'apo': self.res['apo'],
            'eos': self.res['eos'],
            'D401': self.res['D401'],
            'D5400': self.res['D5400'],
        }
        for line in self.res['lines']:
            key = self.matched[line.acc]
            fpa_final[key] = round(fpa_final.get(key, 0) + line.normal_ypo, 2)
        self.fpa.setHtml(html_final(fpa_final))
        self.tabWidget.setCurrentIndex(2)

    def load_account_e2_matching(self):
        dict1 = {}
        try:
            with open(ACCOUNT_MATCH, encoding='utf8') as fil:
                for line in fil.readlines():
                    acc, e2code = line.split()
                    dict1[acc] = e2code
        except Exception:
            pass
        return dict1

    def save_account_e2_matching(self):
        sort_vals = [f"{k} {self.matched[k]}" for k in sorted(self.matched)]
        with open(ACCOUNT_MATCH, 'w', encoding='utf8') as fil:
            fil.write('\n'.join(sort_vals))

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
        INI.setValue('parse/name', f'{data.row} {data.start} {data.end}')
        self.le_eponymia.setText(f'{self.codata}')

    def set_apo(self):
        data = self.handleIsozygioSelectionChanged()
        self.apo = (data.row, data.start, data.end)
        INI.setValue('parse/apo', f'{data.row} {data.start} {data.end}')
        self.le_apo.setText(f'{self.apo}')

    def set_eos(self):
        data = self.handleIsozygioSelectionChanged()
        self.eos = (data.row, data.start, data.end)
        INI.setValue('parse/eos', f'{data.row} {data.start} {data.end}')
        self.le_eos.setText(f'{self.eos}')

    def set_account(self):
        data = self.handleIsozygioSelectionChanged()
        self.account = (data.start, data.end)
        INI.setValue('parse/acc', f'{data.start} {data.end}')
        self.le_account.setText(f'{self.account}')

    def set_per(self):
        data = self.handleIsozygioSelectionChanged()
        self.per = (data.start, data.end)
        INI.setValue('parse/per', f'{data.start} {data.end}')
        self.le_per.setText(f'{self.per}')

    def set_debit(self):
        data = self.handleIsozygioSelectionChanged()
        self.debit = (data.start, data.end)
        INI.setValue('parse/xre', f'{data.start} {data.end}')
        self.le_debit.setText(f'{self.debit}')

    def set_credit(self):
        data = self.handleIsozygioSelectionChanged()
        self.credit = (data.start, data.end)
        INI.setValue('parse/pis', f'{data.start} {data.end}')
        self.le_credit.setText(f'{self.credit}')

    def open(self):
        # fnam, _ = qw.QFileDialog.getOpenFileName(self, "Open", self.fnam, "")
        inif = INI.value('isozygio_file', defaultValue='')
        encoding_from_ini = INI.value('encoding', defaultValue='WINDOWS-1253')
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open', inif, "")
        if file_name:
            with open(file_name, encoding=encoding_from_ini) as fil:
                self.isozygio.setPlainText(fil.read())
            INI.setValue('isozygio_file', file_name)

    def open_fpa(self):
        fileName, filtr = QtWidgets.QFileDialog.getOpenFileName(self)
        if fileName:
            with open(fileName, encoding='utf8') as fil:
                self.fpa.setHtml(fil.read())

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


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
