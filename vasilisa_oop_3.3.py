from __future__ import annotations
# 1 ************************************************
# class Owner:
#     def __init__(self, name: str, surname: str, age: int):
#         self.__name = name
#         self.__surname = surname
#         self.__age = age
    
#     def __str__(self):
#         return f"name: {self.__name}\nsurname: {self.__surname}\nage: {self.__age}"

#     def get_age(self):
#         return f"age: {self.__age}"
    
#     def get_name(self):
#         return f"name: {self.__name}"
    
#     def get_surname(self):
#         return f"surname: {self.__surname}"

#     def set_name(self, new_name: str):
#         if isinstance(new_name, str):
#             self.__name = new_name
#         else:
#             raise TypeError("fatal(, ne str")
        
#     def set_surname(self, new_surname: str):
#         if isinstance(new_surname, str):
#             self.__surname = new_surname
#         else:
#             raise TypeError("fatal(, ne str")
        
#     def set_age(self, new_age: int):
#         if isinstance(new_age, int):

#             if new_age >= 18 and new_age < 150:
#                 self.__age = new_age
#             else:
#                 print('вы либо слишком юны, либо уже умерли :(')

#         else:
#             raise TypeError("fatal(, ne int")

# class BankAccount:
#     def __init__(self, owner: Owner, balance: float):
#         self.__owner = owner
#         self.__balance = balance

#     def get_owner(self):
#         return self.__owner
    
#     def get_balance(self):
#         return f"balance: {self.__balance}"
    
#     def set_balance(self, delta: float):
#         if isinstance(delta, float):

#             if (self.__balance + delta) >= 0:
#                 return self.__balance + delta
#             else:
#                 return 'в долг не даем и вам не советуем!'
            
#         else:
#             raise TypeError('ne  float :()')
        
#     def __str__(self):
#         return (f"owner: {self.__owner}\n"
#                 f"balance: {self.__balance}")
        
# user = Owner('lol', 'kek', 20)
# acc = BankAccount(user, 15.1)
# print(acc.get_balance())
# print(acc.set_balance(-25.0))

#2 ********************************************************
# class Rectangle:
#     def __init__(self, height: float, width: float):
#         self.__height = height
#         self.__width = width

#     def __str__(self):
#         return (f"height: {self.__height}"
#                 f"width: {self.__width}")
    
#     def get_height(self):
#         return f"height: {self.__height}"
    
#     def get_width(self):
#         return f"width: {self.__width}"
    
#     def set_height(self, delta: float):
#         if isinstance(delta, float):

#             if (self.__height + delta) > 0:
#                 return self.__height + delta
#             else: return 'математика за пятый класс...'
        
#         else:
#             raise TypeError('ne float :()')
    
#     def set_width(self, delta: float):
#         if isinstance(delta, float):

#             if (self.__width + delta) > 0:
#                 return self.__width + delta
#             else: return 'математика за пятый класс...'
        
#         else:
#             raise TypeError('ne float :()')
        
#     def area(self):
#         return f"area: {self.__height * self.__width}"

# rect = Rectangle(5.0, 4.0)
# print(rect.get_height())
# print(rect.set_height(-15.0))
# print(rect.get_width())
# print(rect.area())

# 3 **************************************************************
class People:
    def __init__(self, name: str, surname:str, age: int):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f"name: {self.__name}\nsurname: {self.__surname}\nage: {self.__age}"

    def get_age(self):
        return f"age: {self.__age}"
    
    def get_name(self):
        return f"name: {self.__name}"
    
    def get_surname(self):
        return f"surname: {self.__surname}"

    def set_name(self, new_name: str):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise TypeError("fatal(, ne str")
        
    def set_surname(self, new_surname: str):
        if isinstance(new_surname, str):
            self.__surname = new_surname
        else:
            raise TypeError("fatal(, ne str")
        
    def set_age(self, new_age: int):
        if isinstance(new_age, int):

            if new_age >= 5 and new_age < 20:
                self.__age = new_age
            else:
                print('вы либо слишком юны, либо пора задуматься...')

        else:
            raise TypeError("fatal(, ne int")


class Journal:
    def __init__(self):
        self.__math = []
        self.__russian = []
        self.__informatics = []

    def __repr__(self):
        return (f"math: {self.__math}; "
                f"russian: {self.__russian}; "
                f"informatics: {self.__informatics}; ")
    
    def append_math(self, elem: int):
        if isinstance(elem, int):

            if elem >= 2 and elem <= 5:
                self.__math.append(elem)
            else:
                raise ValueError('net :()')
            
        else:
            raise TypeError('ne int :3')
    
    def append_rus(self, elem: int):
        if isinstance(elem, int):

            if elem >= 2 and elem <= 5:
                self.__russian.append(elem)
            else:
                raise ValueError('net :()')
            
        else:
            raise TypeError('ne int :3')
        
    def append_inf(self, elem: int):
        if isinstance(elem, int):

            if elem >= 2 and elem <= 5:
                self.__informatics.append(elem)
            else:
                raise ValueError('net :()')
            
        else:
            raise TypeError('ne int :3')
    
    def mean_math(self):
        if len(self.__math) == 0:
            return 'пока нет оценок'
        
        count = 0
        for i in range(len(self.__math)):
            count += self.__math[i]

        return round(count / len(self.__math), 2)
    
    def mean_russian(self):
        if len(self.__russian) == 0:
            return 'пока нет оценок'
        
        count = 0
        for i in range(len(self.__russian)):
            count += self.__russian[i]

        return round(count / len(self.__russian), 2)
    
    def mean_informatics(self):
        if len(self.__informatics) == 0:
            return 'пока нет оценок'
        
        count = 0
        for i in range(len(self.__informatics)):
            count += self.__informatics[i]

        return round(count / len(self.__informatics), 2)


class Student:
    def __init__(self, people: People, class_stud: str, journal: Journal):
        self.__people = people
        self.__class_stud = class_stud
        self.__journal = journal

    def __repr__(self):
        return (f"student: \n{self.__people}\n"
                f"class: {self.__class_stud}\n"
                f"journal: \n{self.__journal}")


p1 = People('lol', 'kek', 12)
p1.set_age(15)
m = [2, 4, 5]
r = [2, 2, 2]
inf = [2, 4, 5]
jour = Journal()
jour.append_inf(4)
print('mean math: ', jour.mean_math())

stud = Student(p1, '2a', jour)
print(stud)