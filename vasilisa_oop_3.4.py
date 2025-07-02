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

# 3 ****************************************************
class Engine:
    def __init__(self, power: int, type: str):
        self.check_power(power)
        self.__power = power

        self.check_type(type)
        self.__type = type

        self.__current_status = 0

    def check_power(self, elem):
        if not isinstance(elem, int):
            raise TypeError('ne int')
        
        if elem < 0 or elem > 1250:
            raise ValueError('net)')
        
    def check_type(self, elem):
        if not isinstance(elem, str):
            raise TypeError('ne str')
        
        if elem not in ["бензиновый", "дизельный", "водородный"]:
            raise ValueError('таких не знаем')
    
    def ignite(self):
        if self.__current_status != 'работает':
            self.__current_status = 'работает'
        return self.__current_status
    
    def shutdown(self):
        if self.__current_status == 'работает':
            self.__current_status = 'остановлен'
        else:
            raise Warning('я хз какое тут кинуть исключение')
        
        return self.__current_status
    
    def service(self):
        self.shutdown()
        self.__current_status = 'на обслуживании'
        return self.__current_status
    
    def get_status(self):
        if self.__current_status == 'работает':
            return self.__current_status
        elif self.__current_status == 'остановлен':
            return self.__current_status
        else:
            return self.__current_status
        
    def __str__(self):
        return (f"Engine\n"
                f"power: {self.__power}\n"
                f"type: {self.__type}")
    
class Wheel:
    def __init__(self, size: int, type: str):
        self.check_size(size)
        self.__size = size

        self.check_type(type)
        self.__type = type

        self.__pressure = 0

    def check_size(self, size):
        if not isinstance(size, int):
            raise TypeError('ne int *_*')
        
        if size < 10 or size > 22:
            raise ValueError('оставьте эти колеса на свой самокат')
        
    def check_type(self, elem):
        if elem not in ["летняя", "зимняя", "всесезонная"]:
            raise ValueError('ne to')
        
    def rotate(self):
        print('имитация вращения колеса')

    def inflate(self, delta: float):
        if not isinstance(delta, float):
            raise TypeError('ne float (')
        
        if self.__pressure + delta < 0 or self.__pressure + delta > 2.5:
            raise ValueError('fatal')
        
        if self.__pressure + delta < self.__pressure:
            print('давление спущено на', delta)
            self.__pressure = self.__pressure + delta
        elif self.__pressure + delta > self.__pressure:
            print('давление надуто на', delta)
            self.__pressure = self.__pressure + delta
        else:
            print('давление осталось прежним')
            self.__pressure = self.__pressure


    def deflate(self):
        print('спуск колес в функции inflate, я не прочитала задание полностью')
    
    def __repr__(self):
        return (f"size: {self.__size}; "
                f"type: {self.__type}")
    
    # def __eq__(self, value: Wheel):
    #     return self.__size == value.__size and self.__type == value.__type and self.__pressure == value.__pressure
    
class Car:
    def __init__(self, brand: str, model: str,
                 engine: Engine,
                 wheels: list[Wheel],
                 ):
        self.check_str(brand)
        self.__brand = brand

        self.check_str(model)
        self.__model = model

        self.__engine = engine

        self.__wheels = wheels
        self.check_wheels()

    def check_str(self, elem):
        if not isinstance(elem, str):
            raise TypeError('ne str')
        
    def check_wheels(self):
        if len(self.__wheels) != 4:
            raise ValueError('net')
        
        for i in range(len(self.__wheels)):
            for j in range(i + 1, len(self.__wheels)):

                if self.__wheels[i] == self.__wheels[j]:
                    raise ValueError('одно колесо не может стоять на двух местах')
                
    def start(self):
        self.__engine.ignite()

        for wheel in self.__wheels:
            if wheel.__pressure < 1.1:
                print('давление в колесе', wheel, 'ниже нормы')
        
    def stop(self):
        self.__engine.shutdown()

    def get_specs(self):
        return (f"{self.__brand} {self.__model} - двигатель: {self.__engine}")
    
    def replace_wheel(self, idx: int, new: Wheel):
        if not isinstance(idx, int):
            raise TypeError
        
        if idx < 0 or idx > 3:
            raise ValueError("выход за границы диапазона")
        
        self.__wheels[idx] = new
        print('замена прошла')

    def __repr__(self):
        return (f"{self.__brand}\n"
                f"{self.__model}\n"
                f"{self.__engine}\n"
                f"{self.__wheels}")

w1 = Wheel(12, 'летняя')
w2 = Wheel(12, 'летняя')
w3 = Wheel(12, 'летняя')
w4 = Wheel(12, 'летняя')

eng = Engine(123, 'бензиновый')
print(eng.ignite())

car = Car('m', 'm', eng, [w1, w2, w3, w4])
print(car)
new = Wheel(15, 'летняя')
car.replace_wheel(0, new)

# 4 /////////////////////////////////////////////////
def check_str(elem):
        if not isinstance(elem, str):
            raise TypeError('ne str')
        
class Client:
    def __init__(self,client_id: str,
                 name: str,
                 email: str,
                 orders: list[Order],
                 count: int
                 ):
        check_str(client_id)
        self.__client_id = client_id

        check_str(name)
        self.__name = name

        check_str(email)
        self.__email = email
        
        self.__orders = orders

        self.__ord_count = count

    def place_order(self, order: Order):
        
        for i in range(len(self.__orders)):
            if self.__orders[i] == order:
                self.__ord_count += 1
                return

        self.__orders.append(order)

    def get_orders(self):
        list = [i for i in self.__orders]

        return list
    
    def __repr__(self):
        return (f"client: {self.__client_id}\n"
                f"name: {self.__name}\n"
                f"email: {self.__email}\n"
                f"orders: {self.__orders}")
        

class OrderItem:
    def __init__(self, item_name: str,
                 count: int):
        check_str(item_name)
        self.__item_name = item_name

        self.check_int(count)
        self.__count = count
        
    def check_int(self, elem):
        if not isinstance(elem, int):
            raise TypeError('ne int')
        
    def __repr__(self):
        return (f"name: {self.__item_name}, count: {self.__count}")
    
    def get_name(self):
        return self.__item_name
    
    def get_count(self):
        return self.__count
    
    def set_count(self):
        self.__count += 1


class Order:
    def __init__(self,
                 order_id: str,
                 client: Client,
                 items: list[OrderItem],
                 ):
        check_str(order_id)
        self.__order_id = order_id

        data = datetime.now()
        self.__date = data
        self.__client = client
        self.__items = items

    def __eq__(self, value: Order):
        return (self.__order_id == value.__order_id and 
                self.__client == value.__client and 
                self.__items == value.__items)
    
    def add_item(self, order_item: OrderItem):
        for i in range(len(self.__items)):
            if self.__items[i].get_name() == order_item.get_name():
                self.__items[i].set_count()
                return
        
        self.__items.append(order_item)

    def get_summary(self):
        return (f"ordr id: {self.__order_id} from {self.__date} for {self.__client} item: {self.__items}")
    
    def __repr__(self):
        return (f"{self.__order_id}\n"
                f"{self.__date}"
                f"{self.__items}\n"
                f"{self.__client}")