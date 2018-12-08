import numpy as np
import timer
import pll
import json
from utils import *


class Efficiency:
    def __init__(self, freq, alpha, beta, filename="efficiency.json"):
        self.freq = freq
        self.latest_theta = 0
        self.alpha = alpha
        self.beta = beta
        self.filename = filename

    def efficiency(self, classs, N):
        freq = self.freq
        alpha = self.alpha
        beta = self.beta
        n = N

        time_measurer = timer.FunTimeMeasurer()
        plll = classs(freq=freq, alpha=alpha, beta=beta, N=n)
        full = get_data(filename="pilot.csv")
        blocks = split_data(full, n)
        whole_carr2 = np.array([])
        whole_carr3 = np.array([])

        print(f"START: name of class: {classs.info()}; blocks: {N}")
        for b in blocks:
            carr2, carr3 = time_measurer.run(plll.process, b)
            whole_carr2 = np.append(whole_carr2, np.array(carr2))
            whole_carr3 = np.append(whole_carr3, np.array(carr3))

        data = {"Algorithm info": classs.info(),
                "Block length": n,
                "Total time": time_measurer.get_total_time(),
                "Average time": time_measurer.get_average_time()}
        self.write_to_json(data)

    def efficiency_final(self):
        # clean entity
        with open(self.filename, "w"):
            pass

        klasy = [pll.PllNaive, pll.PllC1]

        for b in klasy:
            numbers = [100, 150]
            for i in numbers:
                self.efficiency(b, i)

    def write_to_json(self, data):
        with open(self.filename, 'a') as f:
            text = json.dumps(data)
            f.write(text + "\n")


if __name__ == "__main__":
    ef = Efficiency(0.4775, 0.0100, 2.5000e-05)
    ef.efficiency_final()
    print("done")

