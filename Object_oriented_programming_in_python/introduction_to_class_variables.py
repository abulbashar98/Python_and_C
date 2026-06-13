# Class variables = shared among all instances of class.
#                   defined outside the constructor.
#                   allows you to share data among all objects created
#                   from class

class Student:

    class_year = 2027
    num_of_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_of_students += 1


student1 = Student("Eric", 27)
student2 = Student("Adam", 29)

# attributes
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)

# class variables
print(f"class variable from student1 object: {student1.class_year}")
print(f"class variable from student2 object: {student2.class_year}")

# Best practice for readability and understanding of a class variable is to use accessing dot operator with Class rather than object

print(f"class variable from Student Class: {student1.class_year}")

print(f"The graduating year of our class is: {Student.class_year}")

print(f"Number of students graduating from class of {Student.class_year} is: {Student.num_of_students}")

student3 = Student("James", 28)
student4 = Student("Adler", 29)

print(f"Number of students graduating from class of {Student.class_year} is {Student.num_of_students}")