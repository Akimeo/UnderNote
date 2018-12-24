# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'redactor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 620)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("note.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(256, 128))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.NotePlace = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.NotePlace.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.NotePlace.setMinimumSize(QtCore.QSize(80, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.NotePlace.setFont(font)
        self.NotePlace.setAutoFillBackground(False)
        self.NotePlace.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.NotePlace.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.NotePlace.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.NotePlace.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.NotePlace.setPlainText("")
        self.NotePlace.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.NotePlace.setObjectName("NotePlace")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.fileOpen = QtWidgets.QAction(MainWindow)
        self.fileOpen.setObjectName("fileOpen")
        self.fileSave = QtWidgets.QAction(MainWindow)
        self.fileSave.setEnabled(False)
        self.fileSave.setObjectName("fileSave")
        self.fileSaveAs = QtWidgets.QAction(MainWindow)
        self.fileSaveAs.setObjectName("fileSaveAs")
        self.setFileFont = QtWidgets.QAction(MainWindow)
        self.setFileFont.setObjectName("setFileFont")
        self.menu.addAction(self.fileOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.fileSave)
        self.menu.addAction(self.fileSaveAs)
        self.menu_3.addAction(self.setFileFont)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt5 блокнот"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_3.setTitle(_translate("MainWindow", "Формат"))
        self.fileOpen.setText(_translate("MainWindow", "Открыть"))
        self.fileOpen.setStatusTip(_translate("MainWindow", "Открыть новый файл"))
        self.fileOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.fileSave.setText(_translate("MainWindow", "Сохранить"))
        self.fileSave.setStatusTip(_translate("MainWindow", "Сохранить открытый файл"))
        self.fileSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.fileSaveAs.setText(_translate("MainWindow", "Сохранить как"))
        self.fileSaveAs.setStatusTip(_translate("MainWindow", "Сохраить новый файл"))
        self.fileSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.setFileFont.setText(_translate("MainWindow", "Сменить шрифт"))
        self.setFileFont.setShortcut(_translate("MainWindow", "Ctrl+Shift+F"))
