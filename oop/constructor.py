# CONSTRUCTOR : - A constructor is a special method in a class that is automatically called when an object of the class is created. It is used to initialize the attributes of the object and perform any necessary setup or configuration. In Python, the constructor method is defined using the __init__() method.

# __init__() METHOD : - All classes have a function called __init__(), which is always executed when the object is being initiated.

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

#creating class

class Student:

    college_name = "DAV College"
    name = "anonymous"        #class attr

    # #default constructors
    # def __init__(self):
    #     pass

    #parameterized constructors
    def __init__(self, name, marks):
        self.name = name                #obj attr > class attr
        self.marks = marks
        print("adding new student in database.....")

s1 = Student("Karan", 100)
print(s1.name, s1.marks)

s2 = Student("arjun", 62)
print(s2.name, s2.marks)