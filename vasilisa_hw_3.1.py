# class Animal:
#     def __init__(self, name: str, 
#                  type: str,
#                 age: int
#                 ):
#         self.name = name
#         self.type = type
#         self.age = age

#     def __str__(self):
#         return f"{self.name, self.type, self.age}"
    
#     def play_sound(self, sound):
#         print(sound)
    
# cat = Animal('Caticat', 'cat', 5)
# print(cat)

# sound = cat.play_sound(input('input sound: '))

# 2 *************************************************
# class Autor:
#     def __init__(self, name: str, surname: str):
#         self.name = name
#         self.surname = surname 

#     def __str__(self):
#         return f"{self.name, self.surname}"
    

# class Book:
#     def __init__(self, name_book: str, autor: Autor,
#                  pages: int):
#         self.name_book = name_book
#         self.autor = autor
#         self.pages = pages

#     def open_page(self, num_str):
#         if self.pages <= num_str and self.pages >= 0:
#             return f'страница успешно открыта'
#         else:
#             return f'fatal((('
        
#     def __str__(self):
#         return f"{self.name_book, str(self.autor), self.pages}"
    
# au = Autor('NO', 'Name')
# print('фвтор:', au)

# book1 = Book('new_book', au, 50) #спросить дмитрия про вывод автора
# print(book1)

# 3 **************************
# class PassengerPlane:
#     def __init__(self, manufacturer: str,
#                  model: str,
#                  capacity: int,
#                  number_passengers: int,
#                  height: int,
#                  speed: int):
#         self.manufacturer = manufacturer
#         self.model = model
#         self.capacity = capacity
#         self.number_passengers = number_passengers
#         self.height = height
#         self.speed = speed

#     def __str__(self):
#         return f"{self.manufacturer, self.model, self.capacity, self.number_passengers, self.height, self.speed}"

#     def takeoff(self):
#         if self.height == 0:
#             print('самолет взлетает')
#         else:
#             print('высота больше 0, самолет уже взлетел')

#     def land(self):
#         if self.height != 0:
#             print('начало посадки')
#         else:
#             print('самолет уже приземлился')

#     def height_change(self, delta_height):
#         if self.height > 0:

#             if (delta_height + self.height) >= 0 and (delta_height + self.height) <= 12000:
#                 self.height = delta_height + self.height
#                 print('новая высота: ', self.height)
#             else:
#                 print('недопустимая высота')

#         else:
#             print('самолет еще не взлетел')

#     def speed_change(self, delta_speed): # я с вами не согл, скорость меняется с момента, когда самолет начинает подготовку визлету
#         if self.speed > 0:

#             if (delta_speed + self.speed) >= 0 and (delta_speed + self.speed)  <= 1100:
#                 self.speed = delta_speed + self.speed
#                 print('новая скорость: ', self.speed)
#             else:
#                 print('fatal speed((((')

#         else:
#             print('заведите самолет')

# plane1 = PassengerPlane('manufacturer', 'model', 15, 9, 2000, 150)
# print(plane1)

# speed = plane1.speed_change(500)
# height = plane1.height_change(80000)

# takeoff = PassengerPlane.takeoff(plane1)
# landing = PassengerPlane.land(plane1)

# 4 ******************************************
class Executor:
    def __init__(self, name: str, surname: str, year_beginning_career: int):
        self.name = name
        self.surname = surname
        self.year_beginning_career = year_beginning_career

    def __str__(self):
        return f"{self.name, self.surname, self.year_beginning_career}"