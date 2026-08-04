
"""
================================================================================
  TOPIC 9: ABSTRACT PROPERTIES — Forcing Subclasses to Implement Properties
================================================================================

  WHAT ARE ABSTRACT PROPERTIES?
  ------------------------------
  You already know about:
    - @abstractmethod → forces subclasses to implement METHODS
    - @property       → turns a method into a read-only attribute

  Abstract Property = @property + @abstractmethod COMBINED
  It forces subclasses to implement a PROPERTY (not just a method).

  WHY USE ABSTRACT PROPERTIES?
  ------------------------------
  Sometimes you want ALL subclasses to have a specific ATTRIBUTE-STYLE access
  (like shape.area instead of shape.get_area()) but you want to ENFORCE it.

  REAL-WORLD ANALOGY:
  --------------------
  A Shape blueprint says: "Every shape MUST have an area and perimeter
  that can be accessed like: shape.area (not shape.get_area())"

  Without abstract property, a subclass could forget to implement 'area'
  or implement it as a regular method instead of a property.
  Abstract property ENFORCES the property interface.

================================================================================
"""

from abc import ABC, abstractmethod
import math


# ============================================================
# EXAMPLE 1: Shape with Abstract Properties
# ============================================================

class Shape(ABC):
    """
    Abstract base class for all geometric shapes.

    Abstract METHODS:     subclasses must implement the method
    Abstract PROPERTIES:  subclasses must implement the property

    area      → must be a @property (access as shape.area, not shape.area())
    perimeter → must be a @property
    name      → must be a @property that returns the shape's name
    """

    @property
    @abstractmethod
    def area(self):
        """
        Abstract property: Subclasses MUST implement this as a @property.
        If a subclass tries to implement it as a regular method or doesn't
        implement it at all, Python will raise TypeError when instantiating.
        """
        pass

    @property
    @abstractmethod
    def perimeter(self):
        """
        Abstract property: Every shape must have a perimeter.
        Accessed as shape.perimeter (not shape.perimeter())
        """
        pass

    @property
    @abstractmethod
    def name(self):
        """Abstract property: Every shape must have a name."""
        pass

    # Normal (non-abstract) method — available to all shapes
    def describe(self):
        """Uses the abstract properties — works for ANY shape."""
        return (f"Shape: {self.name}\n"
                f"  Area:      {self.area:.4f}\n"
                f"  Perimeter: {self.perimeter:.4f}")

    def is_larger_than(self, other_shape):
        """Compare two shapes using their area property."""
        return self.area > other_shape.area


# ----- Concrete subclass: Circle -----
class Circle(Shape):
    """
    Circle implements ALL abstract properties.
    They are implemented as @property decorated methods.
    """
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def name(self):
        """Implements abstract property 'name'."""
        return "Circle"

    @property
    def area(self):
        """Implements abstract property 'area'. Returns πr²"""
        return math.pi * self._radius ** 2

    @property
    def perimeter(self):
        """Implements abstract property 'perimeter'. Returns 2πr"""
        return 2 * math.pi * self._radius


# ----- Concrete subclass: Rectangle -----
class Rectangle(Shape):
    def __init__(self, width, height):
        self._width  = width
        self._height = height

    @property
    def name(self):
        return "Rectangle"

    @property
    def area(self):
        """Implements abstract property 'area'. Returns w × h"""
        return self._width * self._height

    @property
    def perimeter(self):
        """Implements abstract property 'perimeter'. Returns 2(w + h)"""
        return 2 * (self._width + self._height)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height


# ----- Concrete subclass: Triangle -----
class Triangle(Shape):
    def __init__(self, a, b, c):
        """a, b, c are the three sides."""
        self._a = a
        self._b = b
        self._c = c

    @property
    def name(self):
        return "Triangle"

    @property
    def area(self):
        """Heron's formula: area = √(s(s-a)(s-b)(s-c))"""
        s = self.perimeter / 2   # semi-perimeter
        return math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))

    @property
    def perimeter(self):
        return self._a + self._b + self._c


print("=== Abstract Properties: Shapes ===")
c = Circle(7)
r = Rectangle(5, 10)
t = Triangle(3, 4, 5)

# Note: access as shape.area NOT shape.area() — it's a property!
print(c.describe())
print()
print(r.describe())
print()
print(t.describe())
print()
print(f"Is Circle larger than Rectangle? {c.is_larger_than(r)}")

# Try to instantiate the abstract class directly
try:
    s = Shape()   # ❌ Should fail
except TypeError as e:
    print(f"\nCannot instantiate Shape: {e}")

# Try to create an incomplete subclass
try:
    class BadShape(Shape):
        pass       # ❌ Missing all abstract properties

    b = BadShape()
