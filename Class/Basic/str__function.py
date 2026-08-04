
🚨🚨__str__ must return a string, not print it. So never used print in str.🚨🚨
'''        
The __str__() function controls what should be returned when the class object is represented as a string.

The __str__ method is a special method in Python that is called by the print function 
and the str function to get the string representation of an object.

To get the default string representation of the object, you should define the __str__ method in the class.

The __str__() method returns a human-readable, or informal, string representation of an object. 
This method is called by the built-in print(), str(), and format() functions. 

If you don’t define a __str__() method for a class, then the built-in object implementation calls the __repr__() method instead.

__str__() does NOT run when the object is created.
It runs only when Python needs a string representation of the object.
'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1)

'''
Error:❌❌
C:\Users\User\Desktop\oop training\Mypractice>py my1.py
Hello my name is John
Traceback (most recent call last):
  File "C:\Users\User\Desktop\oop training\Mypractice\my1.py", line 30, in <module>
    print(p1)
    ~~~~~^^^^
TypeError: __str__ returned non-string (type NoneType)



Reason:

Your __str__ method uses print() instead of return.

What happens:

     -print(p1) calls __str__ method
     -Your method prints "Hello my name is John" - this works
    -Then __str__ returns None (because no return statement)
    - print(p1) tries to print the returned None → TypeError
'''

#Soln:

def __str__(self):
    return "Hello my name is " + self.name  # return, not print

#==============================================================================================================================================================================
Never use ',' in the return of str(example bottom) if it's multi line return statement 
but if it's a single line return statement, then we can use 

ex1: we can use coma here 
    def __str__(self):
        return f"Department: {self.name}, Classes: {[cls.name for cls in self.classes]}, Professors: {[prof.name for prof in self.professors]}"
      
ex2:we can't use coma here
    def __str__(self):
        return (f"Department: {self.name} \n"
        f"Classes: {[cls.name for cls in self.classes]}\n"
        f"Professors: {[prof.name for prof in self.professors]}\n")


#==============================================================================================================================================================================
#example-1
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1) 

#==============================================================================================================================================================================
#example-2 This approach avoids using __str__ but still allows you to get meaningful output
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 


#This approach avoids using __str__ but still allows you to get meaningful output

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def print(self):
    return f"{self.name},{self.age}"


p1 = Person("John", 36)

print(p1.print())


#==============================================================================================================================================================================
#imporant
🚨🚨__str__ must return a string, not Tuple.🚨🚨

class Department:
    def __init__(self,name):
        self.name=name#department_name
        self.classes=[] ## This is a instance level list
        self.professors=[]## This is a instance level list

    def add_class(self,class_name,class_time):#contains classname,time
        # self.classes.append(class_obj)
        #I'm storing here dictionary inside list,a dict as ONE ITEM in the list
        self.classes.append({"name":class_name,"time":class_time})

    def add_professor(self,professor_name,professor_sub):#contains professor name,age
        self.professors.append({"name":professor_name,"Subject":professor_sub})
    
    def __str__(self):
        classes_str=", ".join([f"{cls['name']} at {cls['time']}" for cls in self.classes])
        professor_str=", ".join([f"{prof['name']} of ({prof['Subject']})" for prof in self.professors])
        return (
        f"Department:{self.name}\n"
        f"Classes :{classes_str}\n"
        f"Professors:{professor_str}")

'''
if we use  ','  in the return() to separate f"Department:{self.name}\n"  f"Classes :{classes_str}\n"
it'll return a tuple
The commas make it equivalent to:
return (string1, string2, string3)

This is not valid for the __str__ method because it must return a single string, not a tuple.
When defining the __str__ method, you should never use commas to separate strings in the return statement because 
it creates a tuple instead of a single string. The __str__ method is specifically required to return a single string, not any other type of object like a tuple.



❌ Incorrect (Tuple Return):
def __str__(self):
    return (
        f"Department: {self.name}\n", 
        f"Classes: {classes_str}\n", 
        f"Professors: {professors_str}"
    )
    
The commas create a tuple:
(
    "string1",
    "string2",
    "string3"
)
This will raise a TypeError because __str__ must return a string, not a tuple.

When is it Okay to Use Commas?
Using commas is fine outside of __str__ if you intend to return a tuple or use them for other purposes. For example:

return "Hello", "World"  # Returns a tuple ('Hello', 'World')
But for __str__, always ensure the return type is a single string.
'''

'''
Question: 

why I'm putting [ ] here? I'm talking about the [ before f" and at the last ] before )?
Actually they are optional, without them code also works
-Creates complete list first, then joins
-Creates items one by one (memory efficient)
-Works fine - brackets are optional here

'''

deptobj=Department("CSE")
# deptobj.name=
deptobj.add_class("DSA",10.10)
deptobj.add_class("AI",9.55)

deptobj.add_professor("Roy","DA")
deptobj.add_professor("Ak","ML")
# deptobj.professors=["Mr.roy","Alex"]

print(deptobj)


#==============================================================================================================================================================================
#__str__() and __repr__() Examples Using a New Class
class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age
    
    def __str__(self):
        return f'The creature type is {self.name} and the age is {self.age}'

    def __repr__(self):
        return f'Ocean(\'{self.name}\', {self.age})'

c = Ocean('Jellyfish', 5)

print(str(c))
print(repr(c))


