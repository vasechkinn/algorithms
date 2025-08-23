class PersonCard:
    def __init__(self, name: str,
                 age: int,
                 occupation: str,
                 ):
        self.__name = name
        self.__age = age
        self.__occupation = occupation

    def __str__(self):
        return (f"name: {self.__name}"
                f"age: {self.__age}"
                f"occupation: {self.__occupation}")
    
class PersonList:

    class Node:
        def __init__(self, data: any, next: any):
            self.data = data
            self.next = next
    
    def __init__(self):
        self.__count = 0
        self.__head = None

    def __check_type(self, elem, type):
        if not isinstance(elem, type):  raise TypeError('ne tot tip')

    def is_empty(self):
        return self.__count == 0

    def append_person(self, data: PersonCard):
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
        
    def add_person(self, data: PersonCard):
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
                         ):
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