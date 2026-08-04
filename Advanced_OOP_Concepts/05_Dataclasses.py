
"""
================================================================================
  TOPIC 5: DATACLASSES — @dataclass Decorator
================================================================================

  WHAT ARE DATACLASSES?
  ----------------------
  Dataclasses (introduced in Python 3.7) automatically generate common
  dunder methods like __init__, __repr__, __eq__ for you.

  WITHOUT dataclass, you write a LOT of repetitive boilerplate:
    class Person:
        def __init__(self, name, age, city):
            self.name = name
            self.age  = age
            self.city = city
        def __repr__(self):
            return f"Person(name={self.name!r}, age={self.age!r})"
        def __eq__(self, other):
            return self.name == other.name and self.age == other.age

  WITH @dataclass, you just write the fields — Python does the rest!

  WHAT @dataclass AUTO-GENERATES:
  --------------------------------
  ✅ __init__   → constructor with all fields
  ✅ __repr__   → nice string representation
  ✅ __eq__     → equality comparison (field by field)

  OPTIONAL (with parameters):
  ✅ __lt__, __gt__ etc.  → when order=True
  ✅ make immutable       → when frozen=True
  ✅ __hash__             → when frozen=True or unsafe_hash=True

================================================================================
"""

from dataclasses import dataclass, field, fields, asdict, astuple
from typing import List

# ============================================================
# EXAMPLE 1: Basic @dataclass
# ============================================================

# ✅ Without @dataclass — lots of repetitive code
class PersonOld:
    def __init__(self, name, age, city):
        self.name = name
        self.age  = age
        self.city = city

    def __repr__(self):
        return f"PersonOld(name={self.name!r}, age={self.age!r}, city={self.city!r})"

    def __eq__(self, other):
        return (self.name == other.name and
                self.age  == other.age  and
                self.city == other.city)


# ✅ WITH @dataclass — much cleaner! Same power, less code.
@dataclass
class Person:
    """
    @dataclass auto-generates:
      - __init__(self, name, age, city)
      - __repr__()
      - __eq__()
    You just declare the FIELDS with type hints.
    """
    name: str       # field with type hint
    age: int        # field with type hint
    city: str       # field with type hint


print("=== Basic @dataclass ===")
p1 = Person("Tasin", 24, "Dhaka")
p2 = Person("Mahmud", 23, "Chittagong")
p3 = Person("Tasin", 24, "Dhaka")   # same as p1

print(p1)              # auto __repr__: Person(name='Tasin', age=24, city='Dhaka')
print(p1 == p3)        # True  — auto __eq__ compares all fields
print(p1 == p2)        # False

print()

# ============================================================
# EXAMPLE 2: Default Values in Dataclasses
# ============================================================

@dataclass
class Product:
    """
    Fields can have default values.
    Fields WITHOUT defaults must come BEFORE fields WITH defaults.
    (Same rule as regular function arguments)
    """
    name: str
    price: float
    category: str = "General"    # default value
    in_stock: bool = True        # default value
    rating: float = 0.0          # default value


print("=== Default Values ===")
# All fields provided
laptop = Product("Laptop", 75000.0, "Electronics", True, 4.5)
print(laptop)

# Using defaults for optional fields
shirt = Product("T-Shirt", 500.0)
print(shirt)   # category="General", in_stock=True, rating=0.0

print()

# ============================================================
# EXAMPLE 3: Mutable Default Values — Using field()
# ============================================================

"""
⚠️ IMPORTANT: You CANNOT use mutable defaults (lists, dicts) directly!

This is WRONG and will raise an error:
    @dataclass
    class Cart:
        items: list = []   # ❌ ValueError: mutable default!

The reason: All instances would SHARE the same list!

SOLUTION: Use field(default_factory=list)
"""

@dataclass
class ShoppingCart:
    """
    Use field(default_factory=...) for mutable defaults.
    Each instance gets its OWN fresh list/dict.
    """
    customer_name: str
    # ✅ Correct way to have a list default
    items: List[str] = field(default_factory=list)
    # ✅ Correct way to have a dict default
    metadata: dict = field(default_factory=dict)

    def add_item(self, item):
        self.items.append(item)

    def get_total_items(self):
        return len(self.items)


print("=== Mutable Defaults with field() ===")
cart1 = ShoppingCart("Tasin")
cart2 = ShoppingCart("Mahmud")

cart1.add_item("Laptop")
cart1.add_item("Mouse")
cart2.add_item("Shirt")

print(cart1)     # items=['Laptop', 'Mouse'] — cart1's own list
print(cart2)     # items=['Shirt']           — cart2's own list
print(f"cart1 items: {cart1.items}")
print(f"cart2 items: {cart2.items}")

print()

