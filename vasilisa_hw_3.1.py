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
class Autor:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname 

    def __str__(self):
        return f"{self.name, self.surname}"
    

class Book:
    def __init__(self, name_book: str, autor: Autor,
                 pages: int):
        self.name_book = name_book
        self.autor = autor
        self.pages = pages

    def open_page(self, num_str):
        if self.pages <= num_str and self.pages >= 0:
            return f'страница успешно открыта'
        else:
            return f'fatal((('
        
    def __str__(self):
        return f"{self.name_book, str(self.autor), self.pages}"
    
au = Autor('NO', 'Name')
print('фвтор:', au)

book1 = Book('new_book', au, 50) #спросить дмитрия про вывод автора
print(book1)

# 3 **************************
class PassengerPlane:
    def __init__(self, aircraft_manufacturer: str,
                 aircraft_model: str,
                 aircraft_capacity: int,
                 number_passengers: int,
                 current_height: int,
                 current_speed: int):
        self.aircraft_manufacturer = aircraft_manufacturer
        self.aircraft_model = aircraft_model
        self.aircraft_capacity = aircraft_capacity
        self.number_passengers = number_passengers
        self.current_height = current_height
        self.current_speed = current_speed

    def __str__(self):
        return f"{self.aircraft_manufacturer, self.aircraft_model, self.aircraft_capacity, self.number_passengers, self.current_height, self.current_speed}"

    def airplane_takeoff(self):
        if self.current_height == 0:
            print('самолет взлетает')
        else:
            print('высота больше 0, самолет уже взлетел')

    def landing_the_plane(self):
        if self.current_height != 0:
            print('начало посадки')
        else:
            print('самолет уже приземлился')

    def height_change(self, height):
        if height >= 0 and height <= 12000:
            self.current_height = height
            print('новая высота: ', self.current_height)
        else:
            print('недопустимая высота')

    def speed_change(self, speed):
        if speed >= 0 and speed <= 1100:
            self.current_speed = speed
            print('новая скорость: ', self.current_speed)
        else:
            print('fatal speed((((')

plane1 = PassengerPlane('manufacturer', 'model', 15, 9, 2000, 150)
print(plane1)

speed = PassengerPlane.speed_change(plane1, 500)
height = PassengerPlane.height_change(plane1, 80000)

takeoff = PassengerPlane.airplane_takeoff(plane1)
landing = PassengerPlane.landing_the_plane(plane1)