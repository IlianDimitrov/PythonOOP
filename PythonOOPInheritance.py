#Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def welcome(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")

x.welcome()

#Create a Child Class
class Student(Person):
    pass

a = Student("Parsey","Jackson")
a.welcome()

#Add a property called graduationyear to the Student class:
class Student(Person):
    def __init__(self, firstname, lastname, graduationyear):
        Person.__init__(self, firstname, lastname)
        self.graduationyear = graduationyear
    def welcome(self):
        print("Welcome",  self.firstname, self.lastname, "to the class of", self.graduationyear)
b = Student("Ilian","Dimitrov","2017")
b.welcome()

x.welcome()
#If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
c = Student("Test","Test2","Test3")

c.welcome()
