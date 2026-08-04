
"""
================================================================================
  TOPIC 17: SINGLETON PATTERN
================================================================================

  WHAT IS IT?
  -----------
  The Singleton pattern ensures that a class has ONLY ONE instance, and provides 
  a global point of access to it. No matter how many times you try to instantiate 
  the class, you get the exact same object back.

  REAL-WORLD ANALOGY:
  -------------------
  Think of a country's President or a Government. There can be many citizens, 
  but there is only one Government. If you ask for the Government, you always 
  get the same entity.

  WHEN TO USE IT:
  ---------------
  - Database connections (you usually want one pool shared everywhere).
  - Configuration managers (read config once, share it globally).
  - Logging systems (one central logger).

================================================================================
"""

# ============================================================
# METHOD 1: Using __new__ (The Classic Python Way)
# ============================================================

class DatabaseSingleton:
    _instance = None # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        # If the instance doesn't exist yet, create it.
        if cls._instance is None:
            print("  [DB] Creating new Database connection...")
            cls._instance = super().__new__(cls)
            # You can also initialize attributes here to ensure they only run once
            cls._instance._connected = True 
        return cls._instance

    def __init__(self, db_name="default_db"):
        # Warning: __init__ WILL be called every time you call DatabaseSingleton()
        # even if it returns the same object! Be careful not to overwrite state.
        if not hasattr(self, 'db_name'):
            self.db_name = db_name

print("=== Singleton via __new__ ===")
db1 = DatabaseSingleton("UsersDB")
db2 = DatabaseSingleton("ProductsDB")

print(f"db1 ID: {id(db1)}, Name: {db1.db_name}")
print(f"db2 ID: {id(db2)}, Name: {db2.db_name}")
print(f"Are db1 and db2 the exact same object? {db1 is db2}")

print()

# ============================================================
# METHOD 2: Using a Metaclass (The most robust way)
# ============================================================
# We saw this in the Metaclasses topic, but here it is again.
# This approach avoids the problem of __init__ being called multiple times.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # Intercept the instantiation process
        if cls not in cls._instances:
            print(f"  [Meta] Creating first instance of {cls.__name__}...")
            # Create and store the instance
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        print("  [Logger] __init__ called (should only see this ONCE)")
        self.logs = []

    def log(self, msg):
        self.logs.append(msg)

print("=== Singleton via Metaclass ===")
logger1 = Logger()
logger1.log("System started")

logger2 = Logger() # __init__ is NOT called again!
logger2.log("User logged in")

print(f"logger1 logs: {logger1.logs}")
print(f"logger2 logs: {logger2.logs}") # Exact same list!
print(f"Are logger1 and logger2 the exact same object? {logger1 is logger2}")

"""
SUMMARY:
---------
- Singletons restrict instantiation to a single object.
- It's a great pattern to prevent wasting memory/resources on duplicates.
- Can be implemented via `__new__`, a metaclass, or simply by using a module 
  (in Python, a file `config.py` with variables is naturally a singleton!).
"""
