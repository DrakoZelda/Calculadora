# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
sys.path.append('../Controlador')
from Main_Controller import *

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.controlador = MainController(self)
        self.init_ui()

    def init_ui(self):
        self.label = QtGui.Qlabel()
        h_layout = QtGui.QHBoxLayout()
        v_layout = QtGui.QVBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.entrada_texto)
        self.entrada_texto = QtGui.QtLineEdit()
        igual = QtGui.QPushButton('=')
        menos = QtGui.QPushButton('-')
        mas = QtGui.QPushButton('+')
        negativo = QtGui.QPushButton('(-)')
        uno = QtGui.QPushButton('1')
        dos = QtGui.QPushButton('2')
        tres = QtGui.QPushButton('3')
        cuatro = QtGui.QPushButton('4')
        cinco = QtGui.QPushButton('5')
        seis = QtGui.QPushButton('6')
        siete = QtGui.QPushButton('7')
        ocho = QtGui.QPushButton('8')
        nueve = QtGui.QPushButton('9')
        cero = QtGui.QPushButton('0')
        derecha = QtGui.QPushButton('>')
        izquierda = QtGui.QPushButton('<')
        v_layout.addWidget(uno)
        v_layout.addWidget(dos)
        v_layout.addWidget(tres)
        v_layout.addWidget(cuatro)
        v_layout.addWidget(cinco)
        v_layout.addWidget(seis)
        v_layout.addWidget(siete)
        v_layout.addWidget(ocho)
        v_layout.addWidget(nueve)
        v_layout.addWidget(cero)
        v_layout.addWidget(igual)
        v_layout.addWidget(menos)
        v_layout.addWidget(mas)
        v_layout.addWidget(negativo)
        h_layout.addWidget(derecha)
        h_layout.addWidget(izquierda)



        self.setLayout(h_layout)
        self.setWindowTitle('Launcher Nid for zpid')
        self.setGeometry(200, 200, 200, 200)
        self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())