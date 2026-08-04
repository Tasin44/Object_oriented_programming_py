
"""
================================================================================
  TOPIC 14: DESCRIPTORS — __get__, __set__, __delete__
================================================================================

  WHAT IS A DESCRIPTOR?
  ---------------------
  A descriptor is an object attribute with "binding behavior". Basically, it's a
  class that defines how to get, set, or delete an attribute of another class.
  Behind the scenes, `@property`, `@classmethod`, and `@staticmethod` are all
  implemented using descriptors!

  REAL-WORLD ANALOGY:
  -------------------
  Think of a Bouncer at a club. Instead of just letting anyone in or out
  (normal variable assignment), the Bouncer (Descriptor) intercepts you when
  you try to enter (`__set__`) or leave (`__get__`) to check your ID.

================================================================================
"""

# ============================================================
# EXAMPLE 1: A Data Descriptor (Validating Data)
# ============================================================

class PositiveNumber:
    """
    This is a Descriptor class.
    It manages an attribute for another class and ensures the value is > 0.
    """
    def __set_name__(self, owner, name):
        # In Python 3.6+, __set_name__ automatically gets the variable name!
        # E.g., if used as `price = PositiveNumber()`, name will be 'price'.
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        """Called when accessing the attribute: e.g., product.price"""
        if obj is None:
            return self
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        """Called when assigning to the attribute: e.g., product.price = 50"""
        if value <= 0:
            raise ValueError(f"'{self.public_name}' must be greater than zero!")
        setattr(obj, self.private_name, value)


class Product:
    # We assign descriptors at the CLASS level!
    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price       # Triggers PositiveNumber.__set__
        self.quantity = quantity # Triggers PositiveNumber.__set__


print("=== Data Descriptors ===")
p1 = Product("Laptop", 1000, 5)
print(f"Created: {p1.name}, Price: {p1.price}, Qty: {p1.quantity}")

try:
    p1.price = -500 # This will be caught by the descriptor!
except ValueError as e:
    print(f"Error caught: {e}")

print()

# ============================================================
# EXAMPLE 2: A Non-Data Descriptor (Lazy Evaluation)
# ============================================================
import time

class LazyProperty:
    """
    A descriptor that only has __get__ (no __set__).
    It calculates a value only ONCE, then caches it directly into the object's dictionary.
    """
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
            
        print(f"  [LazyProperty] Calculating {self.name} for the first time...")
        value = self.function(obj)
        
        # Cache the value inside the object's __dict__
        # Because instance dict takes precedence over non-data descriptors,
        # next time the property is accessed, it won't call __get__!
        obj.__dict__[self.name] = value 
        return value

class DeepThought:
    def __init__(self):
        pass

    @LazyProperty
    def meaning_of_life(self):
        # Simulate an expensive computation
        time.sleep(1)
        return 42

print("=== Lazy Property Descriptor ===")
computer = DeepThought()

print("First access:")
print(f"Result: {computer.meaning_of_life}") # Takes 1 second

print("\nSecond access:")
print(f"Result: {computer.meaning_of_life}") # Instant! (fetched from __dict__)

"""
SUMMARY:
---------
- Data Descriptors implement both `__get__` and `__set__`.
- Non-Data Descriptors implement only `__get__` (like standard methods).
- Instance dictionary (`__dict__`) takes precedence over Non-Data Descriptors,
  but Data Descriptors take precedence over the instance dictionary.
- Highly reusable: You write the logic once and use it across many classes.
"""
