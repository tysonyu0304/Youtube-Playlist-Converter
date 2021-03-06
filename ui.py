# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiicon.ui',
# licensing of 'uiicon.ui' applies.
#
# Created: Fri Feb  4 17:24:40 2022
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 640)
        Form.setMinimumSize(QtCore.QSize(480, 640))
        Form.setMaximumSize(QtCore.QSize(480, 640))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.input = QtWidgets.QPlainTextEdit(Form)
        self.input.setMaximumSize(QtCore.QSize(16777215, 59))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.input.setFont(font)
        self.input.setObjectName("input")
        self.verticalLayout.addWidget(self.input)
        self.convert = QtWidgets.QPushButton(Form)
        self.convert.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.convert.setFont(font)
        self.convert.setObjectName("convert")
        self.verticalLayout.addWidget(self.convert)
        self.output = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.output.setFont(font)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.verticalLayout.addWidget(self.clear)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.webopen = QtWidgets.QPushButton(Form)
        self.webopen.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.webopen.setFont(font)
        self.webopen.setObjectName("webopen")
        self.horizontalLayout.addWidget(self.webopen)
        self.copy = QtWidgets.QPushButton(Form)
        self.copy.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.copy.setFont(font)
        self.copy.setObjectName("copy")
        self.horizontalLayout.addWidget(self.copy)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QtWidgets.QApplication.translate("Form", "Youtube播放清單轉各影片網址轉換器", None, -1)
        )
        self.label.setText(
            QtWidgets.QApplication.translate("Form", "將Youtube播放清單網址或ID放到下面", None, -1)
        )
        self.convert.setText(QtWidgets.QApplication.translate("Form", "轉換", None, -1))
        self.clear.setText(QtWidgets.QApplication.translate("Form", "清空", None, -1))
        self.webopen.setText(
            QtWidgets.QApplication.translate("Form", "用瀏覽器開啟", None, -1)
        )
        self.copy.setText(
            QtWidgets.QApplication.translate("Form", "將網址複製到剪貼簿", None, -1)
        )