except TypeError as e:
    print(f"BadShape error: {e}")

print()

# ============================================================
# EXAMPLE 2: Abstract Property with Setter
# ============================================================

class Vehicle(ABC):
    """
    Vehicle with abstract property + abstract setter.
    Forces subclasses to implement BOTH getter and setter for speed.
    """

    @property
    @abstractmethod
    def speed(self):
        """Abstract property: current speed of vehicle."""
        pass

    @speed.setter
    @abstractmethod
    def speed(self, value):
        """
        Abstract setter: allows setting speed.
        Subclass must implement BOTH getter and setter.
        Note: order matters — @property first, then @speed.setter
        """
        pass

    @property
    @abstractmethod
    def max_speed(self):
        """Abstract property: maximum allowed speed."""
        pass

    def accelerate(self, amount):
        """Generic accelerate — works for any Vehicle."""
        new_speed = self.speed + amount
        if new_speed > self.max_speed:
            new_speed = self.max_speed
            print(f"  Speed capped at max: {self.max_speed}")
        self.speed = new_speed   # calls the abstract setter
        return f"Speed: {self.speed} km/h"


class Car(Vehicle):
    """Car implements both getter and setter for speed."""

    def __init__(self, brand, model):
        self.brand  = brand
        self.model  = model
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Speed cannot be negative!")
        self._speed = value

    @property
    def max_speed(self):
        return 200   # Car max speed: 200 km/h

    def __str__(self):
        return f"{self.brand} {self.model}"


class Bicycle(Vehicle):
    def __init__(self, brand):
        self.brand  = brand
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = max(0, value)

    @property
    def max_speed(self):
        return 40   # Bicycle max speed: 40 km/h


print("=== Abstract Property with Setter ===")
car  = Car("BMW", "M3")
bike = Bicycle("Trek")

print(f"{car}: {car.accelerate(80)}")
print(f"{car}: {car.accelerate(80)}")   # hits max
print(f"{car}: {car.accelerate(80)}")   # stays at max

print()
print(f"Bike: {bike.accelerate(25)}")
print(f"Bike: {bike.accelerate(25)}")   # hits max 40

print()

# ============================================================
# EXAMPLE 3: Abstract Properties in Data Models
# ============================================================

class BaseReport(ABC):
    """
    Abstract base for different report types.
    Every report must have: title, data, format.
    They must be properties so accessing them feels natural.
    """

    @property
    @abstractmethod
    def title(self):
        pass

    @property
    @abstractmethod
    def format(self):
        """The output format: 'csv', 'json', 'html', etc."""
        pass

    def generate(self):
        """Template method that uses abstract properties."""
        print(f"=== {self.title} ===")
        print(f"Format: {self.format.upper()}")
        self._write_content()

    @abstractmethod
    def _write_content(self):
        pass


class SalesReport(BaseReport):
    def __init__(self, month, sales_data):
        self.month = month
        self.sales_data = sales_data

    @property
    def title(self):
        return f"Sales Report — {self.month}"

    @property
    def format(self):
        return "csv"

    def _write_content(self):
        print("Date,Product,Amount")
        for row in self.sales_data:
            print(f"{row['date']},{row['product']},{row['amount']}")


class UserReport(BaseReport):
    def __init__(self, users):
        self.users = users

    @property
    def title(self):
        return "User Activity Report"

    @property
    def format(self):
        return "json"

    def _write_content(self):
        import json
        print(json.dumps(self.users, indent=2))


print("=== Abstract Properties in Reports ===")
sales = SalesReport("January 2026", [
    {"date": "2026-01-01", "product": "Laptop",  "amount": 75000},
    {"date": "2026-01-05", "product": "Monitor", "amount": 25000},
])
sales.generate()

print()
users = UserReport([
    {"name": "Tasin", "logins": 42},
    {"name": "Mahmud", "logins": 28},
])
users.generate()

"""
SUMMARY — ABSTRACT PROPERTIES:
================================

SYNTAX (order matters!):
  @property
  @abstractmethod
  def my_prop(self):
      pass

ABSTRACT PROPERTY + SETTER:
  @property
  @abstractmethod
  def speed(self):
      pass

  @speed.setter
  @abstractmethod
  def speed(self, value):
      pass

KEY POINTS:
  1. Subclasses MUST implement it as @property (not a plain method)
  2. Python raises TypeError if abstract property not implemented
  3. Cannot instantiate abstract class
  4. Access it like: obj.area  (not obj.area())
  5. Combine with @abstractmethod for setter enforcement

USE WHEN:
  - You want attribute-style access (obj.area not obj.get_area())
  - You want to ENFORCE that ALL subclasses have this property
  - Building template method patterns where base calls abstract properties
"""
