# Object = a bundle of related attributes(variables) and methods(functions)
# Example: phone, book, car
# You need a 'class' to create many objects
# Class = (blueprint) use to design a structure and layout of an object


from car import Car

# Attributes

car1 = Car("Mercedes", 2025, "red", False)
car2 = Car("BMW",2024,"white",True)
car3 = Car("Kia",2026,"white",False)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

# Methods

car1.drive()
car1.stop()
car2.drive()
car2.stop()
car3.drive()
car3.stop()