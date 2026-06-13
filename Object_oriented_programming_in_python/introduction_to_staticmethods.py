# "Static methods" = A method belongs to a class rather than any objet made from that class(instance). Usually used for general utility functions

# Instance method = best for operations on instances of the class (object)
# Static method = best for utility functions that do not need any class data

class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    
    def get_info(self):
        return f"Name: {self.name}, Position: {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_positions
        

# To use a static method, we don't need to create an instance or object from that class. We can access the static method using the class only

print(Employee.is_valid_position("Manager"))

# For instance method we have to create an instance(object) of that class and pass in the required arguments

employee1 = Employee("Jack", "Manager")
employee2 = Employee("Ryan", "Cook")
employee3 = Employee("Adam", "Janitor")

employee_list = [employee1,employee2,employee3]

for employee in employee_list:
    print(employee.get_info())

