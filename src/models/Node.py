class Node:
    def __init__(self, name, demand):
        self.name = name
        self.demand = demand

    def __repr__(self):
        return f"(name: '{self.name}', demand: {self.demand})"
