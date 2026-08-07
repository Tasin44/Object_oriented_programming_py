#See details in docs

'''
When to use self or not? 
'''
class Student:
    def __init__(self, name):
        self.name = name   # instance attribute

    def greet(self, msg):
        print(msg, self.name)
        

obj = Student("Tasin")
obj.greet("Hello")

'''
এখানে কে কী?
name → __init__ এর argument → object এ store হয়েছে → তাই self.name
msg → greet() method এর argument → local → তাই শুধু msg

যদি ভুল করে লিখো:
print(self.msg)   # ❌ Error
কারণ msg object এ store নাই।

Super short rule:

-Object এ save করা data → self.
-Function এ আসা input → সরাসরি নাম
'''
#=======================================================================================================================================================

'''
You must use self. to access object data inside each methods of the class. 
__init__ stores data, while other methods retrieve it via self..
'''
class Person:
    def __init__(ref1,name,age):
        ref1.name=name# assigns the value to the object's attribute
        ref1.age=age 
    def myfunc(ref2):
       print("This is :"+ref2.name)
p1=Person("Tasin",25)
p1.myfunc()

'''
The self parameter is a reference 
to the current instance of the class, 
and is used to access variables that belongs to the class.

It does not have to be named self ,
you can call it whatever you like, 
but it has to be the first parameter 
of any function in the class

when u define methods within a class, you need to explicitly pass self 
as the first parameter to these methods. 
This allows those methods to access and modify attributes (variables) 
and call other methods on the same object (instance of the class).
'''
#🔸🔸🔸  Best Practice

#Use self.attribute in all methods of the class to access object data.
#__init__ sets attributes by self.attribute, while other methods use them.


#🔸🔸🔸  Why Can’t We Skip self. in any class method?

#❌ Wrong Approach (Without self.):

def __add__(self, other):
    total_age = age + other.age  # ❌ ERROR: What is `age`? Not defined!


#    age alone is just a local variable (doesn’t exist in __add__).
#    self.age tells Python: "Use the age attribute of this object (obj1)."

#✅ Correct Approach (With self.):

def __add__(self, other):
    total_age = self.age + other.age  # ✅ Correct: Uses obj1.age + obj2.age


