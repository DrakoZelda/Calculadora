# -*- coding: utf-8 -*-
import sys
sys.path.append('../Modelos')
import parser
from Calculadora import *


class MainController():

    def __init__(self, una_ventana):
        self.Calculadora = Calculadora()
        self.ventana = una_ventana
        self.cal = self.ventana.display

    def handler_clear(self):
        self.ventana.display.cursorBackward(True)

    def handler_clearAll(self):
        self.ventana.display.clear()

    def handler_izquierda(self):
        self.ventana.display.cursorBackward(False)

    def handler_derecha(self):
        self.ventana.display.cursorForward(False)

    def handler_write(self):
        le = str(self.ventana.display.text())
        self.trigger = self.ventana.sender()
        c = str(self.trigger.text())
        if (le == 0) or (le == ""):
            self.ventana.display.setText(c)
        else:
            s = le + c
            self.ventana.display.setText(s)

    def operation(self):
        f = str(self.ventana.display.text())
        ff = parser.expr(f).compile()
        newF = eval(ff)
        if ! in myList:

        self.Calculadora.resultado = newF
        self.ventana.display.setText(str(newF))








    #dolar = 9.230
    #dolarBlue = 15.84
    #euro = 10.24
    #yen = 0.077
