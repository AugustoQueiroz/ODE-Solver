#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt

class Plotter:
    def print(self, method_name, results, should_print_all):
        print(method_name)

        if should_print_all:
            for t in results.keys():
                print("y(%.2f) = %.2f" % (t, results[t]))
        else:
            t = list(results.keys())[-1]
            print("y(%.2f) = %.2f" % (t, results[t]))

    def plot(self, method_name, results, should_print=True, all=False):
        if should_print:
            self.print(method_name, results, all)

        plt.plot(list(results.keys()), list(results.values()), label=method_name)

    def show(self, y_prime):
        plt.title("y' = " + y_prime)
        plt.xlabel("t")
        plt.ylabel("y")
        plt.legend()
        plt.show()
