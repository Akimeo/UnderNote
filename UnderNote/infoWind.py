# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoWind.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(440, 434)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.namel = QtWidgets.QLabel(self.centralwidget)
        self.namel.setGeometry(QtCore.QRect(160, 210, 121, 31))
        self.namel.setAlignment(QtCore.Qt.AlignCenter)
        self.namel.setObjectName("namel")
        self.pixlab = QtWidgets.QLabel(self.centralwidget)
        self.pixlab.setGeometry(QtCore.QRect(22, 10, 396, 200))
        self.pixlab.setObjectName("pixlab")
        self.copyrlab = QtWidgets.QLabel(self.centralwidget)
        self.copyrlab.setGeometry(QtCore.QRect(10, 350, 171, 41))
        self.copyrlab.setAlignment(QtCore.Qt.AlignCenter)
        self.copyrlab.setObjectName("copyrlab")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UnderNote - о программе"))
        self.namel.setText(_translate("MainWindow", "UnderNote v1.0.1"))
        self.pixlab.setText(_translate("MainWindow", "TextLabel"))
        self.copyrlab.setText(_translate("MainWindow", "© UnderBottom Games, 2018"))

