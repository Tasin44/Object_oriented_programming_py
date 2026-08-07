
"""
#================================================================================
  TOPIC 7: CLASS VARIABLES vs INSTANCE VARIABLES — Deep Dive
#================================================================================

  WHAT'S THE DIFFERENCE?
  ------------------------
  INSTANCE VARIABLE:
    - Defined with  self.something  inside __init__
    - Each object has its OWN copy
    - Changing it on one object doesn't affect others
    - Stored in the object's own __dict__

  CLASS VARIABLE:
    - Defined directly in the class body (outside any method)
    - SHARED across ALL instances
    - Changing it on the CLASS affects all instances
    - But changing it on an INSTANCE creates a NEW instance variable (shadow!)
    - Stored in the class __dict__

  REAL-WORLD ANALOGY:
  --------------------
  Think of a Bank:
    - class variable  = bank's interest rate (shared for all accounts)
    - instance variable = each account holder's balance (unique per person)

  THE MUTABLE DEFAULT TRAP:
  --------------------------
  ⚠️ Using a MUTABLE object (list, dict) as a class variable is dangerous!
  All instances will SHARE the same object!
  This is one of the most common Python OOP bugs.

#================================================================================
"""

# ============================================================
# EXAMPLE 1: Basic Class vs Instance Variables
# ============================================================

class Employee:
    """
    company_name and base_salary are CLASS VARIABLES — shared by all employees.
    name, department, salary are INSTANCE VARIABLES — unique per employee.
    """
    # ── CLASS VARIABLES ──────────────────────────────────
    company_name  = "TechCorp BD"    # shared by ALL employees
    base_salary   = 30000            # company-wide base salary
    employee_count = 0               # tracks total employees created

    def __init__(self, name, department, salary):
        # ── INSTANCE VARIABLES ───────────────────────────
        self.name       = name        # unique to each employee
        self.department = department  # unique to each employee
        self.salary     = salary      # unique to each employee

        # Incrementing CLASS variable inside __init__
        Employee.employee_count += 1  # Use class name to access class variables

    def show_info(self):
        return (f"{self.name} | {self.department} | "
                f"Salary: {self.salary} | Company: {Employee.company_name}")

    @classmethod
    def get_employee_count(cls):
        """Class method to access class variables."""
        return f"Total employees: {cls.employee_count}"

    @classmethod
    def change_company_name(cls, new_name):
        """Changes company name for ALL employees."""
        cls.company_name = new_name


print("=== Class vs Instance Variables ===")
emp1 = Employee("Tasin",  "Engineering", 80000)
emp2 = Employee("Mahmud", "Marketing",   60000)
emp3 = Employee("Riya",   "HR",          55000)

print(emp1.show_info())
print(emp2.show_info())
print(Employee.get_employee_count())   # Total employees: 3

# Change CLASS variable — affects ALL instances
Employee.change_company_name("NewTech BD")
print("\nAfter company name change:")
print(emp1.show_info())   # NewTech BD
print(emp2.show_info())   # NewTech BD

print()

# ============================================================
# EXAMPLE 2: The SHADOWING Trick — Instance overrides Class
# ============================================================

print("=== Shadowing Class Variable with Instance Variable ===")

class Circle:
    """
    pi is a class variable (shared).
    When you set self.pi on an instance, it creates a NEW instance variable
    that SHADOWS (hides) the class variable for that instance only.
    """
    pi = 3.14159      # Class variable

    def __init__(self, radius):
        self.radius = radius    # instance variable

    def area(self):
        return self.pi * self.radius ** 2   # uses self.pi (searches instance first, then class)


c1 = Circle(5)
c2 = Circle(10)

print(f"c1 area (default pi): {c1.area():.4f}")
print(f"c2 area (default pi): {c2.area():.4f}")

# Shadowing: set pi on c1 instance only
c1.pi = 3.14    # ← Creates a NEW instance variable on c1 only!

print(f"\nAfter c1.pi = 3.14:")
print(f"c1 pi:       {c1.pi}")          # 3.14    (instance variable on c1)
print(f"c2 pi:       {c2.pi}")          # 3.14159 (still using class variable!)
print(f"Circle.pi:   {Circle.pi}")      # 3.14159 (class variable unchanged)
print(f"c1 area (custom pi): {c1.area():.4f}")
print(f"c2 area (class  pi): {c2.area():.4f}")

# Check where pi is found for each:
print(f"\nc1 has its own pi in __dict__: {'pi' in c1.__dict__}")  # True
print(f"c2 has its own pi in __dict__: {'pi' in c2.__dict__}")  # False

print()

# ============================================================
# EXAMPLE 3: ⚠️ THE MUTABLE DEFAULT TRAP (MUST KNOW!)
# ============================================================

print("=== DANGER: Mutable Class Variable Bug ===")