# ============================================================
# EXAMPLE 4: Ordered Dataclass — order=True
# ============================================================

@dataclass(order=True)
class Student:
    """
    order=True automatically generates:
      __lt__, __le__, __gt__, __ge__
    Comparison is done field by field (in the order they're declared).
    ⚠️ sort_index is compared first!
    """
    # sort_index is used for comparison (comes first in field order)
    gpa: float        # compared first (highest field listed first for comparison)
    name: str
    student_id: int


print("=== Ordered Dataclass ===")
s1 = Student(3.8, "Tasin",  20062)
s2 = Student(3.5, "Mahmud", 20068)
s3 = Student(3.9, "Riya",   20075)

students = [s1, s2, s3]
students.sort()   # works because order=True generated __lt__ etc.
print("Sorted by GPA (ascending):")
for s in students:
    print(f"  {s.name}: GPA={s.gpa}")

print()

# ============================================================
# EXAMPLE 5: Frozen (Immutable) Dataclass — frozen=True
# ============================================================

@dataclass(frozen=True)
class Point:
    """
    frozen=True makes the dataclass IMMUTABLE.
    You cannot change any field after creation.
    Also automatically generates __hash__ (making it usable in sets/dicts).

    Useful for: coordinates, constants, keys in dictionaries
    """
    x: float
    y: float

    def distance_to(self, other):
        """Calculate distance between two Points."""
        import math
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


print("=== Frozen (Immutable) Dataclass ===")
p1 = Point(3.0, 4.0)
p2 = Point(0.0, 0.0)
print(f"Point: {p1}")
print(f"Distance from origin: {p1.distance_to(p2):.2f}")  # 5.0

# Try to modify — will raise FrozenInstanceError
try:
    p1.x = 10    # ❌ This will fail
except Exception as e:
    print(f"Error: {e}")   # cannot assign to field 'x'

# Frozen dataclasses are hashable — can be used as dict keys or in sets!
point_set = {p1, p2}
point_dict = {p1: "origin-point"}
print(f"Point in set: {p1 in point_set}")  # True

print()

# ============================================================
# EXAMPLE 6: field() — Exclude from repr/init/compare
# ============================================================

@dataclass
class Employee:
    """
    field() lets you customize behavior of individual fields:
      repr=False   → exclude from __repr__ output
      compare=False → exclude from __eq__ comparison
      init=False   → don't include in __init__, set in __post_init__
    """
    name: str
    department: str
    salary: float = field(repr=False)       # hide salary from repr
    bonus: float = field(default=0.0, compare=False)  # exclude from comparison
    _internal_id: int = field(default=0, init=False, repr=False)  # not in __init__

    def __post_init__(self):
        """
        __post_init__ is called AFTER __init__ automatically.
        Use it for validation or derived field initialization.
        """
        # Validate salary
        if self.salary < 0:
            raise ValueError("Salary cannot be negative!")
        # Auto-generate internal id
        self._internal_id = hash(self.name) % 10000


print("=== field() customization ===")
emp1 = Employee("Tasin", "Engineering", 80000.0, bonus=5000.0)
emp2 = Employee("Tasin", "Engineering", 90000.0, bonus=3000.0)

print(emp1)          # salary NOT shown in repr (repr=False)
print(f"Equal? {emp1 == emp2}")  # True — bonus excluded from compare (compare=False)

print()

# ============================================================
# EXAMPLE 7: Utility Functions — asdict, astuple, fields()
# ============================================================

@dataclass
class Config:
    host: str = "localhost"
    port: int = 8000
    debug: bool = False

config = Config("example.com", 443, True)
print("=== Dataclass Utilities ===")

# Convert to dictionary
config_dict = asdict(config)
print(f"As dict:  {config_dict}")
# Output: {'host': 'example.com', 'port': 443, 'debug': True}

# Convert to tuple
config_tuple = astuple(config)
print(f"As tuple: {config_tuple}")
# Output: ('example.com', 443, True)

# Get field metadata
print("Fields:")
for f in fields(config):
    print(f"  {f.name}: {f.type} = {getattr(config, f.name)}")

"""
SUMMARY — @DATACLASS PARAMETERS:
===================================

@dataclass                    → basic, generates __init__, __repr__, __eq__
@dataclass(order=True)        → also generates __lt__, __le__, __gt__, __ge__
@dataclass(frozen=True)       → immutable + hashable
@dataclass(repr=False)        → skip __repr__ generation
@dataclass(eq=False)          → skip __eq__ generation

field() parameters:
  default=...            → default value
  default_factory=list   → mutable default (use for list/dict)
  repr=False             → exclude from __repr__
  compare=False          → exclude from __eq__ and ordering
  init=False             → don't include in __init__

Special method:
  __post_init__()        → called after __init__, for validation/derived fields
"""
