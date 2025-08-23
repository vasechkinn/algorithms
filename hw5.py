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
        
        iterator = self.__head

        while iterator.next.next is not None:
            iterator = iterator.next

        node = iterator.next.next
        iterator.next = None
        self.__count -= 1
        return node
    
    def remove_person(self, person: PersonCard) -> None:
        """
        Удаляет карточку персоны,
        соответствующую переданной person.
        :param person: elem class PersonCard
        """

        if self.is_empty():
            return None
        
        self.__count -= 1

        if self.__head.data == person:
            self.__head = self.__head.next
            return
        
        iterator = self.__head
        while iterator.next is not None:

            if iterator.next.data == person:
                iterator.next = iterator.next.next
                return None

            iterator = iterator.next

    def clear_all(self) -> None:
        """
        Очищает список, удаляя все карточки
        """
        self.__head = None
        self.__count = 0

    