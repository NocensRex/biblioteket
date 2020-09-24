class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


p = Point(3, 4)

print(p)
