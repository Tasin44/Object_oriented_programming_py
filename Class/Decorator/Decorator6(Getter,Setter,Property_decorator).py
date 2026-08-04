#Getter, Setter, and Deleter
#source:https://youtu.be/d2m07ENg-tA?feature=shared
#also,read this blog:https://www.geeksforgeeks.org/getter-and-setter-in-python/


#Using normal function to achieve getters and setters behaviour
#1st approach(single _protected attribute )

One-line summary

Constructor (__init__) sets initial value.
Setter controls future changes + validation.


class Geek: 
	def __init__(self, age = 0): 
		self._age = age 
	
	# getter method 
	def get_age(self): 
		return self._age 
	
	# setter method 
	def set_age(self, x): 
		self._age = x 

raj = Geek() 

# setting the age using setter 
raj.set_age(21) 

# retrieving age using getter 
print(raj.get_age()) #output 21

print(raj._age) #output 21

'''
The attribute _age is not truly private. By convention, attributes starting with a single underscore (_) are considered 
"protected" in Python, meaning they are intended for internal use but can still be accessed directly if needed.
Therefore, accessing _age directly using raj._age works without any restriction.
'''

class Person:
  def __init__(self,name="Roy"):
    self._name=name
  
  def get_name(self):
    return self._name
  
  def set_name(self,x):
    self._name=x

obj=Person()
obj.set_name("Tasin")
print(obj.get_name())

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Person:
  def __init__(self,name="kamal",age=24):
    self._nam=name 
    self._age=age 
  def get_name(self):
    return self._nam
  def get_age(self):
      return self._age
  def set_nameage(self,x,y):
    self._nam=x
    if y!=0 and y>0:#adding validation
        self._age=y

ob=Person()
ob.set_nameage("roy",-6)
print(ob.get_name())
print(ob.get_age())

====================================================================================================================================================================================================================================
#2nd approach(double __private attribute )
'''
✅ Getter and Setter Methods
These are special methods used to safely access and update private attributes.
The correct and recommended way to access or modify private attribute is through getter and setter methods.
'''

class Geek:
    def __init__(self,age=0):
        self.__age=age
    
    def get_age(self):
        return self.__age
    
    def set_age(self,x):
        self.__age=x

obj= Geek()

obj.set_age(39)

print(obj.get_age())

print(obj.__age) #AttributeError: 'Geek' object has no attribute '__age'


'''
The attribute __age is truly private because of name mangling in Python.

Attributes starting with double underscores (__) are renamed internally by Python to prevent accidental access or overriding. 
This is called name mangling.

Internally, self.__age is renamed to _Geek__age to make it harder to access directly.

Therefore, trying to access obj.__age directly raises an AttributeError, as Python does not find an attribute named __age.
'''

'''
🚫 Direct Access (Not Recommended)
You can technically access private attributes using name mangling:

		print(obj._Geek__age)

This breaks encapsulation and should be avoided unless you're debugging or working in special cases.
'''
====================================================================================================================================================================================================================================

#🚨🚨❓❓I can directly pass age 23 and then I can retrive by get_age, then why I need to use set_age() for private attribute?

class Student:
    def __init__(self,age=0):
        self.__age=age
    def get_age(self):
        return self.__age
    
obj=Student(23) #If I can already pass age in constructor, why do I need set_age()?
print(obj.get_age()) 

'''
-In your example, yes — you can pass 23 directly and retrieve it with get_age(). That works fine.
-But private attributes + setter methods are not about “can I set it?” — they are about control, validation, and safety.

2️⃣ The problem without setter ❌

Right now, nothing stops invalid data.

Someone can do:
'''
		obj = Student(-50)
		print(obj.get_age())

Output → -50 ❌ (Invalid age)

Or:

		obj = Student("Hello")
'''
Now age becomes string 😐

So your object state becomes corrupted.

3️⃣ Setter adds validation ✅

Setter lets you control how data is set.
'''

class Student:
    def __init__(self,age=0):
        self.__age=age#both is correct
        # self.set_age(age)#both is correct
    def get_age(self):
        return self.__age
    def set_age(self,x):
        if x<0:
            raise ValueError("age can't be below 0")
        self.__age=x


obj=Student()
obj.set_age(-2)
print(obj.get_age())
'''
Output: ValueError: age can't be below 0

5️⃣ Encapsulation principle (core OOP reason)

Private attribute = “Don’t touch directly”

Setter = “Use controlled door” 🚪

Think like ATM:

Balance = private

You can’t change balance directly

You must deposit/withdraw through system

Same idea.

6️⃣ Real-world analogy 🧠

Imagine hospital database (relevant to your backend projects):

Patient age field:

Without setter:

Anyone can store -5

Or "unknown"

With setter:

Only valid integer age allowed

System integrity maintained

7️⃣ When setter is NOT needed

If attribute:

Never changes after creation

Doesn’t need validation

Then constructor alone is fine ✅
'''


====================================================================================================================================================================================================================================
'''
@property decorator
@property is a built-in Python decorator.

It makes a method behave like an attribute, so you can access it without calling it as a method(without name mangling)

The @property decorator works for both protected (single _age) and private (double __age) attributes. 
This is because the @property decorator creates a layer of abstraction that allows controlled access to an attribute, 
regardless of whether the attribute is "protected" (single _) or "private" (double __).
'''

#previous code getter and setter method example with property decorator 
#✅Remember,Python expects both the getter and setter to share the same name.
class Geek:
    def __init__(self,age=0):
        self.__age=age
    
    # Getter using @property
    @property
    def fage(self):
        print("getter method called")
        return self.__age

    # Setter using @property_name.setter
    @fage.setter #@functionname.setter
    def fage(self,x):#✅getter and setter must be same name
        if(x<18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called") 
        self.__age=x

# Create an object
obj= Geek()

# Modify private attribute like a regular variable
#When you decorate a method with @property, you should access it like an attribute -fage=39, not like a function - fage(39)
obj.fage=39 #instead of obj.set_age(39),Using property setter (no parentheses!)

print(obj.fage)#instead of obj.get_age() and  __age#Using property getter

# You can still access the private variable like this (not recommended though)
print(obj.age)#instead of obj.get_age() and  __age


'''
Getter and Setter and property why used :Explanation

Getter:
    Used to access the value of a private attribute.
    Defined as a method that returns the value of the attribute.

Setter:
    Used to modify the value of a private attribute.
    Defined as a method that updates the value with some additional logic, if needed.

Property Decorator (@property):
    A Python feature to create getters and setters in a concise way.
    Allows using an attribute-like syntax (obj.attribute) to interact with private variables, while still having full control through methods.

'''
