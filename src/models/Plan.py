class Plan:
    weight = None
    utility_time = None

    def __init__(self, route=None, vehicle=None, start_time=None):
        self.route = route
        self.vehicle = vehicle
        self.start_time = start_time

    def __repr__(self):
        return '(start_time: {}, vehicle: {}, weight: {}, utility_time: {}, route: {})'\
            .format(self.start_time, self.vehicle, self.weight, self.utility_time, self.route)
