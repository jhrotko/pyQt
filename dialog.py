# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\JoanaH\Documents\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QPushButton


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(463, 376)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.amountEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.amountEdit.setGeometry(QtCore.QRect(20, 50, 104, 41))
        self.amountEdit.setObjectName("amountEdit")
        self.Instruction = QtWidgets.QLabel(Dialog)
        self.Instruction.setGeometry(QtCore.QRect(20, 10, 241, 21))
        self.Instruction.setObjectName("Instruction")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(20, 110, 211, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.addMoeny = QPushButton(Dialog)
        self.addMoeny.setGeometry(QtCore.QRect(150, 50, 75, 23))
        self.addMoeny.setObjectName("addMoeny")
        self.addMoeny.clicked.connect(self.change_amount)

        self.totalAmount = QtWidgets.QTextEdit(Dialog)
        self.totalAmount.setGeometry(QtCore.QRect(300, 260, 151, 41))
        self.totalAmount.setObjectName("totalAmount")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 240, 141, 21))
        self.label.setObjectName("label")
        self.progressText = QtWidgets.QTextEdit(Dialog)
        self.progressText.setGeometry(QtCore.QRect(20, 140, 181, 91))
        self.progressText.setObjectName("progressText")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Instruction.setText(_translate("Dialog", "Choose amount of money to add to your account"))
        self.addMoeny.setText(_translate("Dialog", "Add Money"))
        self.label.setText(_translate("Dialog", "Amount in your account"))

    def change_amount(self, amount):
        print("shdkfj")
