# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui',
# licensing of 'ui2.ui' applies.
#
# Created: Fri Feb  4 17:25:59 2022
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 198))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.open = QtWidgets.QPushButton(Form)
        self.open.setMinimumSize(QtCore.QSize(0, 67))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(21)
        self.open.setFont(font)
        self.open.setObjectName("open")
        self.horizontalLayout.addWidget(self.open)
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setMinimumSize(QtCore.QSize(0, 67))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(21)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "警告", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>接下來將會用您的預設瀏覽器開啟所有的影片，</p><p>您確定要繼續嗎</p></body></html>", None, -1))
        self.open.setText(QtWidgets.QApplication.translate("Form", "確認", None, -1))
        self.cancel.setText(QtWidgets.QApplication.translate("Form", "取消", None, -1))

