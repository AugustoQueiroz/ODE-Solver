#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt

class Plotter:
    def print(self, method_name, results, should_print_all):
        print()
        print(method_name)

        if should_print_all:
            for i, t in enumerate(results[0]):
                print("y(%.2f) = %.2f" % (t, results[1][i]))
        else:
            t = results[0][-1]
            print("y(%.2f) = %.2f" % (t, results[1][-1]))

    def plot(self, method_name, results, should_print=True, all=False):
        if should_print:
            self.print(method_name, results, all)

        plt.plot(list(results[0]), list(results[1]), label=method_name)

    def show(self, y_prime):
        plt.title("y' = " + y_prime)
        plt.xlabel("t")
        plt.ylabel("y")
        plt.legend()
        plt.show()
