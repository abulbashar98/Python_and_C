# Magic methods = Dunder methods (double_underscore) ex: __init__, __str__,__eq__,__lt__,__gt__,__add__,__contains__,__get__item

# They are automatically called by python's many built in operations
# They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self,title,author,num_of_pages):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages
    
    def __str__(self):
        return f"Book title: {self.title} Author: {self.author} Pages: {self.num_of_pages}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self,other):
        return self.num_of_pages < other.num_of_pages
    
    def __gt__(self,other):
        return self.num_of_pages > other.num_of_pages
    
    def __add__(self,other):
        return self.num_of_pages + other.num_of_pages
    
    def __contains__(self, item):
        return item in self.title or item in self.author
    
    def __getitem__(self, key):
        if key == "author":
            return self.author
        elif key == "title":
            return self.title
        elif key == "num_of_pages":
            return self.num_of_pages
        else:
            print(f"This key {key} was not found")

book1 = Book("The Hobbit", "J.J.R Tokien", 324)
book2 = Book("Harry Potter and the stone", "J.k Rolling", 359)
book3 = Book("The Alchemist", "Paulo Coello", 224)
book4 = Book("The Hobbit", "J.J.R Tokien", 324)

# Print object give us the value of the address
# print(book1)
# terminal: <__main__.Book object at 0x0000013F4E1A86E0>

# Now change this behavior using magic method __str__
# print(book1)
# terminal: Book title: The hobbit Author: J.J.R Tokien Pages: 324



# Comparison between two objects
# print(book1 == book2)
# terminal: False

# Even if we make the same instances like book1 and book 4
# print(book1 == book4)
# terminal: False

# To change this behavior we can use __eq__ method
# print(book1 == book4)
# terminal: True




# We can not compare objects using < operator too
# print(book1 < book2)
# terminal: TypeError: '<' not supported between instances of 'Book' and 'Book'

# We can change this behavior using __lt__ method
# print(book2 < book3)
# terminal: False 



# We can not compare objects using > operator too unless there is __lt__ method created in class
# print(book2 > book3)
# terminal: TypeError: '<' not supported between instances of 'Book' and 'Book'

# We can change this behavior using __gt__ method
# print(book2 > book3)
# terminal: False 




# We can't use + operator to add objects but we can add(+) object attributes
# print(book2 + book3)
# terminal: TypeError: unsupported operand type(s) for +: 'Book' and 'Book'
# print(book2.num_of_pages + book3.num_of_pages)
# terminal: 583

# We can change this behavior using __add__ method
# print(book2 + book3)
# terminal: 583

# print(book1.num_of_pages + book2.num_of_pages)
# terminal: 689




# We can't search for a keyword in our object
# print("Harry" in book2)
# terminal: TypeError: argument of type 'Book' is not a container or iterable

# We can change this behavior using __contains__ method
# print("Paulo" in book3)
# terminal: True
# print("James" in book3)
# terminal: False




# We can't access a key using index operator on an object(instance)
# print(book1["title"])
# terminal: TypeError: 'Book' object is not subscriptable

# We can change this behavior using __getitem__ method
print(book2["author"])
# terminal: J.K Rolling
print(book3["title"])
# terminal: The Alchemist


