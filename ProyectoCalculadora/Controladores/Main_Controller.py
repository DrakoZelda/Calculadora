# -*- coding: utf-8 -*-
import sys
sys.path.append('../Modelos')
from Calculadora import *


class MainController():

    def __init__(self, una_ventana):
        self.Calculadora = Calculadora()
        self.ventana = una_ventana

    def handler_clear(self):
        self.ventana.entrada_texto.backspace()

    def handler_clearAll(self):
        self.ventana.entrada_texto.clear()

    def handler_izquierda(self):
        self.ventana.entrada_texto.cursorBackward(false)

    def handler_derecha(self):
        self.ventana.entrada_texto.cursorForward(false)

    def handler_write(self, ):


