from ode_solver import ODE_Solver

solver = ODE_Solver()
solver.solve("0, 1, 2*t+3*y, 0.1, 0.5, 0 1 2")
