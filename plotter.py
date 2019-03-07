#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt

class Plotter:
    def plot(self, method_name, results):
        plt.plot(list(results.keys()), list(results.values()), label=method_name)

    def show(self, y_prime):
        plt.title("y' = " + y_prime)
        plt.xlabel("t")
        plt.ylabel("y")
        plt.legend()
        plt.show()
