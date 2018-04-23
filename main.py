# -*- coding: utf-8 -*-
import sympy
import matplotlib.pyplot as plt

# Definindo os símbolos t e y que serão usadas nas funções de entrada
t, y = sympy.symbols("t y")

# Implementação dos métodos numéricos:
def euler_simples(t0, y0, f, h):
    return y0 + f(t0, y0)*h

def euler_inverso(t0, y0, f, h):
    y1 = euler_simples(t0, y0, f, h)
    return y0 + f(t0 + h, y1)*h

def euler_composto(t0, y0, f, h):
    y1 = euler_simples(t0, y0, f, h)
    return y0 + (f(t0, y0) + f(t0+h, y1))*h/2

def runge_kutta(t0, y0, f, h):
    k1 = f(t0, y0)
    k2 = f(t0+(h/2), y0 + (h/2)*k1)
    k3 = f(t0+(h/2), y0 + (h/2)*k2)
    k4 = f(t0+h, y0 + h*k3)
    return y0 + (k1 + 2*k2 + 2*k3 + k4)*h/6

# O array dos métodos disponíveis:
metodos = [euler_simples, euler_inverso, euler_composto, runge_kutta]
nomes = ["Euler Simples", "Euler Inverso", "Euler Composto", "Runge-Kutta"]

# A função que encontra um dado tf a partir de um PVI e um método escolhido
def calcular_ate_tf(t0, y0, f, h, tf, metodo):
    y1 = y0
    t1 = t0
    
    ts = [t1]
    ys = [y1]

    while t1 < tf:
        y1 = metodo(t1, y1, f, h)
        t1 += h
        ts.append(t1)
        ys.append(y1)

    return (ts, ys)

# O corpo da função principal
def main():
    line = raw_input()
    line = line.split(",")

    t0 = float(line[0])
    y0 = float(line[1])
    f_text = line[2]
    h = float(line[3])
    tf = float(line[4])
    metodos_requeridos = [int(s) for s in line[5].split(" ") if s != ""]

    # Converter a função para uma expressão de sympy, e daí pra uma função
    f_expr = sympy.sympify(f_text)
    f = sympy.lambdify([t, y], f_expr, "math")

    for metodo in metodos_requeridos:
        ts, ys = calcular_ate_tf(t0, y0, f, h, tf, metodos[metodo])
        
        plt.plot(ts, ys, label=nomes[metodo])

    plt.xlabel("t")
    plt.ylabel("y")
    plt.show()

main()
