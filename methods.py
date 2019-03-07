#-*- coding: utf-8 -*-
import math
import sympy

class Methods:
    def __init__(self):
        self.methods= [
                {
                    "name": "Euler Simples",
                    "function": self.euler
                    },
                {
                    "name": "Euler Inverso",
                    "function": self.inverse_euler
                    },
                {
                    "name": "Euler Composto",
                    "function": self.composite_euler
                    },
                ]

    def __getitem__(self, key):
        return self.methods[key]

    def euler(self, t, ys, f, h):
        y = ys[t]
        return y + f(t, y)*h

    def inverse_euler(self, t, ys, f, h):
        y = ys[t]
        y1 = self.euler(t, ys, f, h)
        return y + f(t + h, y1)*h

    def composite_euler(self, t, ys, f, h):
        y = ys[t]
        y1 = self.euler(t, ys, f, h)
        return y + (f(t, y) + f(t+h, y1))*h/2
