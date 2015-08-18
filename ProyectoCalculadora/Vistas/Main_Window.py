# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
sys.path.append('../Controladores')
from Main_Controller import *


class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.controlador = MainController(self)
        self.init_ui()

    def init_ui(self):
        display = QtGui.QLineEdit()
        self = QtGui.QLabel()


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
        izquierda = QtGui.QPushButton('←')
        arriba = QtGui.QPushButton('↑')
        abajo = QtGui.QPushButton('↓')
        raiz = QtGui.QPushButton('√')
        ans = QtGui.QPushButton('Ans')
        porcentaje = QtGui.QPushButton('%')
        exponenteDiez = QtGui.QPushButton('x10ª')
        parentesisIzquierdo = QtGui.QPushButton('(')
        parentesisDerecho = QtGui.QPushButton(')')
        cuadrado = QtGui.QPushButton('x²')
        potencia = QtGui.QPushButton('xª')
        factorial = QtGui.QPushButton('!')
        yen = QtGui.QPushButton('¥')
        libra = QtGui.QPushButton('£')
        euro = QtGui.QPushButton('€')
        peso = QtGui.QPushButton('$a')
        dolar = QtGui.QPushButton('$')
        bitCoin = QtGui.QPushButton('฿')
        clear = QtGui.QPushButton('<')
        clearAll = QtGui.QPushButton('<<')