import numpy as np
import math
import cpll
from trigonometric_lut import *


class PllState:
    def __init__(self):
        self.freq = 0
        self.latest_theta = 0
        self.alpha = 0
        self.beta = 0
        self.N = 0


class IPll:
    def __init__(self, state_class, freq, alpha, beta, N):
        self.state = state_class()
        self.state.freq = freq
        self.state.latest_theta = 0
        self.state.alpha = alpha
        self.state.beta = beta
        self.state.N = N

    @staticmethod
    def info():
        return "PLL abstract"

    def process(self, pilot):
        return None, None, None


class PllNaive(IPll):
    def __init__(self, freq, alpha, beta, N):
        super().__init__(PllState, freq, alpha, beta, N)
        self.carr1 = [1.0 for _ in range(N)]
        self.carr2 = [1.0 for _ in range(N)]
        self.carr3 = [1.0 for _ in range(N)]

    @staticmethod
    def info():
        return "PLL naive"

    def process(self, pilot):
        for n in range(self.state.N):
            self.carr1[n] = math.cos(self.state.latest_theta)
            self.carr2[n] = math.cos(2 * self.state.latest_theta)
            self.carr3[n] = math.cos(3 * self.state.latest_theta)
            perr = -pilot[n] * math.sin(self.state.latest_theta)
            self.state.latest_theta += self.state.freq + self.state.alpha * perr
            self.state.freq += self.state.beta * perr
        return self.carr1, self.carr2, self.carr3


class IPllNumPy(IPll):
    def __init__(self, state_class, freq, alpha, beta, N):
        super().__init__(state_class, freq, alpha, beta, N)
        self.carr1 = np.ones(shape=N, dtype=np.float)
        self.carr2 = np.ones(shape=N, dtype=np.float)
        self.carr3 = np.ones(shape=N, dtype=np.float)

    @staticmethod
    def info():
        return "PLL numpy abstract"


class PllNumPy0(IPllNumPy):
    def __init__(self, freq, alpha, beta, N):
        super().__init__(PllState, freq, alpha, beta, N)

    @staticmethod
    def info():
        return "PLL numpy 0"

    # carr[n] = math.cos
    def process(self, pilot):
        for n in range(self.state.N):
            self.carr1[n] = math.cos(self.state.latest_theta)
            self.carr2[n] = math.cos(2 * self.state.latest_theta)
            self.carr3[n] = math.cos(3 * self.state.latest_theta)
            perr = -pilot.item(n) * math.sin(self.state.latest_theta)
            self.state.latest_theta += self.state.freq + self.state.alpha * perr
            self.state.freq += self.state.beta * perr
        return self.carr1, self.carr2, self.carr3


class PllNumPy1(IPllNumPy):
    def __init__(self, freq, alpha, beta, N):
        super().__init__(PllState, freq, alpha, beta, N)

    @staticmethod
    def info():
        return "PLL numpy 1"

    # carr.itemset(n, math.cos
    def process(self, pilot):
        for n in range(self.state.N):
            self.carr1.itemset(n, math.cos(self.state.latest_theta))
            self.carr2.itemset(n, math.cos(2 * self.state.latest_theta))
            self.carr3.itemset(n, math.cos(3 * self.state.latest_theta))
            perr = -pilot.item(n) * math.sin(self.state.latest_theta)
            self.state.latest_theta += self.state.freq + self.state.alpha * perr
            self.state.freq += self.state.beta * perr
        return self.carr1, self.carr2, self.carr3


class PllNumPy2(IPllNumPy):
    def __init__(self, freq, alpha, beta, N):
        super().__init__(PllState, freq, alpha, beta, N)

    @staticmethod
    def info():
        return "PLL numpy 2"

    # carr.itemset(n, np.cos
    def process(self, pilot):
        for n in range(self.state.N):
            self.carr1.itemset(n, np.cos(self.state.latest_theta))
            self.carr2.itemset(n, np.cos(2 * self.state.latest_theta))
            self.carr3.itemset(n, np.cos(3 * self.state.latest_theta))
            perr = -pilot.item(n) * np.sin(self.state.latest_theta)
            self.state.latest_theta += self.state.freq + self.state.alpha * perr
            self.state.freq += self.state.beta * perr
        return self.carr1, self.carr2, self.carr3


