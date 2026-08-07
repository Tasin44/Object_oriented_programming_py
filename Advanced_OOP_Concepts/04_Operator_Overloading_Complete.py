
"""
#================================================================================
  TOPIC 4: OPERATOR OVERLOADING — Complete Guide
#================================================================================

  WHAT IS OPERATOR OVERLOADING?
  ------------------------------
  Operator overloading means giving custom meaning to Python operators
  (+, -, *, /, [], in, len, etc.) for YOUR classes.

  You already know:  __add__, __lt__, __gt__, __len__, __str__, __call__
  THIS FILE covers the ones you're MISSING:
    ✅ __sub__        → subtraction (-)
    ✅ __mul__        → multiplication (*)
    ✅ __truediv__    → division (/)
    ✅ __floordiv__   → floor division (//)
    ✅ __mod__        → modulo (%)
    ✅ __pow__        → power (**)
    ✅ __neg__        → unary minus (-x)
    ✅ __abs__        → abs(x)
    ✅ __eq__         → equality (==)
    ✅ __ne__         → not equal (!=)
    ✅ __contains__   → membership (in)
    ✅ __getitem__    → indexing (obj[i])
    ✅ __setitem__    → index assignment (obj[i] = value)
    ✅ __delitem__    → index deletion (del obj[i])
    ✅ __bool__       → truthiness (bool(obj) or if obj:)
    ✅ __iter__       → makes object iterable (for x in obj)

  HOW IT WORKS:
  -------------
  When you write:  v1 + v2
  Python internally calls: v1.__add__(v2)

  When you write:  v1[0]
  Python internally calls: v1.__getitem__(0)

#================================================================================
"""

# ============================================================
# EXAMPLE 1: Vector class — Math operators
# ============================================================

class Vector:
    """
    A 2D mathematical vector (x, y).
    We'll overload almost every operator to make it behave like a real vector.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # ─── String representation ─────────────────────────────
    def __str__(self):
        """Called by print() and str()"""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Called in interactive shell / repr()"""
        return f"Vector({self.x!r}, {self.y!r})"

    # ─── Arithmetic operators ──────────────────────────────
    def __add__(self, other):
        """v1 + v2  →  adds x and y components"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """v1 - v2  →  subtracts components"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """
        v1 * 3  →  scalar multiplication
        Multiplies both components by a number.
        """
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """
        3 * v1  →  reverse multiplication
        Python tries v1.__mul__(3) first, then 3.__rmul__(v1)
        __rmul__ handles when the scalar is on the LEFT side
        """
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        """v1 / 2  →  float division of each component"""
        if scalar == 0:
            raise ValueError("Cannot divide by zero!")
        return Vector(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        """v1 // 2  →  integer (floor) division"""
        return Vector(self.x // scalar, self.y // scalar)

    def __mod__(self, scalar):
        """v1 % 3  →  modulo of each component"""
        return Vector(self.x % scalar, self.y % scalar)

    def __pow__(self, exponent):
        """v1 ** 2  →  power of each component"""
        return Vector(self.x ** exponent, self.y ** exponent)

    # ─── Unary operators ──────────────────────────────────
    def __neg__(self):
        """-v1  →  negates both components"""
        return Vector(-self.x, -self.y)

    def __abs__(self):
        """abs(v1)  →  magnitude (length) of vector: √(x²+y²)"""
        import math
        return math.sqrt(self.x**2 + self.y**2)

    # ─── Comparison operators ──────────────────────────────
    def __eq__(self, other):
        """v1 == v2  →  True if both components are equal"""
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """v1 != v2  →  opposite of __eq__"""
        return not self.__eq__(other)

    def __lt__(self, other):
        """v1 < v2  →  compare by magnitude"""
        return abs(self) < abs(other)

    def __gt__(self, other):
        """v1 > v2  →  compare by magnitude"""
        return abs(self) > abs(other)

    def __le__(self, other):
        """v1 <= v2"""
        return abs(self) <= abs(other)

    def __ge__(self, other):
        """v1 >= v2"""
        return abs(self) >= abs(other)

    # ─── Boolean ──────────────────────────────────────────
    def __bool__(self):
        """
        bool(v1) or  if v1: ...
        A Vector is True if it's NOT the zero vector (0, 0)
        """
        return self.x != 0 or self.y != 0


print("=== Vector Math Operators ===")
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")        # __add__
print(f"v1 - v2 = {v1 - v2}")        # __sub__
print(f"v1 * 3  = {v1 * 3}")         # __mul__
print(f"5 * v1  = {5 * v1}")         # __rmul__
print(f"v1 / 2  = {v1 / 2}")         # __truediv__
print(f"v1 // 2 = {v1 // 2}")        # __floordiv__
print(f"v1 % 3  = {v1 % 3}")         # __mod__
print(f"v1 ** 2 = {v1 ** 2}")        # __pow__
print(f"-v1     = {-v1}")            # __neg__
print(f"|v1|    = {abs(v1):.2f}")    # __abs__ → √(3²+4²) = 5.0
print(f"v1 == v2? {v1 == v2}")       # __eq__
print(f"v1 != v2? {v1 != v2}")       # __ne__
print(f"v1 > v2?  {v1 > v2}")        # __gt__
zero_v = Vector(0, 0)
print(f"bool(v1) = {bool(v1)}")      # __bool__ → True (not zero)
print(f"bool(zero_v) = {bool(zero_v)}")  # __bool__ → False

print()

# ============================================================
# EXAMPLE 2: Custom List — __getitem__, __setitem__, __contains__, __iter__
# ============================================================

class SmartList:
    """
    A custom list-like object that supports:
    - obj[i]      → indexing
    - obj[i] = x  → assignment
    - del obj[i]  → deletion
    - x in obj    → membership check
    - for x in obj → iteration
    """
    def __init__(self, *items):
        # Store items in an internal list
        self._data = list(items)

    def __str__(self):
        return f"SmartList{self._data}"

    def __len__(self):
        """len(obj) → number of items"""
        return len(self._data)

    def __getitem__(self, index):
        """
        obj[index]  → get item at position
        Supports both positive and negative indexing.
        """
        if isinstance(index, slice):
            return SmartList(*self._data[index])
        return self._data[index]

    def __setitem__(self, index, value):
        """obj[index] = value  → set item at position"""
        self._data[index] = value

    def __delitem__(self, index):
        """del obj[index]  → delete item at position"""
        print(f"Deleting: {self._data[index]}")
        del self._data[index]

    def __contains__(self, item):
        """
        item in obj  →  True if item is in the list
        Python calls this when you use the 'in' keyword.
        """
        return item in self._data

    def __iter__(self):
        """
        for item in obj:  →  makes the object iterable
        Returns an iterator over the internal data.
        """
        return iter(self._data)

    def __add__(self, other):
        """sl1 + sl2  →  combine two SmartLists"""
        return SmartList(*(self._data + other._data))

    def __bool__(self):
        """bool(obj)  →  True if list is not empty"""
        return len(self._data) > 0


print("=== SmartList Operators ===")
sl = SmartList(10, 20, 30, 40, 50)
print(f"SmartList: {sl}")
print(f"Length: {len(sl)}")          # __len__
print(f"sl[0] = {sl[0]}")            # __getitem__
print(f"sl[-1] = {sl[-1]}")          # __getitem__ negative index
print(f"sl[1:3] = {sl[1:3]}")        # __getitem__ slice

sl[2] = 999                          # __setitem__
print(f"After sl[2] = 999: {sl}")

del sl[0]                            # __delitem__
print(f"After del sl[0]: {sl}")

print(f"20 in sl? {20 in sl}")       # __contains__
print(f"999 in sl? {999 in sl}")     # __contains__

print("Iterating:")
for item in sl:                      # __iter__
    print(f"  {item}")

sl2 = SmartList(100, 200)
combined = sl + sl2                  # __add__
print(f"Combined: {combined}")

print()

# ============================================================
# EXAMPLE 3: Money class — real-world operators
# ============================================================

class Money:
    """
    Money class with currency.
    Demonstrates arithmetic, comparison, and string operators.
    """
    def __init__(self, amount, currency="BDT"):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

    def __repr__(self):
        return f"Money({self.amount!r}, {self.currency!r})"

    def _check_currency(self, other):
        """Helper to ensure we're operating on same currency."""
        if self.currency != other.currency:
            raise ValueError(f"Cannot operate on {self.currency} and {other.currency}")

    def __add__(self, other):
        self._check_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        self._check_currency(other)
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, factor):
        """Money * 3 → multiply amount"""
        return Money(self.amount * factor, self.currency)

    def __truediv__(self, divisor):
        """Money / 3 → split bill"""
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        self._check_currency(other)
        return self.amount < other.amount

    def __gt__(self, other):
        self._check_currency(other)
        return self.amount > other.amount

    def __bool__(self):
        """True if amount > 0"""
        return self.amount > 0


