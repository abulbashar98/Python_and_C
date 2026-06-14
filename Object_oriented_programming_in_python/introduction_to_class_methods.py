# Class methods = allows operations related to the class itself
#                 Take (cls) as the first parameter, which represents the 
#                 class itself

# Instance methods = Best for operations on the instances of the class(objects)

# Static methods = Best for utility functions that do not need access to class data

# Class methods = Best for class level data or require access to class itself

class Student:
    
    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_number_of_students(cls):
        return f"Number of students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        return f"Average gpa: {cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Spongebob", 3.2)
student2 = Student("Squidward", 2.2)
student3 = Student("Sandy", 4.0)

print(Student.get_number_of_students())
print(Student.get_avg_gpa())


