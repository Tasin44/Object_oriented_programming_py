
"""
================================================================================
  TOPIC 3: METHOD OVERLOADING (Simulated in Python)
================================================================================

  WHAT IS METHOD OVERLOADING?
  ----------------------------
  In languages like Java/C++, method overloading means:
  You can define MULTIPLE methods with the SAME NAME but DIFFERENT parameters.

  Example in Java:
    void draw(int radius)       { ... }  // draw circle
    void draw(int w, int h)     { ... }  // draw rectangle
    void draw(String shape)     { ... }  // draw by name

  PROBLEM IN PYTHON:
  ------------------
  Python does NOT support true method overloading natively.
  If you define the same method name twice, the second one OVERWRITES the first.

  Example:
    def greet(name):       ...
    def greet(name, age):  ...   # ← This REPLACES the first greet!

  PYTHON'S 3 SOLUTIONS:
  ---------------------
  1. Default Arguments    → handle optional params
  2. *args / **kwargs     → accept any number of args
  3. @singledispatchmethod → true type-based overloading (Python 3.8+)

================================================================================
"""

# ============================================================
# EXAMPLE 1: Naive mistake — defining same method twice
# ============================================================

class BrokenClass:
    def greet(self, name):
        print(f"Hello, {name}!")

    # ❌ This REPLACES the first greet method above!
    def greet(self, name, age):
        print(f"Hello, {name}! You are {age} years old.")

obj = BrokenClass()
# obj.greet("Tasin")       # ❌ TypeError: greet() missing 1 required positional argument: 'age'
obj.greet("Tasin", 24)     # ✅ Only the second definition exists

print()

# ============================================================
# SOLUTION 1: Default Arguments to Simulate Overloading
# ============================================================

class Calculator:
    """
    Using default arguments to handle different numbers of parameters.
    This is the simplest and most common approach in Python.
    """
    def add(self, a, b, c=0):
        """
        If called with 2 args: a + b
        If called with 3 args: a + b + c
        The 'c=0' means c is OPTIONAL — defaults to 0
        """
        return a + b + c

    def power(self, base, exponent=2):
        """
        If called with 1 arg: base squared (default exponent=2)
        If called with 2 args: base to the given power
        """
        return base ** exponent


calc = Calculator()
print("=== Default Arguments ===")
print(calc.add(5, 3))       # Output: 8   (c defaults to 0)
print(calc.add(5, 3, 2))    # Output: 10  (all 3 given)
print(calc.power(4))        # Output: 16  (4^2, exponent defaults to 2)
print(calc.power(2, 10))    # Output: 1024 (2^10)

print()

# ============================================================
# SOLUTION 2: *args to Accept Any Number of Arguments
# ============================================================

class AdvancedCalculator:
    """
    Using *args allows any number of arguments.
    *args collects all positional arguments into a TUPLE.
    """
    def add(self, *args):
        """
        Can add 2, 3, 4, 100 numbers — any count!
        *args receives them all as a tuple.
        """
        if len(args) == 0:
            return 0
        return sum(args)   # sum() works on a tuple too

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def describe(self, *args, **kwargs):
        """
        *args  → positional arguments (as tuple)
        **kwargs → keyword arguments (as dict)
        Simulates multiple method signatures in one function.
        """
        if kwargs.get("mode") == "formal":
            return f"Hello, Mr./Ms. {args[0]}!"
        elif kwargs.get("mode") == "casual":
            return f"Hey {args[0]}! What's up?"
        else:
            return f"Hi {args[0]}!"


adv = AdvancedCalculator()
print("=== *args ===")
print(adv.add(1, 2))             # Output: 3
print(adv.add(1, 2, 3, 4, 5))   # Output: 15
print(adv.multiply(2, 3))        # Output: 6
print(adv.multiply(2, 3, 4))     # Output: 24
print(adv.describe("Tasin"))                    # Hi Tasin!
print(adv.describe("Tasin", mode="formal"))     # Hello, Mr./Ms. Tasin!
print(adv.describe("Tasin", mode="casual"))     # Hey Tasin! What's up?

print()

