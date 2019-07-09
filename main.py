import sys
from ode_solver import ODE_Solver

import matplotlib.pyplot as plt
import sympy


def exata(func):
    t = sympy.symbols("t")
    func = sympy.sympify(func)

    f = sympy.lambdify([t], func)

    ys = []
    ts = []
    for i in range(21):
        ys.append(f(i))
        ts.append(i)
    plt.plot(ts, ys, label="Exata")


# Get the input file
if len(sys.argv) >= 2:
    input_file_name = sys.argv[1]
    verbose = False
    should_plot = False
    output_file_name = None

    if len(sys.argv) >= 3 and (
        sys.argv[2].strip("\n") == "-v" or sys.argv[2].strip("\n") == "-p"
    ):
        verbose = "-v" in sys.argv
        should_plot = "-p" in sys.argv

else:
    print("Usage: python3 main.py [input_file_name] <-v>")
    sys.exit()

solver = ODE_Solver(input_file_name, verbose=verbose, should_plot=should_plot)

for key, val in solver.items():
    print(key, "=>", val)

# Q1
func = "16666.6667*exp(0.1*log(3)*t)"
exata(func)

solver.plotter.show("Q1")
