import sys
from PyQt5.QtPrintSupport import QPrintDialog, QPrintPreviewDialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.QtWidgets import QColorDialog as QCD
from PyQt5.QtWidgets import QFontDialog as QFtD
from PyQt5.QtWidgets import QMessageBox as QMB
from PyQt5.QtWidgets import QFileDialog as QFD
from PyQt5.QtGui import QIcon, QPixmap, QSyntaxHighlighter
from PyQt5.QtCore import QCoreApplication
from redactor import Ui_MainWindow as MainWind_1
from infoWind import Ui_MainWindow as MainWind_2
from win32n64r import crypt


windows = []


class UnderNote(QMainWindow, MainWind_1):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Различные переменные
        self.wt = ' - UnderNote'
        self.tch = False
        self.fn = None
        self.colours = {'color': '#000000',
                        'background': '#FFFFFF'}
        # Главный код
        self.main()

    def main(self):
        # Расширения открываемых файлов
        self.exn = ';;'.join(['UnderTest files (*.UT)',
                              'Text files (*.txt)',
                              'All files (*.*)',
                              'Files without extensions (-*)'])
        # Установление виджета текста как центрального
        self.setCentralWidget(self.NotePlace)
        # Функции меню "Файл"
        self.fileOpen.triggered.connect(self.opens)
        self.fileSave.triggered.connect(self.saves)
        self.fileSaveAs.triggered.connect(self.savesAs)
        self.newWindowAct.triggered.connect(self.newWindow)
        self.printAct.triggered.connect(self.prints)
        self.prevAct.triggered.connect(self.preview)
        self.exitact.triggered.connect(self.close)
        # Функции меню "Правка"
        self.setFileFont.triggered.connect(self.setFont)
        self.wrapp.triggered.connect(self.wrapMode)
        self.textColour.triggered.connect(lambda: self.colourChange('color'))
        self.backgroudColour.triggered.connect(lambda: self.colourChange('background'))
        # Функции меню "Справка"
        self.abouAct.triggered.connect(self.info)
        # Триггер на изменение текста
        self.NotePlace.textChanged.connect(self.textModif)
        self.hlt = Highlighter(self.NotePlace)

    def wrapMode(self):
        # Перенос строк
        if self.wrapp.isChecked():
            self.NotePlace.setLineWrapMode(1)
        else:
            self.NotePlace.setLineWrapMode(0)

    def closeEvent(self, event):
        # Переопрделение закрытия окна
        if self.tch:
            msg = "У вас есть несохранённые изменения.\nВыйти?"
            opts = QMB.Yes | QMB.No | QMB.Save
            reply = QMB.question(self, 'Message', msg, opts, QMB.No)
            if reply == QMB.Yes:
                event.accept()
            elif reply == QMB.Save:
                self.savesAs()
            else:
                event.ignore()
        else:
            event.accept()

    def newWindow(self):
        # Открытие нового окна
        global windows

        windows.append(UnderNote())
        windows[-1].show()

    def decode(self):
        s = self.text
        if s[-1] == '╫':
            s = s[:-1]
        self.text = s[::2] + s[1::2][::-1]

    def opens(self):
        # Открытие файла
        fileName = QFD.getOpenFileName(self, "Открыть файл", "", self.exn)[0]
        if fileName:
            self.fn = fileName
            if fileName.split('.')[-1] == 'UT':
                self.opd = open(fileName, 'r+', encoding = 'UTF-16')
                self.text = crypt(self.opd.read())
            else:
                self.opd = open(fileName, 'r+')
                self.text = self.opd.read()
            self.NotePlace.setPlainText(self.text)
            self.fileSave.setEnabled(True)
            self.opd.close()
            self.setWindowTitle(self.fn.split('/')[-1] + self.wt)
            self.tch = False

    def saves(self):
        # Сохранение файла
        self.opd = open(self.fn, 'w+', encoding = 'UTF-16')
        self.text = self.NotePlace.toPlainText()
        self.opd.write(self.text)
        self.opd.close()
        self.setWindowTitle(self.fn.split('/')[-1] + self.wt)
        self.tch = False

    def savesAs(self):
        # Сохранение файла с указанием названия
        fileName = QFD.getSaveFileName(self, "Сохранить файл", "", self.exn)[0]
        if fileName:
            if "." not in fileName:
                fileName += ".txt"
            self.fn = fileName
            self.fileSave.setEnabled(True)
            self.saves()

    def setFont(self):
        # Выбор шрифта
        font, ok = QFtD.getFont()
        if ok:
            self.NotePlace.setFont(font)

    def textModif(self):
        # Проверка на изменение текста
        self.tch = True
        if self.fn and self.text != self.NotePlace.toPlainText():
            self.setWindowTitle(self.fn.split('/')[-1] + '*' + self.wt)
        elif self.fn:
            self.setWindowTitle(self.fn.split('/')[-1] + self.wt)
            self.tch = False

    def prints(self):
        # Метод печати
        dialog = QPrintDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.NotePlace.document().print_(dialog.printer())

    def preview(self):
        # Превью печати
        dialog = QPrintPreviewDialog()
        self.NotePlace.setLineWrapMode(1)
        dialog.paintRequested.connect(self.NotePlace.print_)
        dialog.exec_()
        if not self.wrapp.isChecked():
            self.NotePlace.setLineWrapMode(0)

    def info(self):
        # О программе
        self.s = Info()
        self.s.show()

    def colourChange(self, typ):
        # Смена цвета
        self.colours[typ] = QCD.getColor().name()
        colSheet = ';'.join([i + ': ' + self.colours[i] for i in self.colours])
        self.NotePlace.setStyleSheet(colSheet)


class Info(QMainWindow, MainWind_2):
    # Окно с информацие о программе
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pixmap = QPixmap('UnderBottom.jpg')
        self.pixlab.setPixmap(pixmap)


class Highlighter(QSyntaxHighlighter):
    # Хайлатинг ваш ненужон
    def __init__(self, k):
        super().__init__(k)

    def highlightBlock(text):
        myClassFormat = QTextCharFormat()
        myClassFormat.setFontWeight(QFont.Weight.Bold.value())
        myClassFormat.setForeground(QBrush(QColor.darkMagenta))
        pattern = "\\bMy[A-Za-z]+\\b"

        expression = QRegExp(pattern)
        index = expression.indexIn(text)
        while index >= 0:
                length = expression.matchedLength()
                setFormat(index, length, myClassFormat)
                index = expression.indexIn(text, index + length)


app = QApplication(sys.argv)
ex = UnderNote()
ex.show()
try:
    sys.exit(app.exec())
except SystemExit:
    pass
