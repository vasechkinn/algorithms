from __future__ import annotations
import datetime

class Book():
    def __init__(self, title: str,
                 author: str,
                 year: int):
        self.check_str(title)
        self.__title = title

        self.check_str(author)
        self.__author = author

        self.check_year(year)
        self.__year = year

    def check_str(self, elem):
        if not isinstance(elem, str):
            raise TypeError('ne str (((((((')
        
    def check_int(self, elem):
        if not isinstance(elem, int):
            raise TypeError('ne int((((((((')

    def get_title(self):
        return self.__title
    
    def check_year(self, year):
        self.check_int(year)
        
        now_year = datetime.datetime.now().year
        if year < 0:
            raise ValueError('литературу до нашей эры не держим')
        
        if year > now_year:
            raise ValueError('net :3')

    def __repr__(self):
        return (f"title: {self.__title}, "
                f"author: {self.__author}, "
                f"year: {self.__year}")

    def getInfo(self):
        print(self)
    
    def bookmarkPage(self, page: int):
        self.check_int(page)
        
        if page < 0 and page > 100000:
            raise ValueError('net :3')
        
        print(f"закладка установлена на странице {page}!")
    
    def updateTitle(self, newTitle: str):
        self.check_str(newTitle)
        bol = self.__title
        self.__title = newTitle

        print(f"книгу {bol} переименовали в {self.__title}")

    def __eq__(self, other_book: Book):
        return self.__title == other_book.__title
    

class Library(Book):
    def __init__(self, name: str,
                 address: str,
                 ):
        self.check_str(name)
        self.__name = name

        self.check_str(address)
        self.__address = address
        self.__books = []

    def __repr__(self):
        return (f"name: {self.__name}\n"
                f"addres: {self.__address}\n"
                f"books: {self.__books}")

    def check_str(self, elem):
        if not isinstance(elem, str):
            raise TypeError('ne str (((((((')

    def add_book(self, book: Book):
        self.__books.append(book)

    def removeBook(self, book: Book):
        new_list = []
        for elem in self.__books:
            if not (elem == book):
                new_list.append(elem)
        
        self.__books = new_list
        print(f"удалена книга {book}")

    def listBooks(self):
        return self.__books
    
    def findBookByTitle(self, title: str):
        for book in self.__books:
            if book.get_title() == title:
                return f"нужная книга: {book}"
            else:
                raise ValueError('не найдено')

book1 = Book('1', '1', 2000)
book2 = Book('2', '2', 2001)

lib = Library('mmm', 'vvv')
lib.add_book(book1)
lib.add_book(book2)
print(lib)

print(lib.findBookByTitle('1'))