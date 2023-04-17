class Demand:
    def __init__(self, w, te, tl):
        self.w = w
        self.te = te
        self.tl = tl

    def __repr__(self):
        return f'(w: {self.w}, te: {self.te}, tl: {self.tl})'

    def to_dict(self):
        return {'w': self.w, 'te': self.te, 'tl': self.tl}
