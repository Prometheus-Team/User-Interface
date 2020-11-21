# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Prototype.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

# QWidget.setProperty("cssClass", [ "bold", "large", "rounded" ])
# palettes black #171820 orange #FDC029 lightdarkorange #DF861D darkorange #AA3D01 grey #BCB6AE

"""
.myButton {
	background:linear-gradient(to bottom, #c62d1f 5%, #f24437 100%);
	background-color:#c62d1f;
	border-radius:18px;
	border:1px solid #d02718;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Trebuchet MS;
	font-size:17px;
	padding:7px 25px;
	text-decoration:none;
}
.myButton:hover {
	background:linear-gradient(to bottom, #f24437 5%, #c62d1f 100%);
	background-color:#f24437;
}
.myButton:active {
	position:relative;
	top:1px;
}
"""

stylesheet = '''
#Form{
    background-color:#171820;
}

QPushButton{
    background:linear-gradient(to bottom, #c62d1f 5%, #f24437 100%);
	background-color:#c62d1f;
	border-radius:10px;
	border:1px solid #d02718;
	color:#ffffff;
	font-family:Trebuchet MS;
	font-size:12px;
    font-weight:bold;
	text-decoration:none;
}

QLabel{
    color:#ffffff;
	font-family:Trebuchet MS;
	font-size:12px;
    font-weight:bold;
}

QLabel[cssClass="values"]{
    color:#FDC029;
}

QComboBox{
    background-color:#BCB6AE;
    color:#ffffff;
	font-family:Trebuchet MS;
	font-size:12px;
    font-weight:bold;
    border-radius:5px;
}

QLineEdit{
    background-color:#BCB6AE;
    color:#ffffff;
	font-family:Trebuchet MS;
	font-size:12px;
    border-radius:8px;
}

QCheckBox{
    color:#ffffff;
	font-family:Trebuchet MS;
	font-size:12px;
}
'''

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
        Form.resize(1329, 886)
        Form.setAutoFillBackground(False)
        self.gridLayout_7 = QtWidgets.QGridLayout(Form)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setLineWidth(2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 1, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.value_1 = QtWidgets.QLabel(self.frame)
        self.value_1.setObjectName("value_1")
        self.gridLayout_2.addWidget(self.value_1, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.value_2 = QtWidgets.QLabel(self.frame)
        self.value_2.setObjectName("value_2")
        self.gridLayout_2.addWidget(self.value_2, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 2, 2, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.frame_3)
        self.openGLWidget.setMinimumSize(QtCore.QSize(431, 491))
        self.openGLWidget.setObjectName("openGLWidget")
        self.verticalLayout.addWidget(self.openGLWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setMinimumSize(QtCore.QSize(0, 26))
        self.pushButton_6.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 26))
        self.pushButton_7.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_8.setMinimumSize(QtCore.QSize(0, 26))
        self.pushButton_8.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_5.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 26))
        self.pushButton_9.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_5.addWidget(self.pushButton_9)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout_7.addWidget(self.frame_3, 0, 1, 2, 1)
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_5.setMidLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(self.frame_5)
        self.openGLWidget_2.setMinimumSize(QtCore.QSize(401, 441))
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.verticalLayout_4.addWidget(self.openGLWidget_2)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_65 = QtWidgets.QLabel(self.frame_5)
        self.label_65.setObjectName("label_65")
        self.horizontalLayout_13.addWidget(self.label_65)
        self.value_23 = QtWidgets.QLabel(self.frame_5)
        self.value_23.setObjectName("value_23")
        self.horizontalLayout_13.addWidget(self.value_23)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_66 = QtWidgets.QLabel(self.frame_5)
        self.label_66.setObjectName("label_66")
        self.horizontalLayout_12.addWidget(self.label_66)
        self.value_24 = QtWidgets.QLabel(self.frame_5)
        self.value_24.setObjectName("value_24")
        self.horizontalLayout_12.addWidget(self.value_24)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_67 = QtWidgets.QLabel(self.frame_5)
        self.label_67.setObjectName("label_67")
        self.horizontalLayout_11.addWidget(self.label_67)
        self.value_25 = QtWidgets.QLabel(self.frame_5)
        self.value_25.setObjectName("value_25")
        self.horizontalLayout_11.addWidget(self.value_25)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_16.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_71 = QtWidgets.QLabel(self.frame_5)
        self.label_71.setObjectName("label_71")
        self.horizontalLayout_15.addWidget(self.label_71)
        self.value_26 = QtWidgets.QLabel(self.frame_5)
        self.value_26.setObjectName("value_26")
        self.horizontalLayout_15.addWidget(self.value_26)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_72 = QtWidgets.QLabel(self.frame_5)
        self.label_72.setObjectName("label_72")
        self.horizontalLayout_14.addWidget(self.label_72)
        self.value_27 = QtWidgets.QLabel(self.frame_5)
        self.value_27.setObjectName("value_27")
        self.horizontalLayout_14.addWidget(self.value_27)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_16.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.gridLayout_7.addWidget(self.frame_5, 0, 2, 2, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setMaximumSize(QtCore.QSize(60, 34))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setMinimumSize(QtCore.QSize(231, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(231, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_10.addWidget(self.comboBox_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11, 0, QtCore.Qt.AlignRight)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(61, 16777215))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_9.addWidget(self.lineEdit_3)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12, 0, QtCore.Qt.AlignRight)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(61, 16777215))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_9.addWidget(self.lineEdit_4, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_3.setMinimumSize(QtCore.QSize(231, 0))
        self.comboBox_3.setMaximumSize(QtCore.QSize(231, 16777215))
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_8.addWidget(self.comboBox_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_7.addWidget(self.label_14)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(231, 16777215))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_7.addWidget(self.lineEdit_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.label_15)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(231, 16777215))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_6.addWidget(self.lineEdit_6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_6.addWidget(self.checkBox, 0, QtCore.Qt.AlignRight)
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setMaximumSize(QtCore.QSize(60, 34))
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_3.addWidget(self.label_17)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(211, 0))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(211, 16777215))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_4.setMinimumSize(QtCore.QSize(211, 0))
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_2.addWidget(self.comboBox_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_19 = QtWidgets.QLabel(self.frame_2)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_4.addWidget(self.label_19)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(211, 16777215))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_4.addWidget(self.lineEdit_8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(180, 26))
        self.pushButton_5.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(180, 26))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(180, 26))
        self.pushButton_3.setMaximumSize(QtCore.QSize(180, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_4)
        self.gridLayout_7.addWidget(self.frame_2, 1, 0, 2, 1)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_4.setLineWidth(2)
        self.frame_4.setMidLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 1, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.frame_4)
        self.label_36.setObjectName("label_36")
        self.gridLayout_6.addWidget(self.label_36, 1, 2, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.frame_4)
        self.label_49.setObjectName("label_49")
        self.gridLayout_6.addWidget(self.label_49, 1, 4, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.frame_4)
        self.label_56.setObjectName("label_56")
        self.gridLayout_6.addWidget(self.label_56, 1, 6, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_6.addWidget(self.comboBox_5, 2, 0, 1, 2)
        self.label_37 = QtWidgets.QLabel(self.frame_4)
        self.label_37.setObjectName("label_37")
        self.gridLayout_6.addWidget(self.label_37, 2, 2, 1, 1)
        self.value_10 = QtWidgets.QLabel(self.frame_4)
        self.value_10.setObjectName("value_10")
        self.gridLayout_6.addWidget(self.value_10, 2, 3, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.frame_4)
        self.label_50.setObjectName("label_50")
        self.gridLayout_6.addWidget(self.label_50, 2, 4, 1, 1)
        self.value_16 = QtWidgets.QLabel(self.frame_4)
        self.value_16.setObjectName("value_16")
        self.gridLayout_6.addWidget(self.value_16, 2, 5, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.frame_4)
        self.label_57.setObjectName("label_57")
        self.gridLayout_6.addWidget(self.label_57, 2, 6, 1, 1)
        self.value_19 = QtWidgets.QLabel(self.frame_4)
        self.value_19.setObjectName("value_19")
        self.gridLayout_6.addWidget(self.value_19, 2, 7, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.frame_4)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 3, 0, 1, 1)
        self.value_3 = QtWidgets.QLabel(self.frame_4)
        self.value_3.setObjectName("value_3")
        self.gridLayout_6.addWidget(self.value_3, 3, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.frame_4)
        self.label_38.setObjectName("label_38")
        self.gridLayout_6.addWidget(self.label_38, 3, 2, 1, 1)
        self.value_11 = QtWidgets.QLabel(self.frame_4)
        self.value_11.setObjectName("value_11")
        self.gridLayout_6.addWidget(self.value_11, 3, 3, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.frame_4)
        self.label_51.setObjectName("label_51")
        self.gridLayout_6.addWidget(self.label_51, 3, 4, 1, 1)
        self.value_17 = QtWidgets.QLabel(self.frame_4)
        self.value_17.setObjectName("value_17")
        self.gridLayout_6.addWidget(self.value_17, 3, 5, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.frame_4)
        self.label_58.setObjectName("label_58")
        self.gridLayout_6.addWidget(self.label_58, 3, 6, 1, 1)
        self.value_20 = QtWidgets.QLabel(self.frame_4)
        self.value_20.setObjectName("value_20")
        self.gridLayout_6.addWidget(self.value_20, 3, 7, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_4)
        self.label_24.setObjectName("label_24")
        self.gridLayout_6.addWidget(self.label_24, 4, 0, 1, 1)
        self.value_4 = QtWidgets.QLabel(self.frame_4)
        self.value_4.setObjectName("value_4")
        self.gridLayout_6.addWidget(self.value_4, 4, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.frame_4)
        self.label_39.setObjectName("label_39")
        self.gridLayout_6.addWidget(self.label_39, 4, 2, 1, 1)
        self.value_12 = QtWidgets.QLabel(self.frame_4)
        self.value_12.setObjectName("value_12")
        self.gridLayout_6.addWidget(self.value_12, 4, 3, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.frame_4)
        self.label_52.setObjectName("label_52")
        self.gridLayout_6.addWidget(self.label_52, 4, 4, 1, 1)
        self.value_18 = QtWidgets.QLabel(self.frame_4)
        self.value_18.setObjectName("value_18")
        self.gridLayout_6.addWidget(self.value_18, 4, 5, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.frame_4)
        self.label_59.setObjectName("label_59")
        self.gridLayout_6.addWidget(self.label_59, 4, 6, 1, 1)
        self.value_21 = QtWidgets.QLabel(self.frame_4)
        self.value_21.setObjectName("value_21")
        self.gridLayout_6.addWidget(self.value_21, 4, 7, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.frame_4)
        self.label_26.setObjectName("label_26")
        self.gridLayout_6.addWidget(self.label_26, 5, 0, 1, 1)
        self.value_5 = QtWidgets.QLabel(self.frame_4)
        self.value_5.setObjectName("value_5")
        self.gridLayout_6.addWidget(self.value_5, 5, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.frame_4)
        self.label_40.setObjectName("label_40")
        self.gridLayout_6.addWidget(self.label_40, 5, 2, 1, 1)
        self.value_13 = QtWidgets.QLabel(self.frame_4)
        self.value_13.setObjectName("value_13")
        self.gridLayout_6.addWidget(self.value_13, 5, 3, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.frame_4)
        self.label_60.setObjectName("label_60")
        self.gridLayout_6.addWidget(self.label_60, 5, 6, 1, 1)
        self.value_22 = QtWidgets.QLabel(self.frame_4)
        self.value_22.setObjectName("value_22")
        self.gridLayout_6.addWidget(self.value_22, 5, 7, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.frame_4)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 6, 0, 1, 1)
        self.value_6 = QtWidgets.QLabel(self.frame_4)
        self.value_6.setObjectName("value_6")
        self.gridLayout_6.addWidget(self.value_6, 6, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.frame_4)
        self.label_41.setObjectName("label_41")
        self.gridLayout_6.addWidget(self.label_41, 6, 2, 1, 1)
        self.value_14 = QtWidgets.QLabel(self.frame_4)
        self.value_14.setObjectName("value_14")
        self.gridLayout_6.addWidget(self.value_14, 6, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.frame_4)
        self.label_30.setObjectName("label_30")
        self.gridLayout_6.addWidget(self.label_30, 7, 0, 1, 1)
        self.value_7 = QtWidgets.QLabel(self.frame_4)
        self.value_7.setObjectName("value_7")
        self.gridLayout_6.addWidget(self.value_7, 7, 1, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.frame_4)
        self.label_42.setObjectName("label_42")
        self.gridLayout_6.addWidget(self.label_42, 7, 2, 1, 1)
        self.value_15 = QtWidgets.QLabel(self.frame_4)
        self.value_15.setObjectName("value_15")
        self.gridLayout_6.addWidget(self.value_15, 7, 3, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.frame_4)
        self.label_32.setObjectName("label_32")
        self.gridLayout_6.addWidget(self.label_32, 8, 0, 1, 1)
        self.value_8 = QtWidgets.QLabel(self.frame_4)
        self.value_8.setObjectName("value_8")
        self.gridLayout_6.addWidget(self.value_8, 8, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.frame_4)
        self.label_34.setObjectName("label_34")
        self.gridLayout_6.addWidget(self.label_34, 9, 0, 1, 1)
        self.value_9 = QtWidgets.QLabel(self.frame_4)
        self.value_9.setObjectName("value_9")
        self.gridLayout_6.addWidget(self.value_9, 9, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_4, 2, 1, 1, 2)
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 21))
        self.frame_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_6.setMidLineWidth(0)
        self.frame_6.setObjectName("frame_6")
        self.widget = QtWidgets.QWidget(self.frame_6)
        self.widget.setGeometry(QtCore.QRect(10, 0, 1291, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_75 = QtWidgets.QLabel(self.widget)
        self.label_75.setObjectName("label_75")
        self.horizontalLayout_17.addWidget(self.label_75)
        self.value_28 = QtWidgets.QLabel(self.widget)
        self.value_28.setObjectName("value_28")
        self.horizontalLayout_17.addWidget(self.value_28)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem)
        self.label_76 = QtWidgets.QLabel(self.widget)
        self.label_76.setObjectName("label_76")
        self.horizontalLayout_17.addWidget(self.label_76, 0, QtCore.Qt.AlignRight)
        self.value_29 = QtWidgets.QLabel(self.widget)
        self.value_29.setObjectName("value_29")
        self.horizontalLayout_17.addWidget(self.value_29, 0, QtCore.Qt.AlignLeft)
        self.gridLayout_7.addWidget(self.frame_6, 3, 0, 1, 3)
        
        self.value_1.setProperty("cssClass", "values")
        self.value_2.setProperty("cssClass", "values")
        self.value_3.setProperty("cssClass", "values")
        self.value_4.setProperty("cssClass", "values")
        self.value_5.setProperty("cssClass", "values")
        self.value_6.setProperty("cssClass", "values")
        self.value_7.setProperty("cssClass", "values")
        self.value_8.setProperty("cssClass", "values")
        self.value_9.setProperty("cssClass", "values")
        self.value_10.setProperty("cssClass", "values")
        self.value_11.setProperty("cssClass", "values")
        self.value_12.setProperty("cssClass", "values")
        self.value_13.setProperty("cssClass", "values")
        self.value_14.setProperty("cssClass", "values")
        self.value_15.setProperty("cssClass", "values")
        self.value_16.setProperty("cssClass", "values")
        self.value_17.setProperty("cssClass", "values")
        self.value_18.setProperty("cssClass", "values")
        self.value_19.setProperty("cssClass", "values")
        self.value_20.setProperty("cssClass", "values")
        self.value_21.setProperty("cssClass", "values")
        self.value_22.setProperty("cssClass", "values")
        self.value_23.setProperty("cssClass", "values")
        self.value_24.setProperty("cssClass", "values")
        self.value_25.setProperty("cssClass", "values")
        self.value_26.setProperty("cssClass", "values")
        self.value_27.setProperty("cssClass", "values")
        self.value_28.setProperty("cssClass", "values")
        self.value_29.setProperty("cssClass", "values")

        self.grabKeyboard()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Prometheus"))
        self.label.setText(_translate("Form", "Remote Controlled Car"))
        self.label_2.setText(_translate("Form", "Battery"))
        self.label_6.setText(_translate("Form", "Tracker Color"))
        self.value_1.setText(_translate("Form", "72%"))
        self.label_8.setText(_translate("Form", "         Mapping Area ..."))
        self.label_4.setText(_translate("Form", "Status"))
        self.value_2.setText(_translate("Form", "In Motion"))
        self.pushButton_2.setText(_translate("Form", "Unregister"))
        self.label_7.setText(_translate("Form", "Add Drone"))
        self.lineEdit.setPlaceholderText(_translate("Form", "IP Address"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Port"))
        self.pushButton.setText(_translate("Form", "Connect"))
        self.pushButton_6.setText(_translate("Form", "Raw"))
        self.pushButton_7.setText(_translate("Form", "Depth"))
        self.pushButton_8.setText(_translate("Form", "Edge"))
        self.pushButton_9.setText(_translate("Form", "Surface"))
        self.label_65.setText(_translate("Form", " Vertices :"))
        self.value_23.setText(_translate("Form", "285k"))
        self.label_66.setText(_translate("Form", " PolyCount :"))
        self.value_24.setText(_translate("Form", "91k"))
        self.label_67.setText(_translate("Form", " Edges :"))
        self.value_25.setText(_translate("Form", "132k"))
        self.label_71.setText(_translate("Form", "Texture Load :"))
        self.value_26.setText(_translate("Form", "382 MB"))
        self.label_72.setText(_translate("Form", "UV Segments :"))
        self.value_27.setText(_translate("Form", "45"))
        self.label_9.setText(_translate("Form", "Navigation"))
        self.label_10.setText(_translate("Form", "   Mapping Area"))
        self.label_11.setText(_translate("Form", "Radius"))
        self.label_12.setText(_translate("Form", "Softness"))
        self.label_13.setText(_translate("Form", "   Traversal Type"))
        self.label_14.setText(_translate("Form", "   Haste"))
        self.label_15.setText(_translate("Form", "   Voxel Map Resolution"))
        self.checkBox.setText(_translate("Form", "Dynamic Voxel Breakdown"))
        self.label_16.setText(_translate("Form", "Mapping"))
        self.label_17.setText(_translate("Form", "   Mapping Precision"))
        self.label_18.setText(_translate("Form", "   Mapping Mode"))
        self.label_19.setText(_translate("Form", "  Surface Approximation Threshold"))
        self.pushButton_5.setText(_translate("Form", "Switch To Manual Control"))
        self.pushButton_4.setText(_translate("Form", "Abort Search"))
        self.pushButton_3.setText(_translate("Form", "Begin Search"))
        self.label_20.setText(_translate("Form", "Mapping Info"))
        self.label_21.setText(_translate("Form", "Drone Data"))
        self.label_36.setText(_translate("Form", "Voxel Data"))
        self.label_49.setText(_translate("Form", "Mapping Data"))
        self.label_56.setText(_translate("Form", "General"))
        self.label_37.setText(_translate("Form", "   Raw Voxels :"))
        self.value_10.setText(_translate("Form", "6432"))
        self.label_50.setText(_translate("Form", "   Mapping Volume :"))
        self.value_16.setText(_translate("Form", "500m^3"))
        self.label_57.setText(_translate("Form", "   Mapping Time :"))
        self.value_19.setText(_translate("Form", "8m"))
        self.label_22.setText(_translate("Form", "   Motion Time :"))
        self.value_3.setText(_translate("Form", "8m43s"))
        self.label_38.setText(_translate("Form", "   Space Voxels :"))
        self.value_11.setText(_translate("Form", "490"))
        self.label_51.setText(_translate("Form", "   Surfaces Generated :"))
        self.value_17.setText(_translate("Form", "22"))
        self.label_58.setText(_translate("Form", "   Rooms Explored :"))
        self.value_20.setText(_translate("Form", "4"))
        self.label_24.setText(_translate("Form", "   Ground Height :"))
        self.value_4.setText(_translate("Form", "1.53m"))
        self.label_39.setText(_translate("Form", "   Occupied Voxels :"))
        self.value_12.setText(_translate("Form", "744"))
        self.label_52.setText(_translate("Form", "   Floor Area Covered :"))
        self.value_18.setText(_translate("Form", "263m^2"))
        self.label_59.setText(_translate("Form", "   Estimated Completion :"))
        self.value_21.setText(_translate("Form", "61%"))
        self.label_26.setText(_translate("Form", "   Distance Covered :"))
        self.value_5.setText(_translate("Form", "83m"))
        self.label_40.setText(_translate("Form", "   Total Voxels :"))
        self.value_13.setText(_translate("Form", "9744"))
        self.label_60.setText(_translate("Form", "   Estimated Remaining Time :"))
        self.value_22.setText(_translate("Form", "3m"))
        self.label_28.setText(_translate("Form", "   Average Speed :"))
        self.value_6.setText(_translate("Form", "0.7m/s"))
        self.label_41.setText(_translate("Form", "   Voxel Volume :"))
        self.value_14.setText(_translate("Form", "31cmx31cm"))
        self.label_30.setText(_translate("Form", "   Displacement :"))
        self.value_7.setText(_translate("Form", "13m"))
        self.label_42.setText(_translate("Form", "   Shattered Voxels :"))
        self.value_15.setText(_translate("Form", "43"))
        self.label_32.setText(_translate("Form", "   Signal Strength :"))
        self.value_8.setText(_translate("Form", "0.88"))
        self.label_34.setText(_translate("Form", "   Voxels Read :"))
        self.value_9.setText(_translate("Form", "1392"))
        self.label_75.setText(_translate("Form", "Status: "))
        self.value_28.setText(_translate("Form", "Idle"))
        self.label_76.setText(_translate("Form", "Version: "))
        self.value_29.setText(_translate("Form", "1.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())