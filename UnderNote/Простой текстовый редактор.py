import sys
from PyQt5.QtWidgets import QMainWindow, QFontDialog, QApplication
from PyQt5.QtWidgets import QFileDialog as QFD
from PyQt5.QtGui import QIcon
from redactor import Ui_MainWindow


class Note(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.wt = ' - PyQt5 блокнот'
        self.main()

    def main(self):
        self.exn = ';;'.join(['Text Files (*.txt)',
                              'All Files (*.*)',
                              'Python Files (*.py)',
                              'System files (*.ini)',
                              'Files without extensions (-*)'])
        self.setCentralWidget(self.NotePlace)
        self.fileOpen.triggered.connect(self.opens)
        self.fileSave.triggered.connect(self.saves)
        self.fileSaveAs.triggered.connect(self.savesAs)
        self.setFileFont.triggered.connect(self.setFont)
        self.NotePlace.textChanged.connect(self.textModif)
        self.fn = None

    def opens(self):
        fileName = QFD.getOpenFileName(self, "Открыть файл", "", self.exn)[0]
        if fileName:
            self.fn = fileName
            self.opd = open(fileName, 'r+')
            self.text = self.opd.read()
            self.NotePlace.setPlainText(self.text)
            self.fileSave.setEnabled(True)
            self.opd.close()
            self.setWindowTitle(self.fn.split('/')[-1] + self.wt)

    def saves(self):
        self.opd = open(self.fn, 'w+')
        self.text = self.NotePlace.toPlainText()
        self.opd.write(self.text)
        self.opd.close()
        self.setWindowTitle(self.fn.split('/')[-1])

    def savesAs(self):
        fileName = QFD.getSaveFileName(self, "Сохранить файл", "", self.exn)[0]
        if fileName:
            self.fn = fileName
            self.opd = open(fileName, 'w+')
            self.text = self.NotePlace.toPlainText()
            self.opd.write(self.text)
            self.opd.close()
            self.setWindowTitle(self.fn.split('/')[-1] + self.wt)

    def setFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.NotePlace.setFont(font)

    def textModif(self):
        if self.fn and self.text != self.NotePlace.toPlainText():
            self.setWindowTitle(self.fn.split('/')[-1] + '*' + self.wt)
        elif self.fn:
            self.setWindowTitle(self.fn.split('/')[-1] + self.wt)


app = QApplication(sys.argv)
ex = Note()
ex.show()
try:
    sys.exit(app.exec())
except SystemExit:
    pass
