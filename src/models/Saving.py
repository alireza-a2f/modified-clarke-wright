class Saving:
    def __init__(self, i, j, time, quantity):
        self.i = i
        self.j = j
        self.time = time
        self.quantity = quantity
        # self.vehicle = vehicle

    def __repr__(self):
        return f"(i: '{self.i}', j: '{self.j}', time: {self.time}, vehicle: {self.quantity})"
