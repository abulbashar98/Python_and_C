# Polymorphism = "greek word that means to have many forms or faces"
#                 poly = many
#                 morphe = form

# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1. Inheritance = An object can be treated of the same type as a parent class
# 2. "Duck Typing" = object must have necessary attributes/methods

from abc import ABC,abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        print()


class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return f"Area of the circle is: {3.14159 * self.radius ** 2} cm²"
            

class Square(Shape):
    def __init__(self,side):
        self.side = side
    
    def area(self):
        return f"Area of the square is: {self.side * self.side} cm²"

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return f"Area of the triangle is: {self.base * self.height * 0.5} cm²"

class Pizza(Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)
        self.topping = topping

    


# circle = Circle(5)
# square = Square(6)
# triangle = Triangle(4, 5)

# circle.area()
# square.area()
# triangle.area()

shapes = [Circle(5),Square(6),Triangle(4,5),Pizza("peperoni",12)]

for shape in shapes:
    print(shape.area())