print("=== Money Operations ===")
price1  = Money(500, "BDT")
price2  = Money(300, "BDT")
discount = Money(50, "BDT")

print(f"price1 = {price1}")
print(f"price2 = {price2}")
print(f"Total  = {price1 + price2}")      # 800 BDT
print(f"After discount = {price1 - discount}")  # 450 BDT
print(f"Triple order = {price1 * 3}")    # 1500 BDT
print(f"Split 3 ways = {price1 / 3}")    # 166.67 BDT
print(f"price1 > price2? {price1 > price2}")   # True
print(f"price1 == price1? {price1 == Money(500, 'BDT')}")  # True

"""
QUICK REFERENCE — ALL MAGIC METHODS FOR OPERATORS:
#====================================================

ARITHMETIC:
  __add__(self, other)      →  self + other
  __sub__(self, other)      →  self - other
  __mul__(self, other)      →  self * other
  __truediv__(self, other)  →  self / other
  __floordiv__(self, other) →  self // other
  __mod__(self, other)      →  self % other
  __pow__(self, other)      →  self ** other
  __neg__(self)             →  -self
  __abs__(self)             →  abs(self)
  __rmul__(self, other)     →  other * self  (reversed)

COMPARISON:
  __eq__(self, other)       →  self == other
  __ne__(self, other)       →  self != other
  __lt__(self, other)       →  self < other
  __gt__(self, other)       →  self > other
  __le__(self, other)       →  self <= other
  __ge__(self, other)       →  self >= other

CONTAINER:
  __len__(self)             →  len(self)
  __getitem__(self, key)    →  self[key]
  __setitem__(self, key, v) →  self[key] = v
  __delitem__(self, key)    →  del self[key]
  __contains__(self, item)  →  item in self
  __iter__(self)            →  for x in self:

MISC:
  __bool__(self)            →  bool(self)  or  if self:
  __str__(self)             →  str(self)   or  print(self)
  __repr__(self)            →  repr(self)
  __call__(self, ...)       →  self(...)
  __len__(self)             →  len(self)
"""
