
"""
================================================================================
  TOPIC 13: METACLASSES — Classes that create Classes
================================================================================

  WHAT IS A METACLASS?
  --------------------
  In Python, everything is an object. A class is an object too!
  If a class is an object, who creates it? A Metaclass.
  By default, the metaclass for all classes in Python is `type`.

  You can write custom metaclasses to automatically modify or enforce rules
  on classes at the time they are created.

  REAL-WORLD ANALOGY:
  -------------------
  - Object is created by a Class. (Car is created by CarFactory blueprint)
  - Class is created by a Metaclass. (CarFactory blueprint is created by a Master Architect)

================================================================================
"""

# ============================================================
# EXAMPLE 1: Creating classes dynamically with `type`
# ============================================================

# Usually, we create classes like this:
class MyNormalClass:
    x = 5

# But `type` is actually a class factory (a metaclass).
# type(name, bases, attrs)
MyDynamicClass = type('MyDynamicClass', (), {'x': 10})

print("=== Creating Classes dynamically ===")
obj1 = MyNormalClass()
obj2 = MyDynamicClass()
print(f"Normal Class x: {obj1.x}")
print(f"Dynamic Class x: {obj2.x}")
print(f"Type of MyNormalClass: {type(MyNormalClass)}") # Output: <class 'type'>

print()

# ============================================================
# EXAMPLE 2: A Custom Metaclass to enforce rules
# ============================================================

class EnforceUppercaseMeta(type):
    """
    A custom metaclass that intercepts the creation of a class and 
    modifies it. Here, it forces all attributes/methods to be uppercase.
    """
    def __new__(cls, name, bases, attrs):
        # cls = the metaclass itself (EnforceUppercaseMeta)
        # name = name of the class being created
        # bases = tuple of base classes
        # attrs = dict of attributes/methods defined in the class

        uppercase_attrs = {}
        for key, value in attrs.items():
            if not key.startswith('__'): # don't modify dunder methods
                uppercase_attrs[key.upper()] = value
            else:
                uppercase_attrs[key] = value

        # Create the class using the modified attributes
        return super().__new__(cls, name, bases, uppercase_attrs)


class Config(metaclass=EnforceUppercaseMeta):
    """
    Because we specify metaclass=EnforceUppercaseMeta, when Python reads this class,
    it passes its name, bases, and attributes to our metaclass.
    """
    host = "localhost"
    port = 8080

    def connect(self):
        return f"Connecting to {self.HOST}:{self.PORT}..." # Must use uppercase here!

print("=== Custom Metaclass Enforcing Rules ===")
cfg = Config()

# Let's check the attributes available on cfg
print(f"Available attributes: {[attr for attr in dir(cfg) if not attr.startswith('__')]}")
print(f"Host (via HOST): {cfg.HOST}")
print(f"Calling CONNECT(): {cfg.CONNECT()}")

print()

# ============================================================
# EXAMPLE 3: Singleton via Metaclass
# ============================================================
# Metaclasses are a great way to implement the Singleton pattern
# (which we'll see more of in the Design Patterns section).

class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        # __call__ in a metaclass is triggered when you instantiate the class!
        if cls not in cls._instances:
            # If not created yet, create it and store it
            cls._instances[cls] = super().__call__(*args, **kwargs)
        # Return the stored instance
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing database connection...")

print("=== Singleton Metaclass ===")
db1 = Database() # Initializes
db2 = Database() # Returns existing instance

print(f"Are db1 and db2 the same object? {db1 is db2}")

"""
SUMMARY:
---------
- A Metaclass intercepts CLASS creation.
- Define a metaclass by inheriting from `type`.
- Override `__new__` to change the class before it is created.
- Override `__call__` to intercept when the class is instantiated.
- Use cases: ORMs (like Django), enforcing coding standards, auto-registering plugins.
"""