class PllNumPy3(IPll):
    def __init__(self, freq, alpha, beta, N):
        super().__init__(PllState, freq, alpha, beta, N)
        self.theta = np.zeros(shape=N, dtype=np.float)

    @staticmethod
    def info():
        return "PLL numpy 3"

    # carr = np.cos
    def process(self, pilot):
        for n in range(self.state.N):
            self.theta.itemset(n, self.state.latest_theta)
            perr = -pilot.item(n) * np.sin(self.state.latest_theta)
            self.state.latest_theta += self.state.freq + self.state.alpha * perr
            self.state.freq += self.state.beta * perr
        carr1 = np.cos(self.theta)
        carr2 = np.cos(2 * self.theta)
        carr3 = np.cos(3 * self.theta)
        return carr1, carr2, carr3


class PllNumPy4(IPllNumPy):
    def __init__(self, freq, alpha, beta, N):
        super().__init__(PllState, freq, alpha, beta, N)

    @staticmethod
    def info():
        return "PLL numpy 4"

    # nditer
    # c[...] = math.cos
    def process(self, pilot):
        for pil, c1, c2, c3 in zip(np.nditer(pilot, op_flags=['readonly']),
                                   np.nditer(self.carr1, op_flags=['writeonly']),
                                   np.nditer(self.carr2, op_flags=['writeonly']),
                                   np.nditer(self.carr3, op_flags=['writeonly'])):
            c1[...] = math.cos(self.state.latest_theta)
            c2[...] = math.cos(2 * self.state.latest_theta)
            c3[...] = math.cos(3 * self.state.latest_theta)
            perr = -pil * math.sin(self.state.latest_theta)
            self.state.latest_theta += self.state.freq + self.state.alpha * perr
            self.state.freq += self.state.beta * perr
        return self.carr1, self.carr2, self.carr3


class PllNumPy5(IPllNumPy):
    def __init__(self, freq, alpha, beta, N):
        super().__init__(PllState, freq, alpha, beta, N)

    @staticmethod
    def info():
        return "PLL numpy 5"

    # .itemset(n, Lut.cos
    def process(self, pilot):
        for n in range(self.state.N):
            self.carr1.itemset(n, Lut.cos(self.state.latest_theta))
            self.carr2.itemset(n, Lut.cos(2 * self.state.latest_theta))
            self.carr3.itemset(n, Lut.cos(3 * self.state.latest_theta))
            perr = -pilot.item(n) * Lut.sin(self.state.latest_theta)
            self.state.latest_theta += self.state.freq + self.state.alpha * perr
            self.state.freq += self.state.beta * perr
        return self.carr1, self.carr2, self.carr3


class PllC1(IPllNumPy):
    def __init__(self, freq, alpha, beta, N):
        super().__init__(cpll.CPllState, freq, alpha, beta, N)

    @staticmethod
    def info():
        return "PLL C 1"

    # math.h cos
    def process(self, pilot):
        self.state = cpll.process1(pilot, self.carr1, self.carr2, self.carr3, self.state)
        return self.carr1, self.carr2, self.carr3


class PllC2(IPllNumPy):
    def __init__(self, freq, alpha, beta, N):
        super().__init__(cpll.CPllState, freq, alpha, beta, N)

    @staticmethod
    def info():
        return "PLL C 2"

    # math.h cos
    def process(self, pilot):
        self.state = cpll.process2(pilot, self.carr1, self.carr2, self.carr3, self.state)
        return self.carr1, self.carr2, self.carr3


class PllC3(IPllNumPy):
    def __init__(self, freq, alpha, beta, N):
        super().__init__(cpll.CPllState, freq, alpha, beta, N)

    @staticmethod
    def info():
        return "PLL C 3"

    # Lut.cos_array
    def process(self, pilot):
        self.state = cpll.process3(pilot, self.carr1, self.carr2, self.carr3, self.state, Lut.cos_array, Lut.sin_array)
        return self.carr1, self.carr2, self.carr3
