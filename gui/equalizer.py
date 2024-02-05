# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Equalizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSlider
from gui.equalizer_ui import reset_sliders


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("QFrame {\n"
"background-color: #353535;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    background-color: #353535;\n"
"    padding: 5px;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    color: pink;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setWhatsThis("")
        self.frame_4.setStyleSheet("QSlider::groove:vertical {\n"
"    background-color:#6b47a5;\n"
"    width: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background-color:#6b47a5;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: pink;\n"
"    border: none;\n"
"    width: 30px;\n"
"    height: 30px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider {\n"
"    border-radius: 2px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalSlider_6 = QtWidgets.QSlider(self.frame_4)
        self.verticalSlider_6.setStyleSheet("")
        self.verticalSlider_6.setProperty("value", 50)
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.horizontalLayout_2.addWidget(self.verticalSlider_6)
        self.verticalSlider_9 = QtWidgets.QSlider(self.frame_4)
        self.verticalSlider_9.setProperty("value", 50)
        self.verticalSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.horizontalLayout_2.addWidget(self.verticalSlider_9)
        self.verticalSlider_8 = QtWidgets.QSlider(self.frame_4)
        self.verticalSlider_8.setProperty("value", 50)
        self.verticalSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_8.setObjectName("verticalSlider_8")
        self.horizontalLayout_2.addWidget(self.verticalSlider_8)
        self.verticalSlider_7 = QtWidgets.QSlider(self.frame_4)
        self.verticalSlider_7.setProperty("value", 50)
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.horizontalLayout_2.addWidget(self.verticalSlider_7)
        self.verticalSlider_5 = QtWidgets.QSlider(self.frame_4)
        self.verticalSlider_5.setProperty("value", 50)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.horizontalLayout_2.addWidget(self.verticalSlider_5)
        self.verticalSlider = QtWidgets.QSlider(self.frame_4)
        self.verticalSlider.setProperty("value", 50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_2.addWidget(self.verticalSlider)
        self.verticalSlider_2 = QtWidgets.QSlider(self.frame_4)
        self.verticalSlider_2.setProperty("value", 50)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalLayout_2.addWidget(self.verticalSlider_2)
        self.verticalSlider_3 = QtWidgets.QSlider(self.frame_4)
        self.verticalSlider_3.setProperty("value", 50)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.horizontalLayout_2.addWidget(self.verticalSlider_3)
        self.verticalSlider_4 = QtWidgets.QSlider(self.frame_4)
        self.verticalSlider_4.setProperty("value", 50)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.horizontalLayout_2.addWidget(self.verticalSlider_4)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QToolTip {\n"
"    padding: 3px; \n"
"     background-color: #353535;\n"
"    color: pink;\n"
"    font-weight:bold;\n"
"    border:1px solid #6b47a8;\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            background-color: #6b47a8;\n"
"            color: pink;\n"
"            border: none;\n"
"            padding: 4px 8px;\n"
"            border-radius: 12px;  /* Добавляем скругленные углы */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5d3990;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4e3278;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignBottom)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QToolTip {\n"
"    padding: 3px; \n"
"     background-color: #353535;\n"
"    color: pink;\n"
"    font-weight:bold;\n"
"    border:1px solid #6b47a8;\n"
"    border-radius: 3px;\n"
"}\n"
"QPushButton {\n"
"            background-color: #6b47a8;\n"
"            color: pink;\n"
"            border: none;\n"
"            padding: 4px 8px;\n"
"            border-radius: 12px;  /* Добавляем скругленные углы */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #5d3990;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4e3278;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.frame)

        self.equalizer_sliders = [
            self.verticalSlider_6,
            self.verticalSlider_9,
            self.verticalSlider_8,
            self.verticalSlider_7,
            self.verticalSlider_5,
            self.verticalSlider,
            self.verticalSlider_2,
            self.verticalSlider_3,
            self.verticalSlider_4
        ]

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Equalizer settings"))
        self.pushButton.setText(_translate("Dialog", "Continue"))
        self.pushButton_2.setText(_translate("Dialog", "Default"))


    def reset_sliders(self):
        reset_sliders(self)