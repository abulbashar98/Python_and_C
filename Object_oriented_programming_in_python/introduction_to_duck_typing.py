# "Duck Typing" = Another way to achieve polymorphism besides inheritance
#                 Objects must have the minimum necessary attributes/methods 

#"If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    is_alive = True

class Dog(Animal):
    def speak(self):
        return "woof!"

class Cat(Animal):
    def speak(self):
        return "meow"

class Car:

    is_alive = False

    def speak(self):
        return ("honk")


animals = [Dog(),Cat(),Car()]

for animal in animals:
    print(animal.speak())
    print(animal.is_alive)