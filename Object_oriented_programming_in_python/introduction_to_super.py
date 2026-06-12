# super() = function used in a child class to call methods from a parent class (superclass)

# allows you to extend the functionality of the inherited methods

# class super
# class super(type, object_or_type=None)
# Return a proxy object that delegates method calls to parent or sibling type of class. This is useful for accessing inherited methods that have been overridden in a class
# The object_or_type determines the method_resolution_order to be searched. The search starts from the class right after the type.

class Shape:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled

    def describe(self):
         print(f"The color is {self.color} is filled: {self.filled}")


class Circle(Shape):
        def __init__(self,color,filled,radius):
            super().__init__(color,filled)
            self.radius = radius
        
        # here we are overriding super() describe method with own child describe method
        def describe(self):
         # or we can extend our functionality using child describe method + super() describe method 
             print(f"This is a circle and the area of this circle is: {self.radius**2 * 3.14159}")
             super().describe()
        


class Square(Shape):
    def __init__(self,color,filled,length):
        super().__init__(color,filled)
        self.length = length
    
    # here we are overriding super() describe method with own child describe method
    def describe(self):
         # or we can extend our functionality using child describe method + super() describe method 
         print(f"This is a square and the area of this square is: {self.length * self.length}")
         super().describe()

class Triangle(Shape):
    def __init__(self,color,filled,height,width):
        super().__init__(color,filled)
        self.height = height
        self.width = width
    
    # here we are overriding super() describe method with own child describe method
    def describe(self):
         # or we can extend our functionality using child describe method + super() describe method 
         print(f"This is a triangle and the area of this triangle is: {self.height * self.width * 0.5}")
         super().describe()

circle = Circle("red",True,5)
square = Square("blue",False,6)
triangle = Triangle("green",False,7,6)

print(circle.color)
print(circle.filled)
print(circle.radius)


# we are now overriding the super() describe method 
circle.describe()
square.describe()
triangle.describe()

