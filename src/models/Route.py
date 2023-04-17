class Route:
    def __init__(self):
        self.nodes = []

    def __repr__(self):
        return '(' + ', '.join(self.nodes) + ')'

    def add_node(self, node):
        self.nodes.append(node)
