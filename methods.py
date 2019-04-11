#-*- coding: utf-8 -*-
import math
import sympy

class Methods:
    def __init__(self):
        self.adams_bashforth_coeficients = [
            [],                                                                                                                                 # Coeficients for order 0
            [1],                                                                                                                                # Coeficients for order 1
            [3.0/2.0, -1.0/2.0],                                                                                                                # Coeficients for order 2
            [23.0/12.0, -4.0/3.0, 5.0/12.0],                                                                                                    # Coeficients for order 3
            [55.0/24.0, -59.0/24.0, 37.0/24.0, -3.0/8.0],                                                                                       # Coeficients for order 4
            [1901.0/720.0, -1387.0/360.0, 109.0/30.0, -637.0/360.0, 251.0/720.0],                                                               # Coeficients for order 5
            [4277.0/1440.0, -2641.0/480.0, 4991.0/720.0, -3649.0/720.0, 959.0/480.0, -95.0/288.0],                                              # Coeficients for order 6
            [198721.0/60480, -18637.0/2520.0, 235183.0/20160.0, -10754.0/945.0, 135713.0/20160.0, -5603.0/2520.0, 19087.0/60480.0],             # Coeficients for order 7
            [16083.0/4480.0, -1152169.0/120960.0, 242653.0/13440.0, -296053.0/13440.0, 2102243.0/120960.0, -115747.0/13440.0, 32863.0/13440.0]  # Coeficients for order 8
        ]

        self.adams_moulton_coeficients = [
            [],                                                                                                                                         # Coeficients for order 0
            [1],                                                                                                                                        # Coeficients for order 1
            [0.5, 0.5],                                                                                                                                 # Coeficients for order 2
            [5.0/12.0, 2.0/3.0, -1.0/12.0],                                                                                                             # Coeficients for order 3
            [3.0/8.0, 19.0/24.0, -5.0/24.0, 1.0/24.0],                                                                                                  # Coeficients for order 4
            [251.0/720.0, 323.0/360.0, -11.0/30.0, 53.0/360.0, -19.0/720.0],                                                                            # Coeficients for order 5
            [95.0/288.0, 1427.0/1440.0, -133.0/240.0, 241.0/720.0, -173.0/1440.0, 3.0/160.0],                                                           # Coeficients for order 6
            [19087.0/60480.0, 2713.0/2520.0, -15487.0/20160.0, 586.0/945.0, -6737.0/20160, 263.0/2520.0, -863.0/60480.0],                               # Coeficients for order 7
            [5257.0/17280.0, 139849.0/120960.0, -4511.0/4480.0, 123133.0/120960.0, -88547.0/120960.0, 1537.0/4480.0, -11351.0/120960.0, 275.0/24192.0]  # Coeficients for order 8
        ]

        self.methods = {
                "euler" : {
                    "name": "Euler Simples",
                    "function": self.euler
                    },
                "euler_inverso": {
                    "name": "Euler Inverso",
                    "function": self.inverse_euler
                    },
                "euler_aprimorado": {
                    "name": "Euler Composto",
                    "function": self.composite_euler
                    },
                "runge_kutta": {
                    "name": "Runge-Kutta",
                    "function": self.runge_kutta
                    },
                "adam_bashforth": {
                    "name": "Adams-Bashforth",
                    "function": self.adams_bashforth
                    },
                "adam_multon": {
                    "name": "Adams-Moulton",
                    "function": self.adams_moulton
                    },
                "euler_inverso_implicito": {
                    "name": "Euler Inverso [Implícito]",
                    "function": self.inverse_euler_implicit
                    },
                "euler_aprimorado_implicito": {
                    "name": "Euler Composto [Implícito]",
                    "function": self.composite_euler_implicit
                    },
                "adam_moulton_implicito": {
                    "name": "Adams-Moulton [Implícito]",
                    "function": self.adams_moulton_implicit
                    }
                }

    def __getitem__(self, key):
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


        coeficients = self.adams_bashforth_coeficients[order]
        y = ys[index] + sum([c*f_i for c, f_i in zip(coeficients, fs)])*h
        return y

    def adams_moulton(self, order, ts, ys, index, f, h):
        #if order == 2: return self.composite_euler(ts, ys, index, f, h)
        ys[index+1] = self.runge_kutta(ts, ys, index, f, h)
        fs = []
        for i in range(0, order):
            fs.append(f(ts[index+1-i], ys[index+1-i]))

        coeficients = self.adams_moulton_coeficients[order]
        y = ys[index] + sum([c*f_i for c, f_i in zip(coeficients, fs)])*h
        return y

    def adams_moulton_implicit(self, order, ts, ys, index, f_expr, h):
        t, y, y1 = sympy.symbols("t y y1")

        fs = [f_expr.subs(t, ts[index+1]).subs(y, y1)]
        for i in range(0, order-1):
            fs.append(f_expr.subs(t, ts[index-i]).subs(y, ys[index-i]))

        f_side = (self.adams_moulton_coeficients[order][i]*f_i*h for i, f_i in enumerate(fs))

        return sympy.solve(sympy.Eq(ys[index] + f_side, y1), y1).pop()