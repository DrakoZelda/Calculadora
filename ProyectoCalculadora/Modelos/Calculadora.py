# -*- coding: utf-8 -*-
from math import *


class Calculadora():
    def __init__(self):
        self.resultado = 0
        self.conversion = ""
        self.conversionMonetaria = 0

    def suma(self, x, y):
        self.resultado = x + y

    def resta(self, x, y):
        self.resultado = x - y

    def multiplicacion(self, x, y):
        self.resultado = x * y

    def division(self, x, y):
        self.resultado = x / y

    def raiz_Cuadrada(self, x):
        self.resultado = math.sqrt(x)

    def factorial(self, x):
        self.resultado = math.factorial(x)

    def exponente(self, x, y):
        self.resultado = math.pow(x, y)

    def porcentaje(self, x, y):
        self.resultado = math.fmod(x, y)