'''
🧠 What Is Method Overriding?
-Method overriding means: This process of re-implementing a method in the child class is known as Method Overriding. 
-In method overriding: A child class redefines a method from its parent class with the same name and signature.

    
Polymorphism In inheritance, the child class inherits the methods from the parent class. 
However, it is possible to modify a method in a child class that it has inherited from the parent class. 
This is particularly useful in cases where the method inherited from 
the parent class doesn’t quite fit the child class. 
In such cases, we re-implement the method in the child class. 
This process of re-implementing a method in the child class is known as Method Overriding.  
'''
class Bird:
  def intro(self):
    print("There are many types of birds.")
    
  def flight(self):
    print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
    
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
    
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

'''
Output

There are many types of birds.
Most of the birds can fly but some cannot.
There are many types of birds.
Sparrows can fly.
There are many types of birds.
Ostriches cannot fly.
'''






'''Method overriding with hybrid inheritance'''

class School:
	def func(self):
		print("This function is in school.")

class Student1(School):#
	def func(self):
		print("This function is in student 1. ")

class Student2(School):#
	def func(self):
		print("This function is in student 2.")

class Student3(Student1, School):#Multiple inheritance 
	def func(self):
		print("This function is in student 3.")

# Driver's code
object = School()
object1 = Student1()
object2 = Student2()
object3 = Student3()
object.func()
object1.func()
object2.func()
object3.func()

'''
Output:
This function is in school.
This function is in student 1. 
This function is in student 2.
This function is in student 3.
'''




