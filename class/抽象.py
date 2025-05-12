"""
使用abstractmethod建立抽象類別
"""

from abc import abstractmethod
class Animal():  # Abstract base class
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):  # Concrete subclass
    def make_sound(self):
        print("Woof!")

my_dog = Dog()
my_dog.make_sound()  # Outputs: Woof!