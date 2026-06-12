# Inheritance = Allows to inherit attributes and methods from another class
#               helps with code readability and extensibility
#               class child(parent)

class Animal:
    def __init__(self,name):
        self.name = name
        self.isAlive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")        

class Dog(Animal):
    def speak(self):
        print(f"{self.name} woofs!")
        

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows!")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} squeeks!")

# inherits name attribute from parent class animal
dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Mickey")


print(dog.name)
print(dog.isAlive)
print(cat.name)
print(cat.isAlive)
print(mouse.name)
print(mouse.isAlive)


# inherits eat and sleep method from parent class animal
dog.eat()
dog.sleep()
cat.eat()
cat.sleep()
mouse.eat()
mouse.sleep()

# having own methods and inherits an attribute name from parent class

dog.speak()
cat.speak()
mouse.speak()