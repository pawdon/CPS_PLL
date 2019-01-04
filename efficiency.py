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
        full = get_data(filename="real_pilot_256000.csv")
        blocks = split_data(full, n)

        print(f"START: name of class: {classs.info()}; blocks: {N}")
        for b in blocks:
            carr1, carr2, carr3 = time_measurer.run(plll.process, b)

        real_time_percent = time_measurer.get_total_time() * 100 * 256000 / len(full)
        data = {"Algorithm info": classs.info(),
                "Block length": n,
                "Total time": time_measurer.get_total_time(),
                "Real time percent": real_time_percent}
        print(data)
        self.write_to_json(data)

    def efficiency_final(self):
        # clean entity
        with open(self.filename, "w"):
            pass

        pll_classes = [pll.PllNaive, pll.PllNumPy0, pll.PllNumPy1, pll.PllNumPy2, pll.PllNumPy3,
                       pll.PllNumPy4, pll.PllNumPy5, pll.PllC1, pll.PllC2, pll.PllC3]

        for pll_c in pll_classes:
            numbers = [256, 2560, 25600, 256000]
            for i in numbers:
                self.efficiency(pll_c, i)

    def write_to_json(self, data):
        with open(self.filename, 'a') as f:
            text = json.dumps(data)
            f.write(text + "\n")


if __name__ == "__main__":
    ef = Efficiency(freq=2*np.pi*19/256, alpha=0.0100, beta=2.5000e-05)
    ef.efficiency_final()
    print("done")

