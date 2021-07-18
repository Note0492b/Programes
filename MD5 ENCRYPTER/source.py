from PyQt6.QtWidgets import QMessageBox
import hashlib

from PySide6 import QtWidgets

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 210)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 221, 191))
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 5px\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 150, 201, 31))
        font = QFont()
        font.setFamilies([u"Hack"])
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setStrikeOut(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(75, 75, 75);\n"
"border-radius: 5px;\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 10, 201, 131))
        font1 = QFont()
        font1.setFamilies([u"Hack"])
        font1.setBold(True)
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(75, 75, 75);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;")

        self.retranslateUi(Form)

        def encoding():
            Add = self.plainTextEdit.toPlainText()
            Text = hashlib.md5(Add.encode())
            self.plainTextEdit.setPlainText(Text.hexdigest())

        self.pushButton.clicked.connect(encoding)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"M^5", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Form", u"Hello", None))
    # retranslateUi





if __name__ == "__main__":
    import sys

    ui = Ui_Form()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
