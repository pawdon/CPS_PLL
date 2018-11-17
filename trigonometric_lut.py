import numpy as np


class Lut:
    print("*****CREATING LUT STARTED*****")
    length = 100000
    x_array = np.linspace(0, 2 * np.pi, length)
    sin_array = np.sin(x_array)
    cos_array = np.cos(x_array)
    print("*****CREATING LUT FINISHED*****")

    @staticmethod
    def sin(x):
        norm = x % (2 * np.pi)
        ind = int(Lut.length * norm / (2 * np.pi))
        return Lut.sin_array.item(ind)

    @staticmethod
    def cos(x):
        norm = x % (2 * np.pi)
        ind = int(Lut.length * norm / (2 * np.pi))
        return Lut.cos_array.item(ind)


def test1():
    print(Lut.sin(0))
    print(Lut.sin(1))
    print(Lut.sin(2 * np.pi))
    print(Lut.sin(2 * np.pi + 1))
    print(np.max([Lut.sin(x) for x in np.linspace(0, 2 * np.pi, 10000)]))
    print(np.min([Lut.sin(x) for x in np.linspace(0, 2 * np.pi, 10000)]))


def comp_sin(x):
    return np.sin(x) - Lut.sin(x)


if __name__ == "__main__":
    test1()
