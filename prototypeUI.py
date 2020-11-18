# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Prototype.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt

class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

    def keyPressEvent(self,event):
        print("key press event fired")

        if event.key() == 16777234:
            #its left arrow button
            print("left arrow pressed")
        elif event.key() == 16777235:
            #its up arrow button
            print("up arrow pressed")
        elif event.key() == 16777236:
            #its right arrow button
            print("right arrow pressed")
        elif event.key() == 16777237:
            #its down arrow button
            print("down arrow pressed")
        elif event.key() == 65:
            #its a button
            print("Button A was pressed")
        elif event.key() == 87:
            #its w button
            print("Button W was pressed")
        elif event.key() == 68:
            #its d button
            print("Button D was pressed")
        elif event.key() == 83:
            #its s button
            print("Button S was pressed")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1278, 875)
        Form.setAutoFillBackground(False)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setMidLineWidth(2)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 351, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(190, 80, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(180, 110, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 140, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 190, 61, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(92, 190, 141, 20))
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 190, 51, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(300, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(280, 90, 81, 16))
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setMidLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.frame_3)
        self.openGLWidget.setGeometry(QtCore.QRect(10, 10, 411, 491))
        self.openGLWidget.setObjectName("openGLWidget")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 520, 51, 26))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 520, 51, 26))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 520, 51, 26))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_9.setGeometry(QtCore.QRect(280, 520, 51, 26))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.frame_3, 0, 1, 2, 1)
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setMidLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(self.frame_5)
        self.openGLWidget_2.setGeometry(QtCore.QRect(9, 9, 401, 441))
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.label_65 = QtWidgets.QLabel(self.frame_5)
        self.label_65.setGeometry(QtCore.QRect(30, 470, 51, 16))
        self.label_65.setObjectName("label_65")
        self.label_66 = QtWidgets.QLabel(self.frame_5)
        self.label_66.setGeometry(QtCore.QRect(30, 500, 61, 16))
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.frame_5)
        self.label_67.setGeometry(QtCore.QRect(30, 530, 51, 16))
        self.label_67.setObjectName("label_67")
        self.label_68 = QtWidgets.QLabel(self.frame_5)
        self.label_68.setGeometry(QtCore.QRect(100, 500, 31, 16))
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.frame_5)
        self.label_69.setGeometry(QtCore.QRect(100, 470, 31, 16))
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.frame_5)
        self.label_70.setGeometry(QtCore.QRect(100, 530, 31, 16))
        self.label_70.setObjectName("label_70")
        self.label_71 = QtWidgets.QLabel(self.frame_5)
        self.label_71.setGeometry(QtCore.QRect(220, 470, 81, 16))
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.frame_5)
        self.label_72.setGeometry(QtCore.QRect(220, 500, 81, 16))
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.frame_5)
        self.label_73.setGeometry(QtCore.QRect(310, 470, 81, 16))
        self.label_73.setObjectName("label_73")
        self.label_74 = QtWidgets.QLabel(self.frame_5)
        self.label_74.setGeometry(QtCore.QRect(310, 500, 81, 16))
        self.label_74.setObjectName("label_74")
        self.gridLayout.addWidget(self.frame_5, 0, 2, 2, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setMidLineWidth(2)
        self.frame_2.setObjectName("frame_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(10, 6, 61, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(30, 40, 71, 16))
        self.label_10.setObjectName("label_10")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 40, 231, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(120, 80, 41, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 80, 51, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(240, 80, 47, 13))
        self.label_12.setObjectName("label_12")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 80, 61, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(30, 120, 71, 16))
        self.label_13.setObjectName("label_13")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setGeometry(QtCore.QRect(120, 120, 231, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(30, 160, 47, 13))
        self.label_14.setObjectName("label_14")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 160, 231, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(30, 200, 101, 16))
        self.label_15.setObjectName("label_15")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 200, 191, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setGeometry(QtCore.QRect(170, 230, 151, 17))
        self.checkBox.setObjectName("checkBox")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(10, 270, 47, 13))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(30, 300, 91, 16))
        self.label_17.setObjectName("label_17")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(140, 300, 211, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setGeometry(QtCore.QRect(30, 340, 71, 16))
        self.label_18.setObjectName("label_18")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_4.setGeometry(QtCore.QRect(140, 340, 211, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setGeometry(QtCore.QRect(30, 380, 161, 16))
        self.label_19.setObjectName("label_19")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(222, 380, 131, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 430, 180, 26))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 465, 180, 26))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 520, 180, 26))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.frame_2, 1, 0, 2, 1)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setMidLineWidth(2)
        self.frame_4.setObjectName("frame_4")
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setGeometry(QtCore.QRect(30, 40, 61, 16))
        self.label_21.setObjectName("label_21")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_5.setGeometry(QtCore.QRect(50, 60, 151, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setGeometry(QtCore.QRect(40, 100, 61, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_4)
        self.label_23.setGeometry(QtCore.QRect(170, 100, 51, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_4)
        self.label_24.setGeometry(QtCore.QRect(40, 130, 81, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_4)
        self.label_25.setGeometry(QtCore.QRect(170, 130, 51, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_4)
        self.label_26.setGeometry(QtCore.QRect(40, 160, 91, 16))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame_4)
        self.label_27.setGeometry(QtCore.QRect(170, 160, 47, 13))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_4)
        self.label_28.setGeometry(QtCore.QRect(40, 190, 91, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame_4)
        self.label_29.setGeometry(QtCore.QRect(170, 190, 47, 13))
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_4)
        self.label_30.setGeometry(QtCore.QRect(40, 220, 91, 16))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_4)
        self.label_31.setGeometry(QtCore.QRect(170, 220, 47, 13))
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.frame_4)
        self.label_32.setGeometry(QtCore.QRect(40, 250, 91, 16))
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame_4)
        self.label_33.setGeometry(QtCore.QRect(170, 250, 47, 13))
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_4)
        self.label_34.setGeometry(QtCore.QRect(40, 280, 91, 16))
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_4)
        self.label_35.setGeometry(QtCore.QRect(170, 280, 47, 13))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame_4)
        self.label_36.setGeometry(QtCore.QRect(260, 40, 61, 16))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame_4)
        self.label_37.setGeometry(QtCore.QRect(270, 70, 61, 16))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame_4)
        self.label_38.setGeometry(QtCore.QRect(270, 100, 71, 16))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.frame_4)
        self.label_39.setGeometry(QtCore.QRect(270, 130, 91, 16))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame_4)
        self.label_40.setGeometry(QtCore.QRect(270, 160, 71, 16))
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.frame_4)
        self.label_41.setGeometry(QtCore.QRect(270, 200, 71, 16))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.frame_4)
        self.label_42.setGeometry(QtCore.QRect(270, 230, 91, 16))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_4)
        self.label_43.setGeometry(QtCore.QRect(370, 130, 51, 16))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.frame_4)
        self.label_44.setGeometry(QtCore.QRect(370, 100, 51, 16))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.frame_4)
        self.label_45.setGeometry(QtCore.QRect(370, 70, 51, 16))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.frame_4)
        self.label_46.setGeometry(QtCore.QRect(370, 160, 51, 16))
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.frame_4)
        self.label_47.setGeometry(QtCore.QRect(360, 200, 61, 16))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.frame_4)
        self.label_48.setGeometry(QtCore.QRect(370, 230, 51, 16))
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.frame_4)
        self.label_49.setGeometry(QtCore.QRect(440, 40, 71, 16))
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.frame_4)
        self.label_50.setGeometry(QtCore.QRect(450, 70, 91, 16))
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.frame_4)
        self.label_51.setGeometry(QtCore.QRect(450, 100, 111, 16))
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.frame_4)
        self.label_52.setGeometry(QtCore.QRect(450, 130, 111, 16))
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.frame_4)
        self.label_53.setGeometry(QtCore.QRect(560, 100, 51, 16))
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.frame_4)
        self.label_54.setGeometry(QtCore.QRect(560, 70, 51, 16))
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.frame_4)
        self.label_55.setGeometry(QtCore.QRect(560, 130, 51, 16))
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.frame_4)
        self.label_56.setGeometry(QtCore.QRect(640, 40, 71, 16))
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.frame_4)
        self.label_57.setGeometry(QtCore.QRect(650, 70, 81, 16))
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.frame_4)
        self.label_58.setGeometry(QtCore.QRect(650, 100, 91, 16))
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.frame_4)
        self.label_59.setGeometry(QtCore.QRect(650, 130, 121, 16))
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.frame_4)
        self.label_60.setGeometry(QtCore.QRect(650, 160, 131, 16))
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.frame_4)
        self.label_61.setGeometry(QtCore.QRect(790, 160, 51, 16))
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.frame_4)
        self.label_62.setGeometry(QtCore.QRect(790, 130, 51, 16))
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.frame_4)
        self.label_63.setGeometry(QtCore.QRect(790, 100, 51, 16))
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.frame_4)
        self.label_64.setGeometry(QtCore.QRect(790, 70, 51, 16))
        self.label_64.setObjectName("label_64")
        self.gridLayout.addWidget(self.frame_4, 2, 1, 1, 2)
        
        self.grabKeyboard()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prometheus"))
        self.label.setText(_translate("Form", "Remote Controlled Cars"))
        self.label_2.setText(_translate("Form", "Battery"))
        self.label_3.setText(_translate("Form", "72%"))
        self.label_4.setText(_translate("Form", "Status"))
        self.label_5.setText(_translate("Form", "In Motion"))
        self.label_6.setText(_translate("Form", "Tracker Color"))
        self.label_7.setText(_translate("Form", "Add Drone"))
        self.lineEdit.setPlaceholderText(_translate("Form", "IP Address"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Port"))
        self.pushButton.setText(_translate("Form", "Connect"))
        self.label_8.setText(_translate("Form", "Mapping Area ..."))
        self.pushButton_2.setText(_translate("Form", "Unregister"))
        self.pushButton_6.setText(_translate("Form", "Raw"))
        self.pushButton_7.setText(_translate("Form", "Depth"))
        self.pushButton_8.setText(_translate("Form", "Edge"))
        self.pushButton_9.setText(_translate("Form", "Surface"))
        self.label_65.setText(_translate("Form", "Vertices :"))
        self.label_66.setText(_translate("Form", "PolyCount :"))
        self.label_67.setText(_translate("Form", "Edges :"))
        self.label_68.setText(_translate("Form", "91k"))
        self.label_69.setText(_translate("Form", "285k"))
        self.label_70.setText(_translate("Form", "132k"))
        self.label_71.setText(_translate("Form", "Texture Load :"))
        self.label_72.setText(_translate("Form", "UV Segments :"))
        self.label_73.setText(_translate("Form", "382 MB"))
        self.label_74.setText(_translate("Form", "45"))
        self.label_9.setText(_translate("Form", "Navigation"))
        self.label_10.setText(_translate("Form", "Mapping Area"))
        self.label_11.setText(_translate("Form", "Radius"))
        self.label_12.setText(_translate("Form", "Softness"))
        self.label_13.setText(_translate("Form", "Traversal Type"))
        self.label_14.setText(_translate("Form", "Haste"))
        self.label_15.setText(_translate("Form", "Voxel Map Resolution"))
        self.checkBox.setText(_translate("Form", "Dynamic Voxel Breakdown"))
        self.label_16.setText(_translate("Form", "Mapping"))
        self.label_17.setText(_translate("Form", "Mapping Precision"))
        self.label_18.setText(_translate("Form", "Mapping Mode"))
        self.label_19.setText(_translate("Form", "Surface Approximation Threshold"))
        self.pushButton_3.setText(_translate("Form", "Begin Search"))
        self.pushButton_4.setText(_translate("Form", "Abort Search"))
        self.pushButton_5.setText(_translate("Form", "Switch To Manual Control"))
        self.label_20.setText(_translate("Form", "Mapping Info"))
        self.label_21.setText(_translate("Form", "Drone Data"))
        self.label_22.setText(_translate("Form", "Flight Time :"))
        self.label_23.setText(_translate("Form", "8m43s"))
        self.label_24.setText(_translate("Form", "Ground Height :"))
        self.label_25.setText(_translate("Form", "1.53m"))
        self.label_26.setText(_translate("Form", "Distance Covered :"))
        self.label_27.setText(_translate("Form", "83m"))
        self.label_28.setText(_translate("Form", "Average Speed :"))
        self.label_29.setText(_translate("Form", "0.7m/s"))
        self.label_30.setText(_translate("Form", "Displacement :"))
        self.label_31.setText(_translate("Form", "13m"))
        self.label_32.setText(_translate("Form", "Signal Strength :"))
        self.label_33.setText(_translate("Form", "0.88"))
        self.label_34.setText(_translate("Form", "Voxels Read :"))
        self.label_35.setText(_translate("Form", "1392"))
        self.label_36.setText(_translate("Form", "Voxel Data"))
        self.label_37.setText(_translate("Form", "Raw Voxels :"))
        self.label_38.setText(_translate("Form", "Space Voxels :"))
        self.label_39.setText(_translate("Form", "Occupied Voxels :"))
        self.label_40.setText(_translate("Form", "Total Voxels :"))
        self.label_41.setText(_translate("Form", "Voxel Volume :"))
        self.label_42.setText(_translate("Form", "Shattered Voxels :"))
        self.label_43.setText(_translate("Form", "744"))
        self.label_44.setText(_translate("Form", "490"))
        self.label_45.setText(_translate("Form", "6432"))
        self.label_46.setText(_translate("Form", "9744"))
        self.label_47.setText(_translate("Form", "31cmx31cm"))
        self.label_48.setText(_translate("Form", "43"))
        self.label_49.setText(_translate("Form", "Mapping Data"))
        self.label_50.setText(_translate("Form", "Mapping Volume :"))
        self.label_51.setText(_translate("Form", "Surfaces Generated :"))
        self.label_52.setText(_translate("Form", "Floor Area Covered :"))
        self.label_53.setText(_translate("Form", "22"))
        self.label_54.setText(_translate("Form", "500m^3"))
        self.label_55.setText(_translate("Form", "263m^2"))
        self.label_56.setText(_translate("Form", "General"))
        self.label_57.setText(_translate("Form", "Mapping Time :"))
        self.label_58.setText(_translate("Form", "Rooms Explored :"))
        self.label_59.setText(_translate("Form", "Estimated Completion :"))
        self.label_60.setText(_translate("Form", "Estimated Remaining Time :"))
        self.label_61.setText(_translate("Form", "3m"))
        self.label_62.setText(_translate("Form", "61%"))
        self.label_63.setText(_translate("Form", "4"))
        self.label_64.setText(_translate("Form", "8m"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
