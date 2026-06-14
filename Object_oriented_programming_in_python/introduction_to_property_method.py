# @property = decorator used to define a method as a property(It can be accessed like an attribute)

# Benefit: Add additional logic when read write or delete attributes
# Gives you getter, setter, deleter methods


class Rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return f"{self._width} cm"
    
    @property
    def height(self):
        return f"{self._height} cm"
    
    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            print("Width must be greater than 0")
        else:    
            self._width = new_width
   
    @height.setter
    def height(self,new_height):
        if new_height <= 0:
            print("Height can't be less than 0")
        else:
            self._height = new_height
    
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

    



rectangle1 = Rectangle(4,5)


# using @property decorator we can access the protected attribute (_attribute) set in our constructor, Protected attribute means the attribute should not be accessed outside of class. So we access that protected attribute using getter method of @property and return value form @property with or without some additional logic


# We can't change object attribute without setter method
# rectangle1.width = 3
# terminal: AttributeError: property 'height' of 'Rectangle' object has no setter

# after using setter method
rectangle1.height = 6
rectangle1.width = 2

print(rectangle1.width)
print(rectangle1.height)
# terminal: 2 cm 6cm


del rectangle1.width
del rectangle1.height

print(rectangle1.height)
# terminal: AttributeError: 'Rectangle' object has no attribute '_height'. Did you mean: 'height'?