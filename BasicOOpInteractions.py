#Creating a class , assign it to variable p1 and access the x element priting it.
class MyClass:
    x = 5

p1 = MyClass()

print(p1.x)


#Basic Class named Person using init() function to assign values for name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print("Name:" + p1.name)
print(p1.age)

#Usinge the words mysillyobject and abc instead of self:
class Person2:
    def __init__(mysillyobject, name, age):
          mysillyobject.name = name
          mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p2 = Person2("John  ",  "36")
p2.myfunc()


#deleting Object Propersties

del p2.age
p2.myfunc()
del p2
print(p2.Name)
"""Error :
5
Name:John
36
Hello my name is John
Hello my name is John
Traceback (most recent call last):
  File "BasicOOpInteractions.py", line 40, in <module>
    print(p2.Name)
NameError: name 'p2' is not defined"""
