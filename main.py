# -*- coding: utf-8 -*-
import sympy
import matplotlib.pyplot as plt

# Definindo os símbolos t e y que serão usadas nas funções de entrada
t, y = sympy.symbols("t y")

# Implementação dos métodos numéricos:
def euler_simples(ts, ys, f, h, index):
    t = ts[index]
    y = ys[index]
    return y + f(t, y)*h

def euler_inverso(ts, ys, f, h, index):
    t = ts[index]
    y = ys[index]
    y1 = euler_simples(ts, ys, f, h, index)
    return y + f(t + h, y1)*h

def euler_composto(ts, ys, f, h, index):
    t = ts[index]
    y = ys[index]
    y1 = euler_simples(ts, ys, f, h, index)
    return y + (f(t, y) + f(t+h, y1))*h/2

def runge_kutta(ts, ys, f, h, index):
    t = ts[index]
    y = ys[index]

    k1 = f(t, y)
    k2 = f(t+(h/2), y + (h/2)*k1)
    k3 = f(t+(h/2), y + (h/2)*k2)
    k4 = f(t+h, y + h*k3)
    return y + (k1 + 2*k2 + 2*k3 + k4)*h/6

# O array dos métodos disponíveis:
metodos = [euler_simples, euler_inverso, euler_composto, runge_kutta]
nomes = ["Euler Simples", "Euler Inverso", "Euler Composto", "Runge-Kutta"]

# A função que encontra um dado tf a partir de um PVI e um método escolhido
def calcular_ate_tf(t0, y0, f, h, tf, metodo):
    y1 = y0
    t1 = t0
    
    ts = todos_ts(t0, tf, h)
    ys = [0 for _ in ts]
    ys[0] = y0
    index = 0

    while index < len(ts)-1:
        ys[index+1] = metodo(ts, ys, f, h, index)
        index += 1

    return (ts, ys)

# Funções estéticas:
def print_tabela(ts, ys):
    for (t, y) in zip(ts, ys):
        print("y(", t, ") = ", y)

def todos_ts(t0, tf, h):
    ts = [t0]
    t = t0
    
    while t <= tf:
        t += h
        ts.append(t)

    return ts


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
        
        print(nomes[metodo])
        print_tabela(ts, ys)
        print()
        plt.plot(ts, ys, label=nomes[metodo])

    plt.xlabel("t")
    plt.ylabel("y")
    plt.legend()
    plt.show()

main()
