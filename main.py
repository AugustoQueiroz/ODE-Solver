import sys
from ode_solver import ODE_Solver
import sympy

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

# t, y = sympy.symbols("t y")
# f = sympy.lambdify([t,y], sympy.sympify("16666.6667*exp(0.1*ln(3)*t)","math"))

solver.plotter.show("Q1")
