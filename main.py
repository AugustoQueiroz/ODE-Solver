# -*- coding: utf-8 -*-
import math
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

def adams_bashforth2(ts, ys, f, h, index):
    f0 = f(ts[index], ys[index])
    f1 = f(ts[index-1], ys[index-1])
    return ys[index] + (3*f0 - f1)*h/2

def adams_bashforth3(ts, ys, f, h, index):
    f0 = f(ts[index], ys[index])
    f1 = f(ts[index-1], ys[index-1])
    f2 = f(ts[index-2], ys[index-2])
    return ys[index] + (23*f0 - 16*f1 + 5*f2)*h/12

def adams_bashforth4(ts, ys, f, h, index):
    f0 = f(ts[index], ys[index])
    f1 = f(ts[index-1], ys[index-1])
    f2 = f(ts[index-2], ys[index-2])
    f3 = f(ts[index-3], ys[index-3])
    return ys[index] + (55*f0-59*f1+37*f2-3*f3)*h/24

def adams_bashforth5(ts, ys, f, h, index):
    f0 = f(ts[index], ys[index])
    f1 = f(ts[index-1], ys[index-1])
    f2 = f(ts[index-2], ys[index-2])
    f3 = f(ts[index-3], ys[index-3])
    f4 = f(ts[index-4], ys[index-4])
    return ys[index] + (1901*f0 - 2774*f1 + 2616*f2 - 1274*f3 + 251*f4)*h/720

def adams_bashforth6(ts, ys, f, h, index):
    f0 = f(ts[index], ys[index])
    f1 = f(ts[index-1], ys[index-1])
    f2 = f(ts[index-2], ys[index-2])
    f3 = f(ts[index-3], ys[index-3])
    f4 = f(ts[index-4], ys[index-4])
    f5 = f(ts[index-5], ys[index-5])
    return ys[index] + (4277*f0-3*2641*f1+2*4991*f2-2*3649*f3+3*959*f4-5*95*f5)*h/1440

def adams_moulton2(ts, ys, f, h, index):
    return euler_composto(ts, ys, f, h, index)

def adams_moulton3(ts, ys, f, h, index):
    y1 = runge_kutta(ts, ys, f, h, index)
    f0 = f(ts[index+1], y1)
    f1 = f(ts[index], ys[index])
    f2 = f(ts[index-1], ys[index-1])
    return ys[index] + (5*f0+8*f1-f2)*h/12

def adams_moulton4(ts, ys, f, h, index):
    y1 = runge_kutta(ts, ys, f, h, index)
    f0 = f(ts[index+1], y1)
    f1 = f(ts[index], ys[index])
    f2 = f(ts[index-1], ys[index-1])
    f3 = f(ts[index-2], ys[index-2])
    return ys[index] + (9*f0+19*f1-5*f2+f3)*h/24

def adams_moulton5(ts, ys, f, h, index):
    y1 = runge_kutta(ts, ys, f, h, index)
    f0 = f(ts[index+1], y1)
    f1 = f(ts[index], ys[index])
    f2 = f(ts[index-1], ys[index-1])
    f3 = f(ts[index-2], ys[index-2])
    f4 = f(ts[index-3], ys[index-3])
    return ys[index] + (251*f0+2*323*f1-24*11*f2+2*53*f3-19*f4)*h/720

def adams_moulton6(ts, ys, f, h, index):
    y1 = runge_kutta(ts, ys, f, h, index)
    f0 = f(ts[index+1], y1)
    f1 = f(ts[index], ys[index])
    f2 = f(ts[index-1], ys[index-1])
    f3 = f(ts[index-2], ys[index-2])
    f4 = f(ts[index-3], ys[index-3])
    f5 = f(ts[index-4], ys[index-4])
    return ys[index] + (5*95*f0+1427*f1-6*133*f2+2*241*f3-173*f4+9*3*f5)*h/1440
    
# O array dos métodos disponíveis:
metodos = [euler_simples, euler_inverso, euler_composto, runge_kutta, adams_bashforth2, adams_bashforth3, adams_bashforth4, adams_bashforth5, adams_bashforth6, adams_moulton2, adams_moulton3, adams_moulton4, adams_moulton5, adams_moulton6]
nomes = ["Euler Simples", "Euler Inverso", "Euler Composto", "Runge-Kutta", "Adams-Bashforth 2", "Adams-Bashforth 3", "Adams-Bashforth 4", "Adams-Bashforth 5", "Adams-Bashforth 6", "Adams-Moulton 2", "Adams-Moulton 3", "Adams-Moulton 4", "Adams-Moulton 5", "Adams-Moulton 6"]

# A função que encontra um dado tf a partir de um PVI e um método escolhido
def calcular_ate_tf(t0, y0, f, h, tf, metodo):
    y1 = y0
    t1 = t0
    
    ts = todos_ts(t0, tf, h)
    ys = [0 for _ in ts]
    ys[0] = y0
    index = 0

    index_metodo = metodos.index(metodo)

    if (index_metodo >= 4 and index_metodo < 9) or (index_metodo >= 9):
        ys[index+1] = runge_kutta(ts, ys, f, h, index)
        index += 1
    if (index_metodo >= 5 and index_metodo < 9) or (index_metodo >= 10):
        ys[index+1] = runge_kutta(ts, ys, f, h, index)
        index += 1
    if (index_metodo >= 6 and index_metodo < 9) or (index_metodo >= 11):
        ys[index+1] = runge_kutta(ts, ys, f, h, index)
        index += 1
    if (index_metodo >= 7 and index_metodo < 9) or (index_metodo >= 12):
        ys[index+1] = runge_kutta(ts, ys, f, h, index)
        index += 1
    if (index_metodo >= 8 and index_metodo < 9) or (index_metodo >= 13):
        ys[index+1] = runge_kutta(ts, ys, f, h, index)
        index += 1

    if index_metodo >= 9:
        index -= 1

    while index < len(ts)-1:
        ys[index+1] = metodo(ts, ys, f, h, index)
        index += 1

    return (ts, ys)

# Funções estéticas:
def print_solucao(ts, ys):
    print "y(", ts[len(ts)-1], ") =", ys[len(ys)-1]

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

    plt.title("y' = " + f_text)
    for (i, metodo) in enumerate(metodos_requeridos):
        ts, ys = calcular_ate_tf(t0, y0, f, h, tf, metodos[metodo])
        
        print(nomes[metodo])
        print_solucao(ts, ys)
        print
        
        plt.plot(ts, ys, label=nomes[metodo])


    plt.title("y' = " + f_text)
    plt.xlabel("t")
    plt.ylabel("y")
    plt.legend()
    plt.show()

main()
