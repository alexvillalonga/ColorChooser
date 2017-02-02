# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

from interficieEx10 import Ui_MainWindow

class SelectorColors(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SelectorColors, self).__init__(parent)
        self.setupUi(self)
        self.cambiarColorFondo()
        self.codigoColor()
        self.centrarFinestra()
        
        #Control dels botons
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"),self.paleta)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"),self.sortir)
        
    
    def cambiarColorFondo(self):
        color = QColor(self.horizontalSlider.value(),self.horizontalSlider_2.value(),self.horizontalSlider_3.value())
        red = color.red()
        green = color.green()
        blue = color.blue()
        self.lineEdit_2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(" + str(red) + ", " + str(green) + ", " + str(blue) + ");")
        self.codigoColor()
    
    def paleta(self):
        color = QColor(self.horizontalSlider.value(),self.horizontalSlider_2.value(),self.horizontalSlider_3.value())
        nuevoColor = QColorDialog.getColor(color)
        self.horizontalSlider.setValue(nuevoColor.red())
        self.horizontalSlider_2.setValue(nuevoColor.green())
        self.horizontalSlider_3.setValue(nuevoColor.blue())
        self.cambiarColorFondo()
        
    
    def codigoColor(self):
        digitHex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

        vermell = self.horizontalSlider.value()
        verd = self.horizontalSlider_2.value()
        blau = self.horizontalSlider_3.value()
        
        valorRojo = []
        valorVerde = []
        valorAzul = []
        
        codi = '#'
        
        if vermell < 16:
            valorRojo.append(str(0))
            aux = vermell % 16
            valorRojo.append(digitHex[aux])
        else: 
            while vermell > 0:
                aux = vermell % 16
                valorRojo.append(digitHex[aux])
                vermell = vermell / 16
            valorRojo.reverse()
        for i in valorRojo:
            codi += i
        
        if verd < 16:
            valorVerde.append(str(0))
            aux = verd % 16
            valorVerde.append(digitHex[aux])
        else:
            while verd > 0:
                aux = verd % 16
                valorVerde.append(digitHex[aux])
                verd = verd / 16
            valorVerde.reverse()
        for i in valorVerde:
            codi += i
     
        if blau < 16:
            valorAzul.append(str(0))
            aux = blau % 16
            valorAzul.append(digitHex[aux])
        else:
            while blau > 0:
                aux = blau % 16
                valorAzul.append(digitHex[aux])
                blau = blau / 16
            valorAzul.reverse()
        for i in valorAzul:
            codi += i
        
        self.lineEdit.setText(codi)
    
    def sortir(self):
        app.quit()
        
    def centrarFinestra(self):
        #obtenim la geometria de la finestra
        qr = self.frameGeometry()
        #obtenim la resolució de la pantalla i calcula el punt central
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        #movem el centre de la nostra finestra al centre de la pantalla
        qr.moveCenter(cp)
        self.move(qr.topLeft())
      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectorColors()
    window.show()
    
    #Sortir del sistema
    sys.exit(app.exec_())
    
