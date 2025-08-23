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
            self.__data = data
            self.__next = next
            