class Animals:
    def __init__(self, name: str, 
                 type_of_animal: str,
                age: int
                ):
        self.name = name
        self.type_of_animal = type_of_animal
        self.age = age

    def __str__(self):
        return f"{self.name, self.type_of_animal, self.age}"
    
    def sound_animal(sound):
        return sound
    
cat = Animals('Caticat', 'cat', 5)
sound = Animals.sound_animal(input('input sound: '))
print(cat)
print(sound)