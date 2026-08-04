'''
#dunder and magic method is same thing

__add__() magic method
Python __add__() method adds two objects and returns 
a new object as a resultant object in Python. 

# methods with double underscores (__method__) are special methods that have specific meanings.
# The __add__ method is designed to handle addition operations 
between two instances of the same class(here Person class)
# If you define the __add__ method in the Person class, 
it's specifically for handling addition operations involving instances of the Person class.
# You can't directly use the __add__ method of the Person class to perform addition 
operations with instances of other classes ,
if you want to do so,u will get TypeError
'''


class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __add__(self, other):
            total_age = self.age + other.age
            total_weight = self.weight + other.weight
            joint_name=self.name+other.name
            return total_age, total_weight ,joint_name

obj1 = Person("Alim", 25, 90)
obj2 = Person("karim", 30, 60)

print(obj1 + obj2)  # Output: (55, 150)



'''
Q: In __add__, why I've to do self.age,self.name, I'm doing the same thing once in __init__, then why I've to do it again?
'''
'''
Ans:
You must use self. to access object data inside each methods of the class.
__init__ stores data, while other methods retrieve it via self..

✅ Why do you use self.age, self.name, etc. again in __add__ or another method of the same class, even if you do it in __init__?

Because:

    In Python, self.name, self.age, etc. are attributes stored in the object.
    When you’re in a method like __add__, you’re working with two objects: self and other.
    You need to access each object's stored values, like this:

self.age        # from first object
other.age       # from second object


🔸🔸🔸  Didn’t I already set those in __init__?

Yes! You set them once in __init__, and they are now part of each object.
But in other methods (like __add__), you must refer to them using self or other to access those saved values.
You’re not redefining — you’re using what was set earlier.

'''
#==================================================================================================================================

'''
We can do the same thing in the return directly like:
'''

class Person:
    def __init__(self, name, age, weight):
        self.name = name   # ✅ Set once (stored in obj1/obj2)
        self.age = age     # ✅ Accessed later via self.age
        self.weight = weight

    def __add__(self, other):
        return (
            self.age + other.age,          # ✅ Uses obj1.age + obj2.age
            self.weight + other.weight,    # ✅ Uses obj1.weight + obj2.weight
            self.name + other.name        # ✅ Combines names
        )

obj1 = Person("Alim", 25, 90)
obj2 = Person("Karim", 30, 60)
print(obj1 + obj2)  # Output: (55, 150, "AlimKarim")





'''
Q: Why is the output is tuple (55, 150, "AlimKarim")?
'''

'''
🔹 Why is it a tuple?

Because of this return line in your __add__ method:

            return total_age, total_weight, joint_name

In Python, when you return multiple comma-separated values like that, they are automatically packed into a tuple.

It's equivalent to:
            return (total_age, total_weight, joint_name)


🔹 How do you know it's a tuple?
Try this:

            result = obj1 + obj2
            print(type(result))  # ➜ <class 'tuple'>

✅ Summary:
| Code                        | Result Type |
| --------------------------- | ----------- |
| `return a, b, c`            | Tuple       |
| `return (a, b, c)`          | Tuple       |
| `return [a, b, c]`          | List        |
| `return {'age': a, 'w': b}` | Dictionary  |

'''

