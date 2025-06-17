# 1 **********************************************************
# не выкупила как делать векторы без точек... класс точек сделала первым
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other: 'Point'):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point'):
        return Point(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"point{self.x, self.y}"
    
A = Point(1, 1)
B = Point(2, 2)

print(A + B)
print(A - B)

class Vector2D:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __eq__(self, other: 'Vector2D'):
        return self.start.x == other.start.x and self.start.y == other.start.y
    