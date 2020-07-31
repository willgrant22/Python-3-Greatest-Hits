#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from PyQt5 import QtCore, QtGui, QtWidgets
import glob
import os 
import sys
class Ui_Form(object):
    x = glob.glob("*.db")
    
    print(x)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(453, 465)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(180, 130, 79, 23))
        self.comboBox.setObjectName("comboBox")
        self.x = glob.glob("*.db")
        self.comboBox.addItems(self.x)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

