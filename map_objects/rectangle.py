class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def blocks(self):
        print(f"blocks {self=}")
        for x in range(self.x1 + 1, self.x2):
            for y in range(self.y1 + 1, self.y2):
                yield x, y

    def __repr__(self):
        return f"Rect({self.x1}, {self.y1}, {self.x2}, {self.y2})"
