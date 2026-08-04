class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

#Modify Object Properties
p1.age = 50

print(p1.age)

#Delete Object Properties
del p1.age

#print(p1.age)

#Delete Objects
del p1

#print(p1)
