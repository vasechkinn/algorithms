# 1 ////////////////////////////////////////////////////////
class PersonCard:
    def __init__(self, name: str,
                 age: int,
                 occupation: str,
                 ):
        self.__check_type(name, str)
        self.__name = name

        self.__check_type(age, int)
        self.__age = age

        self.__check_type(occupation, int)
        self.__occupation = occupation

    def __check_type(self, elem, type):
        if not isinstance(elem, type):  raise TypeError('ne tot tip')

    def __str__(self):
        return (f"name: {self.__name}"
                f"age: {self.__age}"
                f"occupation: {self.__occupation}")
    
class PersonList:

    class Node:
        def __init__(self, data: any, next: any = None):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.__count = 0
        self.__head = None

    def __check_type(self, elem, type):
        if not isinstance(elem, type):  raise TypeError('ne tot tip')

    def is_empty(self):
        return self.__count == 0

    def append_person(self, data: PersonCard) -> None:
        """
        Добавляет новую карточку персоны person в конец списка
        :paran data: elem class PersonCard
        """
        node = PersonList.Node(data = data, next = None)
        self.__count += 1

        if self.is_empty():
            self.__head = node
            return

        iterator = self.__head
        while iterator.next is not None:
            iterator = iterator.next

        iterator.next = node
        
    def add_person(self, data: PersonCard) -> None:
        """
        Добавляет новую карточку персоны person
        в начало списка
        :param data: elem class PersonCard
        """
        node = PersonList.Node(data = data, next = None)
        self.__count += 1

        if self.is_empty():
            self.__head = node
            return
        
        node.next = self.__head
        self.__head = node

    def insert_person_at(self, index: int,
                         data: PersonCard,
                         ) -> None:
        """
        Вставляет новую карточку персоны person на позицию с 
        указанным индексом. Если индекс 
        выходит за границы списка, генерируется исключение. 
        Начинаем с 1
        :param index: порядковый номер элемента, начинается с 1
        :param data: elem class PersonCard
        """
        node = PersonList.Node(data = data, next = None)
        self.__check_type(index, int)
        if index >= self.__count or index < 1:  raise IndexError('выход за границы диапазона')

        iterator = self.__head
        counter = 0

        while counter != index - 1:
            iterator = iterator.next
            counter += 1

        self.__count += 1
        node.next = iterator.next
        iterator.next = node

    def remove_first_person(self)-> Node | None:
        """
        Удаляет первую карточку в списке и возвращает её.
        :return: Node(data, next)
        """
        if self.is_empty():
            return None
        
        node = self.__head
        self.__head = self.__head.next
        self.__count -= 1
        return node
    
    def remove_last_person(self) -> Node | None:
        """
        Удаляет последнюю карточку в списке и возвращает её
        :raturn: Node(data, next)
        """

        if self.is_empty():
            return None
        
        self.__count -= 1

        
        if self.__count == 1:
            node = self.__head
            self.__head = None
            return None

        iterator = self.__head

        while iterator.next.next is not None:
            iterator = iterator.next

        node = iterator.next
        iterator.next = None
        return node
    
    def remove_person(self, person: PersonCard) -> None:
        """
        Удаляет карточку персоны,
        соответствующую переданной person.
        :param person: elem class PersonCard
        """

        if self.is_empty():
            return None

        if self.__head.data == person:
            self.__head = self.__head.next
            self.__count -= 1
            return
        
        iterator = self.__head
        while iterator.next is not None:

            if iterator.next.data == person:
                iterator.next = iterator.next.next
                self.__count -= 1
                return None

            iterator = iterator.next

    def clear_all(self) -> None:
        """
        Очищает список, удаляя все карточки
        """
        self.__head = None
        self.__count = 0

    def total_people(self) -> int:
        """
        Возвращает количество карточек в списке.
        :return: count
        """
        return self.__count
    
