# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


class Plotter:
    def print(self, problem, verbose=True):
        print(problem.method_name())

        if verbose:
            for i, t in enumerate(problem.ts):
                print("y(%f) = %f" % (t, problem.ys[i]))
        else:
            t = problem.ts[-1]
            print("y(%f) = %f" % (t, problem.ys[-1]))

        print()

    def plot(self, problem):
        plt.plot(problem.ts, problem.ys, label=problem.method_name())
        # self.show(str(problem.f_expr))

    def show(self, y_prime):
        # plt.title("y' = " + y_prime)
        plt.xlabel("t")
        plt.ylabel("y")
        plt.legend()
        # plt.xlim(xmin=18)
        # plt.ylim(xmin=)
        # fig_size = plt.rcParams["figure.figsize"]
        # fig_size[0] = 50
        # fig_size[1] = 50
        # plt.figure()
        # plt.rcParams["figure.figsize"] = fig_size
        # # Prints: [8.0, 6.0]
        # print("Current size:", fig_size)
        plt.show()
