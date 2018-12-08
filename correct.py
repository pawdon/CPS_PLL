import numpy as np
import pll
from utils import *


class Corr:

    def __init__(self, freq, alpha, beta):
        self.freq = freq
        self.latest_theta = 0
        self.alpha = alpha
        self.beta = beta

    def correct(self, classs, N):
        freq = self.freq
        alpha = self.alpha
        beta = self.beta
        n = N

        plll = classs(freq=freq, alpha=alpha, beta=beta, N=n)
        full = get_data(filename="pilot.csv")
        refer = get_data(filename="nosna.csv")
        blocks = split_data(full, n)
        whole_carr2 = np.array([])
        whole_carr3 = np.array([])

        print("START", "name of class: ", classs, "blocks: ", N)
        for b in blocks:
            carr2, carr3 = plll.process(b)
            whole_carr2 = np.append(whole_carr2, np.array(carr2))
            whole_carr3 = np.append(whole_carr3, np.array(carr3))

        save_data("result1.csv", whole_carr2)
        save_data("result2.csv", whole_carr3)

        result1 = get_data(filename="result1.csv")
        result2 = get_data(filename="result2.csv")

        if np.all(result1 == refer):
            print("Whole carr2 i refer takie same")
        else:
            print("Whole_carr2 i refer NIE takie same")

        if np.all(result2 == refer):
            print ("Whole carr3 i refer takie same")
        else:
            print ("Whole_carr3 i refer NIE takie same")

    def correct_final(self):
        klasy = [pll.PllNaive]
        numbers = [150, 16, 8, 6]

        for b in klasy:
            for i in numbers:
                self.correct(b, i)


if __name__ == "__main__":
    cor = Corr(0.4775, 0.0100, 2.5000e-05)
    cor.correct_final()
    print("done")
