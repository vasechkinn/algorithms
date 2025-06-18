# 1 **********************************************************
# не выкупила как делать векторы без точек... класс точек сделала первым
# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y

#     def __add__(self, other: 'Point'):
#         return Point(self.x + other.x, self.y + other.y)

#     def __sub__(self, other: 'Point'):
#         return Point(self.x - other.x, self.y - other.y)
    
#     def __str__(self):
#         return f"point{self.x, self.y}"
    
# A = Point(1, 1)
# B = Point(2, 2)

# print(A + B)
# print(A - B)

# class Vector2D:
#     def __init__(self, start: Point, end: Point):
#         self.start = start
#         self.end = end

#     def __eq__(self, other: 'Vector2D'):
#         return self.start.x == other.start.x and self.start.y == other.start.y
    
#     def __add__(self, other: 'Vector2D'):
#         if self == other:
#             return Vector2D(self.start, Point(self.end.x + other.end.x, self.end.y + other.end.y))
#         print('net :3')
        
#     def __sub__(self, other: 'Vector2D'):
#         if self == other:
#             return Vector2D(self.start, Point(self.end.x - other.end.x, self.end.y - other.end.y))
#         else:
#             print('net :3')
        
#     def __mul__(self, delta):
#         new_start = Point(self.start.x * delta, self.start.y * delta)
#         new_end = Point(self.end.x * delta, self.end.y * delta)
#         new_vector = Vector2D(new_start, new_end)

#         return new_vector
    
#     def coord(self):
#         """
#         координата вектора АВ(xb - xa; yb - ya)
#         """
#         return Point(self.end.x - self.start.x, self.end.y - self.start.y)

#     def len(self):
#         cor_vector = self.coord()

#         return (cor_vector.x ** 2 + cor_vector.y ** 2) ** 0.5
    
#     def __str__(self):
#         return (f'start: {self.start}\n'
#                 f'end: {self.end}')
    
# ps1 = Point(0, 0)
# pe1 = Point(2, 2)
# v1 = Vector2D(ps1, pe1)

# ps2 = Point(0, 0)
# pe2 = Point(5, 5)
# v2 = Vector2D(ps2, pe2)

# print('*: ',v1 * 2)
# print('+: ', v1 + v2)
# print('-: ', v1 - v2)
# print('len: ', v1.len())

# 2 /***************************************************
# class Money:
#     def __init__(self, dollars: int, cents: int):
#         # self.dollars = dollars
#         # self.cents = cents

#         self.dollars = dollars + cents // 100
#         self.cents = cents % 100

#     def __add__(self, other: 'Money'):
#         new_cents = self.cents + other.cents
#         new_dollars = self.dollars + other.dollars

#         return Money(new_dollars, new_cents)
    
#     def __sub__(self, other:'Money'):
#         """
#         self - other
#         """
#         new_cents = self.cents - other.cents
#         new_dollars = self.dollars - other.dollars

#         return Money(new_dollars, new_cents)
    
#     def __str__(self):
#         return (f'dollars: {self.dollars}; '
#                 f'cents: {self.cents}')
    
# m1 = Money(1, 120)
# m2 = Money(2, 190)
# print(m1 + m2)
# print(m1 - m2)

# 3 *************************************************
# class Time:
#     def __init__(self, hours: int, minutes: int, seconds: int):
#         sum_seconds = hours * 3600 + minutes * 60 + seconds
#         self.hours = sum_seconds // 3600
#         self.minutes = (sum_seconds % 3600) // 60
#         self.seconds = sum_seconds % 60

#     def __str__(self):
#         return f'Time: {self.hours}:{self.minutes}:{self.seconds}'
    
#     def __add__(self, other: "Time"):
#         new_sum = self.len() + other.len()

#         return Time(0, 0, new_sum)
    
#     def len(self):
#         return self.hours * 3600 + self.minutes * 60 + self.seconds

# m1 = Time(0, 7, 0)
# m2 = Time(1, 8, 2)
# print('+: ', m1 + m2)
# print(m1.len())

# 5 **************************************************
# class Color:
#     def __init__(self, R: int, G: int, B: int, name: str):
#         self.R = R
#         self.G = G
#         self.B = B
#         self.name = name

#     def __str__(self):
#         return (f"red: {self.R}\n"
#                 f"green: {self.G}\n"
#                 f"blue: {self.B}\n"
#                 f"{self.name}")
    
#     def __eq__(self, other: 'Color'):
#         return self.R == other.R and self.G == other.G and self.B == other.B

# class ColoredPoint(Point):
#     def __init__(self, x, y, color: 'Color'):
#         super().__init__(x, y)
#         self.color = color

#     def __add__(self, other: 'ColoredPoint'):
#         if self.color == other.color:
#             return ColoredPoint(self.x + other.x, self.y + other.y, self.color.name)
#         else:
#             new_color = Color(0, 0, 0, 'black')
#             return ColoredPoint(self.x + other.x, self.y + other.y, new_color.name)
        
#     def __sub__(self, other: 'ColoredPoint'):
#         if self.color == other.color:
#             return ColoredPoint(self.x - other.x, self.y - other.y, self.color.name)
#         else:
#             new_color = Color(0, 0, 0, 'black')
#             return ColoredPoint(self.x - other.x, self.y - other.y, new_color.name)
    
#     def len(self):
#         print('не поняла какая у точки должна быть длина')

#     def __str__(self):
#         return (f"coloredpoint: {self.x}, {self.y}, {self.color}")
    
# color1 = Color(255, 255, 255, 'white')
# color2 = Color(255, 255, 255, 'white')

# p1 = ColoredPoint(1, 2, color1)
# p2 = ColoredPoint(2, 3, color2)

# print(p1 + p2)
# print(p1 - p2)

# 6 **************************************
import random
class Matrix:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    # def generate_matrix():
    #     matrix = [[random.randint(1, 9) for _ in range(2)] for _ in range(2)]
    #     return matrix

    def __add__(self, other: 'Matrix'):
        matrix = [[self.a + other.a, self.b + other.b], [self.c + other.c, self.d + other.d]]
        for i in matrix:
            print(*i)
    
    def __mul__(self, delta: int):
        matrix = [[self.a * delta, self.b * delta], [self.c * delta, self.d * delta]]
        for i in matrix:
            print(*i)

    def len(self):
        return 4
    
m1 = Matrix(1, 2, 3, 4)
m2 = Matrix(1, 2, 3, 4)
print('sum matrix:')
summ = m1 + m2
print('\nproizv matrix:')
proizv = m1 * 3
print('\nlen:')
print(m1.len())