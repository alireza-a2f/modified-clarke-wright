class VehicleType:
    def __init__(self, name, weight_capacity, volume_capacity, max_distance):
        self.name = name
        self.weight_capacity = weight_capacity
        self.volume_capacity = volume_capacity
        self.max_distance = max_distance

    def __repr__(self):
        return f'(name: {self.name}, weight_capacity: {self.weight_capacity}, volume_capacity: {self.volume_capacity}, max_distance: {self.max_distance})'
