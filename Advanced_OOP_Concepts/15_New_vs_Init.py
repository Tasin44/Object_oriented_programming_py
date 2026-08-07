
"""
#================================================================================
  TOPIC 15: __new__ vs __init__ — Object Creation Lifecycle
#================================================================================

  WHAT'S THE DIFFERENCE?
  ----------------------
  - `__new__(cls)` is the FIRST step. It actually CREATES and returns a new empty object.
  - `__init__(self)` is the SECOND step. It INITIALIZES the already created object.

  Most of the time, you only need `__init__`.
  You need `__new__` when:
    1. Creating Singletons (returning the same instance every time).
    2. Subclassing immutable types like `tuple` or `str` (where `__init__` is too late).

#================================================================================
"""

# ============================================================
# EXAMPLE 1: The lifecycle order
# ============================================================

class LifecycleTest:
    def __new__(cls, *args, **kwargs):
        print("1. __new__ is called: Allocating memory and creating the object.")
        # We must return the instance using super().__new__
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print("2. __init__ is called: Initializing the object.")
        self.name = name

print("=== Lifecycle Order ===")
obj = LifecycleTest("Tasin")
print(f"Final Object: {obj.name}\n")


# ============================================================
# EXAMPLE 2: Subclassing an immutable type (str)
# ============================================================
# Strings are immutable. Once created, they cannot be changed.
# If we try to modify the string in __init__, it's too late!

class UppercaseString_BAD(str):
    def __init__(self, value):
        # ❌ This does NOT work for immutable types.
        # `self` is already created with the original value.
        pass

class UppercaseString(str):
    def __new__(cls, value):
        # ✅ This works! We modify the value BEFORE the object is fully created.
        upper_value = value.upper()
        # Create the string object using the modified value
        return super().__new__(cls, upper_value)

print("=== Subclassing Immutable Types ===")
s = UppercaseString("hello world")
print(f"UppercaseString output: {s}\n")


# ============================================================
# EXAMPLE 3: Returning a completely different object!
# ============================================================
# Since __new__ returns the object, it can technically return an object
# of a completely different class! (If it does, __init__ of the original
# class is NEVER called).

class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

class PetFactory:
    def __new__(cls, pet_type):
        if pet_type == "dog":
            return Dog()
        elif pet_type == "cat":
            return Cat()
        else:
            return super().__new__(cls)

print("=== Returning Different Objects ===")
pet1 = PetFactory("dog")
pet2 = PetFactory("cat")

print(f"pet1 type: {type(pet1)}, speaks: {pet1.speak()}")
print(f"pet2 type: {type(pet2)}, speaks: {pet2.speak()}")

"""
SUMMARY:
---------
- `__new__(cls, ...)` is a static method (even without the decorator) that creates the instance.
- `__init__(self, ...)` is an instance method that initializes the state.
- If `__new__` returns an instance of `cls`, Python automatically calls `__init__`.
- If `__new__` returns something else, `__init__` is NOT called.
"""