person = PersonCard('name', 10, '123')
linked_list = PersonList()
linked_list.add_person(person)
linked_list.append_person(person)
linked_list.clear_all()
linked_list.insert_person_at(1, person)
linked_list.remove_person(person)
linked_list.remove_last_person()
linked_list.remove_first_person()


# 2 ////////////////////////////////////////////////////////
class ProjectTask:
    def __init__(self, description: str, date: str):
        self.__check_type(description, str)
        self.__description = description

        self.__check_type(date, str)
        self.__date = date

    def __check_type(self, elem, type):
        if not isinstance(elem, type):  raise TypeError('ne tot tip')

class TaskStack:
    class Node:
        def __init__(self, data: any, prev: any = None):
            self.data = data
            self.prev = prev

    def __init__(self):
        self.__top = None
        self.__count = 0

    def is_empty(self)-> bool:
        """
        Возвращает true, если стек пуст, иначе false
        :return: true | false
        """
        return self.__count == 0

    def push(self, task: ProjectTask) -> None:
        """
        Добавляет новую задачу task на вершину стека.
        :return: none
        """
        node = TaskStack.Node(data = task, prev = None)
        self.__count += 1

        if self.is_empty():
            self.__top = node
            return
        
        node.prev = self.__top
        self.__top = node

    def pop(self) -> ProjectTask | None:
        """
        Удаляет и возвращает задачу с вершины стека. 
        Если стек пуст, возвращает None.
        """
        if self.is_empty():        
            return None
        
        node = self.__top
        self.__top = self.__top.prev
        self.__count -= 1
        return node.data
    
    def peek(self) -> ProjectTask | None:
        """
        Возвращает задачу с вершины стека без её удаления.
        Если стек пуст, возвращает None
        :return: Node.data | None
        """
        if self.is_empty():        
            return None
        
        return self.__top.data
    
    def count(self) -> int:
        """
        Возвращает количество задач в стеке.
        :return: count
        """
        return self.__count
    
task = ProjectTask('123', '123')
stack = TaskStack()
stack.is_empty()
stack.push(task)
stack.peek()
stack.pop()
stack.count()

# 3 ////////////////////////////////////////////////////////
class PrintDocument:
    def __init__(self, title: str, num_of_pages: int):
        self.__check_type(title, str)
        self.__title = title

        self.__check_type(num_of_pages, int)
        self.__num_of_pages = num_of_pages

    def __check_type(self, elem, type):
        if not isinstance(elem, type):  raise TypeError('ne tot tip')

class PrintQueue:

    class Node:
        def __init__(self, data: any, prev: any = None):
            self.data = data
            self.prev = prev

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def is_empty(self) -> bool:
        """
        Возвращает true, если очередь пуста, иначе false
        :return: true | false
        """
        return self.__count == 0
    
    def enqueue(self, document: PrintDocument) -> None:
        """
        Добавляет документ document в конец очереди
        """
        node = PrintQueue.Node(data = document, prev = None)
        self.__count += 1

        if self.is_empty():
            self.__head = node
            self.__tail = node
            return
        
        self.__tail.prev = node
        self.__tail = node

    def dequeue(self) -> PrintDocument | None:
        """
        Удаляет и возвращает первый документ из очереди.
        Если очередь пуста, возвращает None.
        :return: PrintDocument | None
        """
        if self.is_empty():
            return None
        
        document = self.__head
        self.__head = self.__head.prev
        self.__count -= 1

        if self.__head is None:
            self.__tail = None

        return document.data
    
    def peek(self) -> PrintDocument | None:
        """
        Возвращает первый документ из очереди без его удаления.
        Если очередь пуста, возвращает None.
        :return: PrintDocument | None
        """
        if self.is_empty():
            return None
        
        return self.__head.data
    
    def count(self)-> int:
        """
        Возвращает количество документов в очереди
        :return: count elems
        """
        return self.__count
    
print_doc = PrintDocument('123', 12)
queue = PrintQueue()
queue.is_empty()
queue.enqueue(print_doc)
queue.peek()
queue.dequeue()