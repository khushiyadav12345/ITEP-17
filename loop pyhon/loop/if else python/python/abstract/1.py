# 1. Animal Sound System

# Create parent class Animal and child classes:

# Dog
# Cat
# Cow

# Override sound() method.


class Animal:
    def sound():
        pass
    
class Dog(Animal):
    def sound(self):
            print("Bark")
            
class Cat(Animal):
    def sound(self):
            print("Meow")
            
class Cow(Animal):
    def sound(self):
            print("Amma")

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()

cow = Cow()
cow.sound()
 