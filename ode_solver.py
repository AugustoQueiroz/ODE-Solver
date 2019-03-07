# -*- coding: utf-8 -*-
import math
import sympy
import methods 
import plotter

class Problem:
    def __init__(self, problem):
        self.t0 = problem[0]
        self.y0 = problem[1]
        self.f_text = problem[2]
        self.f_expr = problem[3]
        self.h = problem[4]
        self.tf = problem[5]

class ODE_Solver:
    def __init__(self):
        # Definindo os símbolos t e y que serão usados nas funções de entrada
        self.t, self.y = sympy.symbols("t y")

        # Os métodos que podem ser resolvidos
        self.methods = methods.Methods()

        self.plotter = plotter.Plotter()

    def solve(self, problem_definition):
        # Método que resolve um problema passado como string
        problem, required_methods = self.get_problem_from_definition(problem_definition)
        
        for method_index in required_methods:
            self.plotter.plot(self.methods[method_index]["name"], self.solve_with_method(problem, method_index))

        self.plotter.show(problem.f_text)

    def create_ys(self, t0, tf, h):
        # Função auxiliar que retorna uma lista com todos os passos de
        # t0 até tf com tamanho de passo h
        ys = {}
        t = t0

        while t <= tf:
            ys[t] = 0
            t += h

        return ys

    def get_problem_from_definition(self, definition):
        # Recebe uma string com o problema definido na formatação
        # t0, y0, f(t, y), h, tf, metodos
        # e retorna esses parametros separadamente, com a função já transformada
        # numa expressão de sympy
        definition = definition.split(",")

        t0 = float(definition[0])
        y0 = float(definition[1])
        f_text = definition[2]
        h = float(definition[3])
        tf = float(definition[4])
        required_methods = [int(s) for s in definition[5].split(" ") if s != ""]

        # Convertendo a função para uma expressão de sympy que depois pode ser usada para criar uma função
        f_expr = sympy.sympify(f_text)

        return (Problem([t0, y0, f_text, f_expr, h, tf]), required_methods)

    def solve_with_method(self, problem, method_index):
        # Função que recebe os parâmetros e mais um método
        # então calcula o PVI usando o método de entrada
        # Retorna tf e seu valor calculado, yf
        metodo = self.methods[method_index]["function"]
        f = sympy.lambdify([self.t, self.y], problem.f_expr, "math") # Transformar a expressão da função em uma função executável

        y1 = problem.y0
        t1 = problem.t0

        # Criação de uma lista com todos os ts e seus respectivos ys
        # TODO: Talvez trocar duas listas por um dicionário y[ts] = ys
        ys = self.create_ys(problem.t0, problem.tf, problem.h)
        ys[problem.t0] = problem.y0
        t = problem.t0

        # Inicialização da lista de resultados baseado nas necessidades do
        # método escolhido

        # Para cada t calcular o próximo ponto
        while t <= problem.tf:
            if  method_index <= 13: ys[t+problem.h] = metodo(t, ys, f, problem.h)
            else: ys[t+problem.h] = metodo(t, ys, f_expr, problem.h)

            t += problem.h

        return ys

if "__name__" == "__main__":
    solver = ODE_Solver()
    solver.solve("0, 1, cos(t)*y, 0.1, 20, 0 1")