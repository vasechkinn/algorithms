# class Animals:
#     def __init__(self, name: str, 
#                  type_of_animal: str,
#                 age: int
#                 ):
#         self.name = name
#         self.type_of_animal = type_of_animal
#         self.age = age

#     def __str__(self):
#         return f"{self.name, self.type_of_animal, self.age}"
    
#     def sound_animal(sound):
#         return sound
    
# cat = Animals('Caticat', 'cat', 5)
# print(cat)

# sound = Animals.sound_animal(input('input sound: '))
# print(sound)
class Autor:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname 

    def __str__(self):
        return f"{self.name, self.surname}"
    

class Book:
    def __init__(self, name_book: str, autor: Autor,
                 number_of_pages: int):
        self.name_book = name_book
        self.autor = autor
        self.number_of_pages = number_of_pages

    def has_page_open(self, num_str):
        if self.number_of_pages <= num_str:
            return f'страница успешно открыта'
        else:
            return f'fatal((('
        
    def __str__(self):
        return f"{self.name_book, self.autor, self.number_of_pages}"
    
au = Autor('NO', 'Name')
print('фвтор:', au)

book1 = Book('new_book', au, 50) #спросить дмитрия про вывод автора
print(book1)