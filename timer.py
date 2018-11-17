import time


class TimeAverager:
    def __init__(self):
        self.time = 0
        self.count = 0

    def add_time(self, t):
        self.time += t
        self.count += 1

    def average(self):
        return self.time / self.count


class FunTimeMeasurer:
    def __init__(self):
        self.averager = TimeAverager()

    def run(self, f, *largs, **dargs):
        start_time = time.time()
        result = f(*largs, **dargs)
        stop_time = time.time()
        self.averager.add_time(stop_time - start_time)
        return result

    def get_average_time(self):
        return self.averager.average()

    def get_total_time(self):
        return self.averager.time


def example(a, b, c):
    x = 0
    y = 0
    for _ in range(a):
        for _ in range(b):
            for _ in range(c):
                x += 1
    return x, y


if __name__ == "__main__":
    time_measurer = FunTimeMeasurer()
    for _ in range(10):
        x, y = time_measurer.run(example, 30, 40, 50)
        print(x, y)
    print("Time =", time_measurer.get_average_time(), "s")
    print("Time =", time_measurer.get_total_time(), "s")
