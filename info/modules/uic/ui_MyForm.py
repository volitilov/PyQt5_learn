# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyForm(object):
    def setupUi(self, MyForm):
        MyForm.setObjectName("MyForm")
        MyForm.resize(300, 93)
        MyForm.setAutoFillBackground(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(MyForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(MyForm)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.button = QtWidgets.QPushButton(MyForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Изображения/ico/3xhumed-Cryonic-Folder-Folder-Blank-3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button.setIcon(icon)
        self.button.setAutoDefault(False)
        self.button.setDefault(False)
        self.button.setFlat(False)
        self.button.setObjectName("button")
        self.verticalLayout.addWidget(self.button)

        self.retranslateUi(MyForm)
        QtCore.QMetaObject.connectSlotsByName(MyForm)

    def retranslateUi(self, MyForm):
        _translate = QtCore.QCoreApplication.translate
        MyForm.setWindowTitle(_translate("MyForm", "My test form"))
        self.label.setText(_translate("MyForm", "<h3>Example text heare</h3>"))
        self.button.setText(_translate("MyForm", "&Закрыть."))

