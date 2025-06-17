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
    
    def __add__(self, other: 'Vector2D'):
        if self == other:
            return Vector2D(self.start, Point(self.end.x + other.end.x, self.end.y + other.end.y))
        print('net :3')
        
    def __sub__(self, other: 'Vector2D'):
        if self == other:
            return Vector2D(self.start, Point(self.end.x - other.end.x, self.end.y - other.end.y))
        else:
            print('net :3')
        
    def __mul__(self, delta):
        new_start = Point(self.start.x * delta, self.start.y * delta)
        new_end = Point(self.end.x * delta, self.end.y * delta)
        new_vector = Vector2D(new_start, new_end)

        return new_vector
    
    def coord(self):
        """
        координата вектора АВ(xb - xa; yb - ya)
        """
        return Point(self.end.x - self.start.x, self.end.y - self.start.y)

    def len(self):
        cor_vector = self.coord()

        return (cor_vector.x ** 2 + cor_vector.y ** 2) ** 0.5
    
    def __str__(self):
        return (f'start: {self.start}\n'
                f'end: {self.end}')
    
ps1 = Point(0, 0)
pe1 = Point(2, 2)
v1 = Vector2D(ps1, pe1)

ps2 = Point(0, 0)
pe2 = Point(5, 5)
v2 = Vector2D(ps2, pe2)

print('*: ',v1 * 2)
print('+: ', v1 + v2)
print('-: ', v1 - v2)
print('len: ', v1.len())