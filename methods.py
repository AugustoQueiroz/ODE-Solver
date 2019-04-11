#-*- coding: utf-8 -*-
import math
import sympy

class Methods:
    def __init__(self):
        self.adams_bashforth_coeficients = [
            [],                                                                                                     # Coeficients for order 0
            [1],                                                                                                    # Coeficients for order 1
            [3.0/2.0, -1.0/2.0],                                                                                    # Coeficients for order 2
            [23.0/12.0, -16.0/12.0, 5.0/12.0],                                                                      # Coeficients for order 3
            [55.0/24.0, -59.0/24.0, 37.0/24.0, -3.0/24.0],                                                          # Coeficients for order 4
            [1901.0/720.0, -2774.0/720.0, 2616.0/720.0, -1274.0/720.0, 251.0/720.0],                                # Coeficients for order 5
            [4277.0/1440.0, -3*2641.0/1440.0, 2*4991.0/1440.0, -2*3649.0/1440.0, 3*959.0/1440.0, -5*95.0/1440.0],   # Coeficients for order 6
            [],                                                                                                     # Coeficients for order 7
            [],                                                                                                     # Coeficients for order 8
        ]

        self.adams_moulton_coeficients = [
            [],                                                                                                     # Coeficients for order 0
            [1],                                                                                                    # Coeficients for order 1
            [0.5, 0.5],                                                                                             # Coeficients for order 2
            [5.0/12.0, 8.0/12.0, -1.0/12.0],                                                                        # Coeficients for order 3
            [9.0/24.0, 19.0/24.0, -5.0/24.0, 1.0/24.0],                                                             # Coeficients for order 4
            [251.0/720.0, 2*323.0/720.0, -24*11.0/720.0, 2*53.0/720.0, -19.0/720.0],                                # Coeficients for order 5
            [5*95.0/1440.0, 1427.0/1440.0, -6*133.0/1440.0, 2*241.0/1440.0, -173.0/1440.0, 9*3.0/1440.0],           # Coeficients for order 6
            [],                                                                                                     # Coeficients for order 7
            []                                                                                                      # Coeficients for order 8
        ]

        self.methods = [
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
                {
                    "name": "Runge-Kutta",
                    "function": self.runge_kutta
                    },
                {
                    "name": "Adams-Bashforth",
                    "function": self.adams_bashforth
                    },
                {
                    "name": "Adams-Moulton",
                    "function": self.adams_moulton
                    },
                {
                    "name": "Euler Inverso [Implícito]",
                    "function": self.inverse_euler_implicit
                    },
                    {
                    "name": "Euler Composto [Implícito]",
                    "function": self.composite_euler_implicit
                    }
                ]

    def __getitem__(self, key):
        if key >= 5 and key <= 11:
            key = 4
        elif key >= 12 and key <= 19:
            key = 5
        elif key >= 20 and key <= 22:
            key = key - 14
        return self.methods[key]

    def euler(self, ts, ys, index, f, h):
        t = ts[index]
        y = ys[index]
        return y + f(t, y)*h

    def inverse_euler(self, ts, ys, index, f, h):
        t = ts[index]
        y = ys[index]
        y1 = self.euler(ts, ys, index, f, h)
        return y + f(t + h, y1)*h

    def inverse_euler_implicit(self, ts, ys, index, f_expr, h):
        t, y, y1 = sympy.symbols("t y y1")

        f_expr = f_expr.subs(t, ts[index+1]).subs(y, y1)

        return sympy.solve(sympy.Eq(ys[index] + f_expr*h, y1), y1).pop()

    def composite_euler(self, ts, ys, index, f, h):
        t = ts[index]
        y = ys[index]
        y1 = self.runge_kutta(ts, ys, index, f, h)
        return y + (f(t, y) + f(t+h, y1))*h/2

    def composite_euler_implicit(self, ts, ys, index, f_expr, h):
        t, y, y1 = sympy.symbols("t y y1")

        f_expr += f_expr.subs(t, ts[index]).subs(y, ys[index])
        f_expr = f_expr.subs(t, ts[index+1]).subs(y, y1)

        return sympy.solve(sympy.Eq(ys[index] + f_expr*h/2, y1), y1).pop()

    def runge_kutta(self, ts, ys, index, f, h):
        t = ts[index]
        y = ys[index]
        k1 = f(t, y)
        k2 = f(t + h/2, y + k1*h/2)
        k3 = f(t + h/2, y + k2*h/2)
        k4 = f(t + h, y + h*k3)
        return y + (k1 + 2*k2 + 2*k3 + k4)*h/6

    def adams_bashforth(self, order, ts, ys, index, f, h):
        fs = []
        for i in range(0, order):
            t = ts[index - i]
            y = ys[index - i]
            fs.append(f(t, y))

        y = ys[index]
        for i, f_i in enumerate(fs):
            y += self.adams_bashforth_coeficients[order][i]*f_i*h
        return y

    def adams_moulton(self, order, ts, ys, index, f, h):
        #if order == 2: return self.composite_euler(ts, ys, index, f, h)
        ys[index+1] = self.runge_kutta(ts, ys, index, f, h)
        fs = []
        for i in range(0, order):
            fs.append(f(ts[index+1-i], ys[index+1-i]))

        y = ys[index]
        for i, f_i in enumerate(fs):
            y += self.adams_moulton_coeficients[order][i]*f_i*h
        return y