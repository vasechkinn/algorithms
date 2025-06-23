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