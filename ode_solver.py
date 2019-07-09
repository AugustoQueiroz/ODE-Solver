# -*- coding: utf-8 -*-
import math
import sympy
import methods
import plotter
from functools import partial


class Problem:
    def __init__(self, problem):
        self.methods = methods.Methods()

        # Information about the method
        self.method = problem[0]
        self.auxiliary_method = problem[1]
        self.order = problem[2]

        # Information about the problem
        self.ts = self.get_ts(problem[3])
        self.h = problem[3][1]
        self.ys = problem[4] + [0] * (
            len(self.ts) - len(problem[4])
        )  # Complets the list of ys with 0s

        # Information about the function
        self.f_expr = problem[5]

    def get_ts(self, t0_h_n_steps):
        # Get the parameters from tuple
        t = t0_h_n_steps[0]
        h = t0_h_n_steps[1]
        n_steps = t0_h_n_steps[2]

        # Create the list of
        self.ts = []
        while len(self.ts) <= n_steps:
            self.ts.append(t)
            t += h

        return self.ts

    def method_function(self):
        return self.methods[self.method]["function"]

    def auxiliary_method_function(self):
        return self.methods[self.auxiliary_method]["function"]

    def method_name(self):
        name = self.methods[self.method]["name"]
        if self.method.startswith("adam") or self.method.startswith("formula"):
            name += " (Ordem = " + str(self.order) + ")"
        if self.auxiliary_method is not None:
            name += " por " + self.methods[self.auxiliary_method]["name"]
        return name

    def __str__(self):
        problem_string = "Problem:\n"
        problem_string += (
            "\tMethod: " + self.method + " of " + str(self.order) + " order" + "\n"
        )
        problem_string += (
            "\tAuxiliary Method: "
            + (self.auxiliary_method if self.auxiliary_method is not None else "None")
            + "\n"
        )
        problem_string += "\tTs: " + str(self.ts) + "\n"
        problem_string += "\tYs: " + str(self.ys) + "\n"
        problem_string += "\tf: " + str(self.f_expr) + "\n"
        return problem_string


class ODE_Solver:
    def __init__(
        self, input_file=None, should_print=True, verbose=False, should_plot=False
    ):
        # Definindo os símbolos t e y que serão usados nas funções de entrada
        self.t, self.y = sympy.symbols("t y")

        # Os métodos que podem ser resolvidos
        self.methods = methods.Methods()

        # O modulo de apresentação dos resultados
        self.plotter = plotter.Plotter()

    def logic(
        self, input_file=None, should_print=True, verbose=False, should_plot=False
    ):
        ys = {}
        if input_file is not None:
            with open(input_file) as input_data:
                for problem_definition in input_data:
                    problem = self.get_problem_from_definition(problem_definition)
                    ys[problem.method_name()] = self.solve(
                        problem,
                        should_print=should_print,
                        verbose=verbose,
                        should_plot=should_plot,
                    )
        return ys

    def get_problem_from_definition(self, definition):
        # Recebe uma string com o problema definido na formatação
        # t0, y0, f(t, y), h, tf, metodos
        # e retorna esses parametros separadamente, com a função já transformada
        # numa expressão de sympy
        definition = definition.strip("\n").split(" ")

        # Get the method wanted and the auxiliary method if needed
        method_and_auxiliary = definition[0].split("_by_")
        method = method_and_auxiliary[0]
        auxiliary_method = (
            method_and_auxiliary[1] if len(method_and_auxiliary) == 2 else None
        )

        # If method has an order, get it
        order = 1
        if method.startswith("adam") or method.startswith("formula"):
            order = int(definition[-1])

        # Get the known ys
        given_ys = (
            order if auxiliary_method is None else 1
        )  # The number of given ys: it's equals to the order of the function if there was no auxiliary given
        if (
            method.endswith("multon") or method.startswith("formula")
        ) and given_ys == order:
            given_ys -= 1  # Moulton receives one less y than it's order
        ys = []
        for value in definition[1 : 1 + given_ys]:
            ys.append(float(value))

        # Get t0, h, and tf
        t_index = 1 + given_ys
        t0 = float(definition[t_index])
        h = float(definition[t_index + 1])
        n_steps = float(definition[t_index + 2])

        # Get the function
        f_index = t_index + 3
        f_text = definition[f_index]
        f_expr = sympy.sympify(f_text)  # Função convertida como uma expressão de sympy

        return Problem([method, auxiliary_method, order, (t0, h, n_steps), ys, f_expr])

    def solve(self, problem, should_print=False, verbose=False, should_plot=False):
        index = 0

        f = sympy.lambdify(
            [self.t, self.y], problem.f_expr, "math"
        )  # Turn the function expression into an executable (python) function

        if problem.auxiliary_method is not None:
            # Use the auxiliary method to calculate the first n points
            auxiliary_method_function = problem.auxiliary_method_function()
            while index < problem.order:
                problem.ys[index + 1] = auxiliary_method_function(
                    problem.ts, problem.ys, index, f, problem.h
                )
                index += 1

        index = problem.order - 1
        method = problem.method_function()
        if problem.method.startswith("adam") or problem.method == "formula_inversa":
            method = partial(
                method, problem.order
            )  # If the method needs an order, fill it in
        while index < len(problem.ts) - 1:
            if problem.auxiliary_method is not None:
                auxiliary_method = problem.auxiliary_method_function()
                problem.ys[index + 1] = auxiliary_method(
                    problem.ts, problem.ys, index, f, problem.h
                )
            problem.ys[index + 1] = method(problem.ts, problem.ys, index, f, problem.h)
            index += 1

        if should_print:
            self.plotter.print(problem, verbose)
        if should_plot:
            self.plotter.plot(problem)

        return problem.ys


if __name__ == "__main__":
    solver = ODE_Solver("input.txt")
