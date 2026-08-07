
"""
#================================================================================
  TOPIC 6: __slots__ — Memory Optimization & Attribute Restriction
#================================================================================

  WHAT IS __slots__?
  -------------------
  Normally, every Python object stores its attributes in a dictionary called
  __dict__. This is flexible but uses extra memory.

  __slots__ tells Python: "This class ONLY needs THESE specific attributes."
  Python then stores attributes in a fixed array instead of a dict.

  BENEFITS:
  ---------
  ✅ Less memory usage — no __dict__ overhead
  ✅ Faster attribute access
  ✅ Prevents accidental creation of new attributes (typo protection!)
  ✅ Useful when you create MILLIONS of instances (game objects, data science)

  WHEN TO USE:
  ------------
  - High-performance applications (game engines, simulations)
  - When you create thousands/millions of small objects
  - When you want to prevent accidental attribute creation

  WHEN NOT TO USE:
  ----------------
  - When you need flexible, dynamic attributes
  - When using multiple inheritance (can get complex)
  - General everyday code (the benefit is small for few objects)

#================================================================================
"""

import sys   # sys.getsizeof() to measure memory

# ============================================================
# EXAMPLE 1: Normal class vs __slots__ class — Memory comparison
# ============================================================

class PointNormal:
    """
    Normal Point class — uses __dict__ internally.
    Every instance has a full dictionary for attributes.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    """
    Point class with __slots__.
    __slots__ = list of attribute names this class is allowed to have.
    Python will NOT create __dict__ for instances.
    """
    __slots__ = ['x', 'y']   # ← This is all you need to add!

    def __init__(self, x, y):
        self.x = x
        self.y = y


print("=== Memory Comparison ===")
p_normal = PointNormal(3, 4)
p_slots  = PointSlots(3, 4)

# Check memory usage
print(f"Normal Point size: {sys.getsizeof(p_normal)} bytes")
print(f"Slots  Point size: {sys.getsizeof(p_slots)} bytes")

# Check if __dict__ exists
print(f"Normal has __dict__: {hasattr(p_normal, '__dict__')}")
print(f"Slots  has __dict__: {hasattr(p_slots, '__dict__')}")
print(f"Normal __dict__: {p_normal.__dict__}")
# p_slots.__dict__ would raise AttributeError!

print()

# ============================================================
# EXAMPLE 2: __slots__ PREVENTS accidental attribute creation
# ============================================================

class UserWithSlots:
    """
    __slots__ prevents adding attributes not in the list.
    This is useful to catch TYPOS at runtime!
    """
    __slots__ = ['name', 'age', 'email']

    def __init__(self, name, age, email):
        self.name  = name
        self.age   = age
        self.email = email


class UserWithoutSlots:
    """Normal class — you can add any attribute at runtime."""
    def __init__(self, name, age, email):
        self.name  = name
        self.age   = age
        self.email = email


print("=== Attribute Restriction ===")
user_slots  = UserWithSlots("Tasin", 24, "tasin@email.com")
user_normal = UserWithoutSlots("Tasin", 24, "tasin@email.com")

# Normal class: new attributes can be added freely
user_normal.phone = "01800000000"   # ✅ No error
user_normal.adres = "Dhaka"         # ✅ No error (but it's a TYPO of 'address'!)
print(f"Normal user adres (typo!): {user_normal.adres}")

# Slots class: ONLY allowed attributes
try:
    user_slots.phone = "01800000000"  # ❌ AttributeError!
except AttributeError as e:
    print(f"Slots error: {e}")

try:
    user_slots.adres = "Dhaka"        # ❌ AttributeError! Catches the typo!
except AttributeError as e:
    print(f"Slots caught typo: {e}")

# Valid attributes work fine
user_slots.name = "Mahmud"   # ✅ 'name' is in __slots__
print(f"Updated name: {user_slots.name}")

print()

# ============================================================
# EXAMPLE 3: Large-scale memory savings
# ============================================================

print("=== Bulk Memory Test (1,000,000 objects) ===")
import tracemalloc

# Test with normal class
tracemalloc.start()
normal_points = [PointNormal(i, i*2) for i in range(1_000_000)]
mem_normal = tracemalloc.get_traced_memory()[1]  # peak memory
tracemalloc.stop()

# Test with slots class
tracemalloc.start()
slots_points = [PointSlots(i, i*2) for i in range(1_000_000)]
mem_slots = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print(f"Normal class memory: {mem_normal / 1024 / 1024:.2f} MB")
print(f"Slots  class memory: {mem_slots  / 1024 / 1024:.2f} MB")
print(f"Memory saved:        {(mem_normal - mem_slots) / 1024 / 1024:.2f} MB")

# Clean up
del normal_points
del slots_points

print()

# ============================================================
# EXAMPLE 4: __slots__ with default values and methods
# ============================================================

class Car:
    """
    __slots__ works perfectly with methods and default values.
    You set defaults in __init__ as usual.
    """
    __slots__ = ['brand', 'model', 'year', 'speed', '_fuel']

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year
        self.speed = 0        # default value
        self._fuel = 100.0    # default fuel level

    def accelerate(self, amount):
        self.speed += amount
        self._fuel -= amount * 0.1   # fuel decreases
        return f"{self.brand} {self.model} speed: {self.speed} km/h"

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        return f"Braking... Speed now: {self.speed} km/h"

    def status(self):
        return (f"{self.brand} {self.model} ({self.year}) | "
                f"Speed: {self.speed} km/h | Fuel: {self._fuel:.1f}%")

    def __repr__(self):
        return f"Car(brand={self.brand!r}, model={self.model!r}, year={self.year})"


car = Car("Toyota", "GR86", 2023)
print("=== Car with __slots__ ===")
print(car)
print(car.accelerate(60))
print(car.accelerate(40))
print(car.brake(30))
print(car.status())

print()

# ============================================================
# EXAMPLE 5: __slots__ in Inheritance
# ============================================================

"""
IMPORTANT: Inheritance with __slots__ requires care.
- Parent defines its __slots__
- Child should ALSO define its own __slots__ (only NEW attributes)
- If child doesn't define __slots__, it gets __dict__ anyway!
"""

class Animal:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    """
    Dog extends Animal with additional slots.
    We only list the NEW attributes in Dog's __slots__.
    The parent's 'name' and 'age' are inherited automatically.
    """
    __slots__ = ['breed', 'is_trained']   # only Dog's NEW attributes

    def __init__(self, name, age, breed, is_trained=False):
        super().__init__(name, age)       # initialize parent slots
        self.breed      = breed
        self.is_trained = is_trained

    def speak(self):
        return f"Woof! I'm {self.name}, a {self.breed}."

    def info(self):
        status = "trained" if self.is_trained else "not trained"
        return f"{self.name} ({self.breed}, age {self.age}, {status})"


print("=== __slots__ with Inheritance ===")
dog = Dog("Rex", 3, "German Shepherd", True)
print(dog.speak())
print(dog.info())

# Check that slots work in child
try:
    dog.unknown_attr = "test"   # ❌ Should raise AttributeError
except AttributeError as e:
    print(f"Inheritance slots protection: {e}")

print()

"""
SUMMARY — __slots__:
#======================

  SYNTAX:
    class MyClass:
        __slots__ = ['attr1', 'attr2']

  EFFECTS:
    - No __dict__ → memory savings
    - Only listed attributes allowed
    - Faster attribute access

  MEMORY:
    Normal class per object  ≈ 48-56 bytes + dict overhead
    Slots class per object   ≈ 32-48 bytes (no dict)
    For 1 million objects    ≈ saves ~50-100 MB!

  GOOD USE CASES:
    - Game objects (bullets, particles, enemies)
    - Data science rows (millions of records)
    - Embedded systems (memory limited)
    - When you want strict attribute validation

  AVOID WHEN:
    - You need dynamic attributes
    - Complex multiple inheritance
    - Code that uses __dict__ directly
"""
