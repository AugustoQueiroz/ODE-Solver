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
    for i in range(11):
        ys.append(f(i))
        ts.append(i)
    plt.plot(ts, ys, label="Exata", marker="o", markevery=25)
    return ys, ts


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

res = solver.logic(input_file_name, verbose=verbose, should_plot=should_plot)

# Q1
# func = "16666.6667*exp(0.1*log(3)*t)"

# Q2
func = "600-550*exp(-0.01*t)"

# Q3
# func = "230*pow((13/23),(t/3))+70"

# Q4
# func = "1.2-(60*t+1.2)*exp(-100*t)"

ys, ts = exata(func)

# print(ys)
errors = {}

for key, val in res.items():
    # print(key, " ", val)
    errors[key] = []
    for i, j in enumerate(ys):
        errors[key].append(round(abs(j - val[i * 10]), 2))

plt.grid()
solver.plotter.show("Q1")

plt.clf()
plt.close()

for key, val in errors.items():
    print(key, "error:", val[-1])

for key, val in res.items():
    print("result in", key, round(val[-1], 2))

for key, val in errors.items():
    # print(key, "=>", val)
    plt.plot(val, label=key, linestyle="--", marker="o")


plt.xlabel("t")
plt.ylabel("diferença com relação a exata")
plt.legend()
plt.grid()
plt.show()
