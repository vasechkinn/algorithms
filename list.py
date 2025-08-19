# ----- List (Список/Динамический массив) -----

# Fields (Атрибуты)
# - count -- фактическое кол-во элементов в массиве
# - size -- кол-во свободных ячеек памяти

# Interface (Операции)

# - add(elem) -- добавить элемент в конец списка
# - add_first(elem) -- добавить элемент в начало списка
# - insert(index, elem) -- вставить элемент на позицию

# - remove(elem) -- удалить элемент. если таких элементов много, удалить первое вхождение
# - pop(index) -- удалить элемент по индексу

# - find(elem) -- найти координату элемента. если таких элементов много, вернуть координату первого вхождения. если таких элементов нет, вернуть -1
# - count(elem) -- посчитать количество вхождений переданного элемента
# - clear() -- очистить массив (сделать каждый элемент None)
# - is_empty() -- проверка на пустоту массива


# - count - свойство, которое возвращает фактическое кол-во элементов

# ----------- Функции языка C -----------
def malloc(numbers):
    return [None] * numbers

def realloc(old_memory, old_size, new_size):
    new_memory = malloc(new_size)  # [none, none, none, ...]

    for i in range(0, old_size, 1):
        new_memory[i] = old_memory[i]

    return new_memory


# ----------- Реализация списка -----------

class List:

    __count: int
    __size: int

    def __init__(self):
        self.__count = 0
        self.__size = 5
        self.__memory = malloc(self.__size)


    def add(self, elem: any) -> None:

        if self.__count == self.__size:
            new_size = self.__size + self.__size // 2
            self.__memory = realloc(self.__memory, self.__size, new_size)
            self.__size = new_size

        self.__memory[self.__count] = elem
        self.__count += 1


    def add_first(self, elem: any):
        """
        добавляет элемент в начало списка
        :param elem: новый элемент с позицией list[0]
        """
        
        if self.__count == self.__size:
            new_size = self.__size + self.__size // 2
            self.__memory = realloc(self.__memory, self.__size, new_size)
            self.__size = new_size

        buff = self.__memory[0]

        for i in range(self.__count - 1, 0, -1):
            self.__memory[i] = self.__memory[i - 1]

        self.__memory[0] = elem
        self.__count += 1

    
    def insert(self, index: int, elem: any):
        """
        вставить элемент elem на индекс index
        :param elem: элемент
        :param index: индекс позиции, на которую должен встать новый элемент
        """
        if not isinstance(index, int):  raise TypeError('ne int')
        assert index < self.__count, f"индекс больше количества элементов массива"
        assert index >= 0, f"индекс не может быть отрицательным"

        if self.__size == self.__count:
            new_size = self.__size + self.__size // 2
            self.__memory = realloc(self.__memory, self.__size, new_size)
            self.__size = new_size

        for i in range(self.__count - 1, index, -1):
            self.__memory [i] = self.__memory[i - 1]

        self.__memory[index] = elem
        self.__count +=1

    
    def remove(self, elem: any):
        """
        удаление выбранного элемента
        если таких элементов несколько, удаляется первое вхождение
        :param elem: элемент для удаления
        """
        self.__check_elem(elem)

        counter = -1
        for i in range(self.__count):
            if elem == self.__memory[i]:
                counter = i
                break

        if counter == -1:  raise ValueError('значение не найдено')

        for i in range(counter, self.__count - 1):
            self.__memory[i] = self.__memory[i + 1]

        self.__memory[self.__count - 1] = None
        self.__count -= 1


    def pop(self, index: int):
        """
        удаляет элемент по индексу
        :param index: index
        """
        if not isinstance(index, int):  raise TypeError('ne int')
        assert index < self.__count, f"индекс больше количества элементов массива"
        assert index >= 0, f"индекс не может быть отрицательным"
        
        for i in range(index, self.__count - 1):
            self.__memory[i] = self.__memory[i + 1]

        self.__memory[self.__count - 1] = None
        self.__count -= 1


    def find(self, elem: any) -> int:
        """
        находит индекс элемента. 
        если таких элементов много, вернуть индекс первого вхождения. 
        если таких элементов нет, return -1
        :param elem: элемент для поиска
        :return: index | -1
        """

        for i in range(self.__count):
            if elem == self.__memory[i]:
                return i
            
        return -1
    

    def count_elems(self, elem: any) -> int:
        """
        находит количество вхождений элемента
        если не найдено, вернуть -1
        :param elem: элемент поиска
        :return: -1 | count
        """
        counter = 0

        for i in range(self.__count):
            if elem == self.__memory[i]:
                counter += 1

        if counter != 0:
            return counter
        
        return counter
    

    def clear(self):
        """
        очищает массив, все элементы None
        """

        for i in range(self.__count):
            self.__memory[i] = None

        self.__count = 0


    def is_empty(self) -> bool:
        """
        если список пуст, возвращает True, иначе False
        :return: True | False
        """
        if self.__count == 0:
            return True
        return False
    

    def __get_count(self):
        return self.__count
    
    count = property(__get_count)