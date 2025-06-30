from __future__ import annotations
import datetime

# class Book():
#     def __init__(self, title: str,
#                  author: str,
#                  year: int):
#         self.check_str(title)
#         self.__title = title

#         self.check_str(author)
#         self.__author = author

#         self.check_year(year)
#         self.__year = year

#     def check_str(self, elem):
#         if not isinstance(elem, str):
#             raise TypeError('ne str (((((((')
        
#     def check_int(self, elem):
#         if not isinstance(elem, int):
#             raise TypeError('ne int((((((((')

#     def get_title(self):
#         return self.__title
    
#     def check_year(self, year):
#         self.check_int(year)
        
#         now_year = datetime.datetime.now().year
#         if year < 0:
#             raise ValueError('литературу до нашей эры не держим')
        
#         if year > now_year:
#             raise ValueError('net :3')

#     def __repr__(self):
#         return (f"title: {self.__title}, "
#                 f"author: {self.__author}, "
#                 f"year: {self.__year}")

#     def getInfo(self):
#         print(self)
    
#     def bookmarkPage(self, page: int):
#         self.check_int(page)
        
#         if page < 0 and page > 100000:
#             raise ValueError('net :3')
        
#         print(f"закладка установлена на странице {page}!")
    
#     def updateTitle(self, newTitle: str):
#         self.check_str(newTitle)
#         bol = self.__title
#         self.__title = newTitle

#         print(f"книгу {bol} переименовали в {self.__title}")

#     def __eq__(self, other_book: Book):
#         return self.__title == other_book.__title
    

# class Library(Book):
#     def __init__(self, name: str,
#                  address: str,
#                  ):
#         self.check_str(name)
#         self.__name = name

#         self.check_str(address)
#         self.__address = address
#         self.__books = []

#     def __repr__(self):
#         return (f"name: {self.__name}\n"
#                 f"addres: {self.__address}\n"
#                 f"books: {self.__books}")

#     def check_str(self, elem):
#         if not isinstance(elem, str):
#             raise TypeError('ne str (((((((')

#     def add_book(self, book: Book):
#         self.__books.append(book)

#     def removeBook(self, book: Book):
#         new_list = []
#         for elem in self.__books:
#             if not (elem == book):
#                 new_list.append(elem)
        
#         self.__books = new_list
#         print(f"удалена книга {book}")

#     def listBooks(self):
#         return self.__books
    
#     def findBookByTitle(self, title: str):
#         for book in self.__books:
#             if book.get_title() == title:
#                 return f"нужная книга: {book}"
#             else:
#                 raise ValueError('не найдено')

# book1 = Book('1', '1', 2000)
# book2 = Book('2', '2', 2001)

# lib = Library('mmm', 'vvv')
# lib.add_book(book1)
# lib.add_book(book2)
# print(lib)

# print(lib.findBookByTitle('1'))

# 2 *************************************************
class Student:
    def __init__(self, name: str,
                 id: str,
                 ):
        self.check_str(name)
        self.__name = name

        self.check_str(id)
        self.__id = id

        self.__grades = []

    def check_str(self, elem):
        if not isinstance(elem, str):
            raise TypeError('ne str :()')
        
    def get_profile(self):
        return (f"name: {self.__name}\nid: {self.__id}")
    
    def assign_grade(self, grade: int):
        if not isinstance(grade, int):
            raise TypeError('мы не в омэрике, оценки это цифры')
        
        if grade < 2 or grade > 5:
            raise ValueError('диапазон оценок от 2 до 5')
        
        self.__grades.append(grade)

    def get_id(self):
        return self.__id

    def __repr__(self):
        return (f"name: {self.__name}\n"
                f"id: {self.__id}\n"
                f"grades: {self.__grades}")
    
    def __eq__(self, other: Student):
        return self.__grades == other.__grades and self.__name == other.__name and self.__id == other.__id

 
class Faculty:
    def __init__(self, name: str,
                 students: list[Student],
                 ):
        
        if not isinstance(name, str):
            raise TypeError('ne str :()')
        self.__name = name

        self.__students = students

    def __repr__(self):
        return(f"name: {self.__name}\n"
               f"students: {self.__students}")

    def enroll(self, student: Student):
        self.__students.append(student)

    def graduate(self, student: Student):
        new_list = []
        for stud in self.__students:
            if stud != student:
                new_list.append(stud)
            else:
                print(f"{stud} выпустился")

        self.__students = new_list

    def list_students(self):
        return self.__students
    
    def find_student(self, id: str):
        for stud in self.__students:

            if stud.get_id() == id:
                return stud
            
        return None

    def get_name(self):
        return self.__name
    
    def __eq__(self, other: Faculty):
        return self.__name == other.__name and self.__students == other.__students
    

class University:
    def __init__(self, name: str,
                 faculties: list[Faculty],
                 ):
        if not isinstance(name, str):
            raise TypeError('ne str :()')
        self.__name = name

        self.__faculties = faculties

    def add_faculty(self, f: Faculty):
        self.__faculties.append(f)

    def remove_faculty(self, f: Faculty):
        new_list = []
        for faculty in self.__faculties:
            if faculty != f:
                new_list.append(faculty)
            
        self.__faculties = new_list
    
    def list_faculties(self):
        return self.__faculties
    
    def find_faculty(self, name: str):
        if not isinstance(name, str):
            raise TypeError('ne str :()')
        
        for faculty in self.__faculties:
            if faculty.get_name() == name:
                return faculty
            
        return None
    
    def __repr__(self):
        return (f"name: {self.__name}\n"
                f"list: {self.__faculties}")


s1 = Student('1', '1')
s2 = Student('2', '2')

list_stud = [s1, s2]
fculty = Faculty('name', list_stud)
uni = University('naame', [fculty])
print(uni.find_faculty('name'))