# ============================================================
# SOLUTION 3: Type Checking Inside Method (isinstance)
# ============================================================

class Formatter:
    """
    Simulate overloading by checking the TYPE of argument at runtime.
    This is a classic manual approach — works but not the most elegant.
    """
    def display(self, data):
        """
        Behaves differently based on the TYPE of 'data':
        - int   → shows as integer with label
        - str   → shows in quotes
        - list  → shows as numbered list
        - dict  → shows as key: value pairs
        """
        if isinstance(data, int):
            print(f"Integer: {data}")

        elif isinstance(data, float):
            print(f"Float: {data:.2f}")

        elif isinstance(data, str):
            print(f'String: "{data}"')

        elif isinstance(data, list):
            print("List:")
            for i, item in enumerate(data, 1):
                print(f"  {i}. {item}")

        elif isinstance(data, dict):
            print("Dictionary:")
            for key, value in data.items():
                print(f"  {key}: {value}")

        else:
            print(f"Unknown type: {data}")


f = Formatter()
print("=== Type-based dispatch ===")
f.display(42)
f.display(3.14159)
f.display("Hello World")
f.display(["Python", "Java", "C++"])
f.display({"name": "Tasin", "age": 24, "city": "Dhaka"})

print()

# ============================================================
# SOLUTION 4: @singledispatchmethod — TRUE Method Overloading
# ============================================================

from functools import singledispatch

"""
singledispatch is the REAL method overloading in Python.
It dispatches (chooses) which function to call based on the TYPE
of the FIRST argument.

@singledispatch     → for standalone functions
@singledispatchmethod → for class methods (Python 3.8+)
"""

@singledispatch
def process(data):
    """Default fallback — called if no specific handler matches."""
    print(f"Cannot process type: {type(data).__name__}")


@process.register(int)
def _(data):
    """Called when data is an int."""
    print(f"Processing integer: {data * 2}")


@process.register(str)
def _(data):
    """Called when data is a string."""
    print(f"Processing string: '{data.upper()}'")


@process.register(list)
def _(data):
    """Called when data is a list."""
    print(f"Processing list with {len(data)} items: {sorted(data)}")


@process.register(float)
def _(data):
    """Called when data is a float."""
    print(f"Processing float: {data:.4f}")


print("=== @singledispatch ===")
process(42)              # int handler
process("hello")         # str handler
process([3, 1, 4, 1, 5]) # list handler
process(3.14159)         # float handler
process({"key": "val"}) # fallback — no handler for dict

print()

# ============================================================
# SOLUTION 5: Using singledispatchmethod in a Class (Python 3.8+)
# ============================================================

from functools import singledispatchmethod

class Printer:
    """
    Using singledispatchmethod inside a class.
    This is TRUE method overloading based on argument type.
    """
    @singledispatchmethod
    def print_data(self, data):
        """Default handler."""
        print(f"Unknown type: {type(data)}")

    @print_data.register(int)
    def _(self, data):
        print(f"🔢 Integer: {data}")

    @print_data.register(str)
    def _(self, data):
        print(f"📝 String: {data!r}")

    @print_data.register(list)
    def _(self, data):
        print(f"📋 List ({len(data)} items): {data}")

    @print_data.register(dict)
    def _(self, data):
        print(f"📖 Dict ({len(data)} keys): {list(data.keys())}")


print("=== @singledispatchmethod in class ===")
printer = Printer()
printer.print_data(100)
printer.print_data("Tasin Mahmud")
printer.print_data([1, 2, 3, 4, 5])
printer.print_data({"name": "Tasin", "city": "Dhaka"})

"""
SUMMARY — METHOD OVERLOADING IN PYTHON:
=========================================

Python has NO native method overloading.
But we have 4 great alternatives:

1. Default Arguments  → simplest, for optional params
2. *args / **kwargs   → flexible, any number of args
3. isinstance()       → manual type checking inside one method
4. @singledispatch    → real type-based dispatch (most Pythonic)

Rule of thumb:
  • Use default args for simple optional params
  • Use @singledispatch when behavior truly changes by type
  • Use *args when accepting variable number of same-type args
"""