class BuggyStudent:
    """
    ⚠️ BUG: 'courses' is a mutable class variable (a list).
    ALL instances share the SAME list object!
    Adding to it on one student affects ALL students!
    This is one of the most common Python bugs.
    """
    courses = []    # ❌ SHARED list — DANGEROUS!

    def __init__(self, name):
        self.name = name

    def add_course(self, course):
        self.courses.append(course)    # modifies the SHARED list!


print("Buggy version:")
s1 = BuggyStudent("Tasin")
s2 = BuggyStudent("Mahmud")

s1.add_course("Python")
s2.add_course("Java")

print(f"s1 courses: {s1.courses}")    # ['Python', 'Java'] ← BUG! Has Java too!
print(f"s2 courses: {s2.courses}")    # ['Python', 'Java'] ← Same shared list!
print(f"Same object? {s1.courses is s2.courses}")  # True — same list!

print()

class CorrectStudent:
    """
    ✅ FIX: Initialize the mutable default in __init__ using self.
    Each instance gets its OWN fresh list.
    """
    def __init__(self, name):
        self.name    = name
        self.courses = []    # ✅ Instance variable — each student gets own list

    def add_course(self, course):
        self.courses.append(course)


print("Fixed version:")
s1 = CorrectStudent("Tasin")
s2 = CorrectStudent("Mahmud")

s1.add_course("Python")
s2.add_course("Java")

print(f"s1 courses: {s1.courses}")    # ['Python']  ← Correct!
print(f"s2 courses: {s2.courses}")    # ['Java']    ← Correct!
print(f"Same object? {s1.courses is s2.courses}")  # False — different lists!

print()

# ============================================================
# EXAMPLE 4: Class Variables for Tracking and Counters
# ============================================================

class DatabaseConnection:
    """
    Class variable used as a counter and for tracking all instances.
    Common pattern: use class variables for SHARED state.
    """
    _instance_count  = 0       # how many connections are open
    _max_connections = 5       # class-level limit
    _all_connections = []      # ← class variable list (intentionally shared!)

    def __init__(self, host, port, db_name):
        if DatabaseConnection._instance_count >= DatabaseConnection._max_connections:
            raise ConnectionError("Max connections reached!")

        self.host    = host
        self.port    = port
        self.db_name = db_name
        self.conn_id = DatabaseConnection._instance_count + 1

        DatabaseConnection._instance_count += 1
        DatabaseConnection._all_connections.append(self)

    def close(self):
        DatabaseConnection._instance_count -= 1
        DatabaseConnection._all_connections.remove(self)
        print(f"Connection {self.conn_id} to {self.db_name} closed.")

    def __repr__(self):
        return f"DB({self.host}:{self.port}/{self.db_name})"

    @classmethod
    def active_connections(cls):
        return f"Active: {cls._instance_count} | All: {cls._all_connections}"


print("=== DatabaseConnection tracker ===")
db1 = DatabaseConnection("localhost", 5432, "main_db")
db2 = DatabaseConnection("192.168.1.1", 3306, "user_db")
print(DatabaseConnection.active_connections())

db1.close()
print(DatabaseConnection.active_connections())

print()

# ============================================================
# EXAMPLE 5: Lookup table and Caching using Class Variables
# ============================================================

class FibCalculator:
    """
    Class variable used as a SHARED CACHE across all instances.
    Once computed, Fibonacci numbers are stored for everyone.
    This is the class-level caching pattern.
    """
    _cache = {0: 0, 1: 1}   # intentionally shared class variable (cache)

    def compute(self, n):
        """Calculate fibonacci(n) using memoization stored in class cache."""
        if n in FibCalculator._cache:
            return FibCalculator._cache[n]
        result = self.compute(n - 1) + self.compute(n - 2)
        FibCalculator._cache[n] = result   # store in shared cache
        return result


print("=== Shared Cache via Class Variable ===")
calc1 = FibCalculator()
calc2 = FibCalculator()

print(f"calc1 fib(10): {calc1.compute(10)}")  # 55
print(f"calc2 fib(10): {calc2.compute(10)}")  # 55 — from cache!
print(f"Cache size: {len(FibCalculator._cache)} numbers stored")
print(f"Cache shares between instances: {calc1._cache is calc2._cache}")  # True

"""
SUMMARY — CLASS vs INSTANCE VARIABLES:
#=======================================

CLASS VARIABLE:
  class MyClass:
      class_var = "shared"       # defined at class level

  - Shared by ALL instances
  - Access via:  MyClass.class_var  or  self.class_var (reads class)
  - Change via:  MyClass.class_var = "new"  (affects ALL)
  - If you do:   self.class_var = "new"  → creates INSTANCE shadow!

INSTANCE VARIABLE:
  def __init__(self):
      self.inst_var = "mine"     # defined inside __init__

  - Unique to each instance
  - Stored in instance's __dict__

MUTABLE DEFAULT TRAP:
  ❌ class A:
        shared_list = []          # BUG: shared by all instances!

  ✅ class A:
        def __init__(self):
            self.my_list = []     # FIX: each instance gets own list

Python variable lookup order (LEGB for classes):
  instance __dict__ → class __dict__ → parent class __dict__ → ...
"""
