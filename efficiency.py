import numpy as np
import timer
import pll
import json


def get_data(filename):
    return np.genfromtxt(filename, delimiter=',')


def split_data(data, n):
    split_nr = int(len(data) / n)
    return np.split(data, split_nr)

class effi:

    def __init__(self, freq, alpha, beta):
        self.freq = freq
        self.latest_theta = 0
        self.alpha = alpha
        self.beta = beta

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

        print("START", "name of class: ", classs, "blocks: ", N )
        for b in blocks:
            carr2, carr3 = time_measurer.run(plll.process, b)
            whole_carr2 = np.append(whole_carr2, np.array(carr2))
            whole_carr3 = np.append(whole_carr3, np.array(carr3))

        data = {}
        data['Total time'] = [time_measurer.get_total_time()]
        data['Avarage time'] = [time_measurer.get_average_time()]
        self.writeToJSON("test", data)

    def efficiency_final(self):
        klasy = [pll.PllNaive]

        for b in klasy:
            numbers = [16, 8, 5, 9]
            for i in numbers:
                self.efficiency(b, i)


    def writeToJSON(self, fileName, data):

        filePathNameWExt = fileName + '.json'
        with open(filePathNameWExt, 'w') as fp:
            json.dump(data, fp)


if __name__ == "__main__":
    ef = effi(0.4775, 0.0100, 2.5000e-05)
    ef.efficiency_final()
    print("done")

