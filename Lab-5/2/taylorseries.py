class TaylorSeries:
    def __init__(self, x1, x2, delta_x, E):
        self.x1 = x1
        self.x2 = x2
        self.delta_x = delta_x
        self.E = E

    def compute(self, x):
        result = 0.0
        term = 1.0
        a = -1
        n = 0
        while abs(term) > self.E:
            term = ((a ** n) * (x - 1) ** (n + 1)) / (n + 1)
            result += term
            n += 1
        return result

    def compute_range(self):
        result_dir = {}
        x = self.x1
        while x <= self.x2:
            result = self.compute(x)
            result_dir[f"{x}"] = f"{result}"
            x += self.delta_x
        return result_dir

