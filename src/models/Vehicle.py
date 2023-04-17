class Vehicle:
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return '(type: {}, available: {}, return_t: {})'\
            .format(self.type, self.available, self.return_t)

    def use(self, upto):
        self.available = False
        self.return_t = upto

    def check_availability(self, t):
        pass
