# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex10.ui'
#
# Created: Mon Nov 14 17:58:17 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 300)
        MainWindow.setMinimumSize(QtCore.QSize(600, 300))
        MainWindow.setMaximumSize(QtCore.QSize(600, 300))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 250, 401, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);\n"
"color: rgb(254, 254, 254);\n"
"font-weight: bold;\n"
"border-radius: 5px;"))
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 250, 121, 31))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(0, 170, 255);\n"
"color: rgb(254, 254, 254);\n"
"font-weight: bold;\n"
"border-radius: 5px;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 230, 581, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 180, 113, 41))
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-2, -1, 601, 41))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(188, 237, 81);\n"
"font-weight: bold;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 50, 321, 161))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalSlider = QtGui.QSlider(self.layoutWidget)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.setProperty("value", 248)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(10)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.horizontalSlider_2 = QtGui.QSlider(self.layoutWidget)
        self.horizontalSlider_2.setMaximum(255)
        self.horizontalSlider_2.setProperty("value", 221)
        self.horizontalSlider_2.setSliderPosition(221)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_2.setTickInterval(10)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.verticalLayout.addWidget(self.horizontalSlider_2)
        self.horizontalSlider_3 = QtGui.QSlider(self.layoutWidget)
        self.horizontalSlider_3.setMaximum(255)
        self.horizontalSlider_3.setProperty("value", 161)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setTickPosition(QtGui.QSlider.TicksAbove)
        self.horizontalSlider_3.setTickInterval(10)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        self.verticalLayout.addWidget(self.horizontalSlider_3)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(470, 50, 61, 161))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"font-weight: bold;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"font-weight: bold;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);\n"
"font-weight: bold;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(542, 50, 51, 161))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtGui.QLabel(self.layoutWidget2)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.layoutWidget2)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(self.layoutWidget2)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_3.addWidget(self.label_7)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 60, 113, 101))
        self.lineEdit_2.setStyleSheet(_fromUtf8("border-radius: 10px;\n"))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_5.setNum)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_6.setNum)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label_7.setNum)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.cambiarColorFondo)
        QtCore.QObject.connect(self.horizontalSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.cambiarColorFondo)
        QtCore.QObject.connect(self.horizontalSlider_3, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), MainWindow.cambiarColorFondo)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Selector de colors (by Ins Marianao)", None))
        self.pushButton.setText(_translate("MainWindow", "Paleta de colors", None))
        self.pushButton_2.setText(_translate("MainWindow", "Sortir", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Selector de colors</p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "RED", None))
        self.label_3.setText(_translate("MainWindow", "GREEN", None))
        self.label_4.setText(_translate("MainWindow", "BLUE", None))
        self.label_5.setText(_translate("MainWindow", str(self.horizontalSlider.value()), None))
        self.label_6.setText(_translate("MainWindow", str(self.horizontalSlider_2.value()), None))
        self.label_7.setText(_translate("MainWindow", str(self.horizontalSlider_3.value()), None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

