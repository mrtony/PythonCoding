class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
        print(f"{self.name}'s age is now {self.age} years old.")


牧羊犬 = Dog("Buddy", 3)
牧羊犬.bark()
print(f"{牧羊犬.name} is {牧羊犬.get_age()} years old.")
牧羊犬.set_age(4)
print(f"{牧羊犬.name} is now {牧羊犬.get_age()} years old.")
