import numpy as np

# a length of Look Up Table
LUT_ARRAY_LENGTH = 100000


class Lut:
    """
    Class for calculating sin and cos using LUT table
    """
    print("*****CREATING LUT STARTED*****")
    length = LUT_ARRAY_LENGTH
    x_array = np.linspace(0, 2 * np.pi, length)
    sin_array = np.sin(x_array)
    cos_array = np.cos(x_array)
    print("*****CREATING LUT FINISHED*****")

    @staticmethod
    def sin(x):
        """
        Calculate sinus
        :param x: an angle
        :return: sin(x)
        """
        norm = x % (2 * np.pi)
        ind = int(Lut.length * norm / (2 * np.pi))
        return Lut.sin_array.item(ind)

    @staticmethod
    def cos(x):
        """
        Calculate cosinus
        :param x: an angle
        :return: cos(x)
        """
        norm = x % (2 * np.pi)
        ind = int(Lut.length * norm / (2 * np.pi))
        return Lut.cos_array.item(ind)
