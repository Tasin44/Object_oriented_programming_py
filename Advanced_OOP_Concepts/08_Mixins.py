
"""
#================================================================================
  TOPIC 8: MIXINS — Reusable Behavior Classes
#================================================================================

  WHAT ARE MIXINS?
  -----------------
  A Mixin is a small, focused class that adds a specific BEHAVIOR (a set of
  methods) to other classes through multiple inheritance.

  KEY RULES OF A MIXIN:
  ----------------------
  1. A mixin is NOT meant to be instantiated on its own
  2. A mixin is NOT a standalone, complete class
  3. A mixin adds ONE specific behavior (logging, serialization, etc.)
  4. A mixin does NOT define __init__ (usually)
  5. Name convention: always end with "Mixin" (e.g., LoggingMixin)

  REAL-WORLD ANALOGY:
  --------------------
  Think of USB ports on a laptop.
  The "USB capability" is like a mixin — it's a feature that many different
  devices can have WITHOUT being the same type of device.
  A laptop, TV, car dashboard — all can "mix in" the USB feature.

  WHY USE MIXINS?
  ---------------
  ✅ Avoid code duplication (DRY principle)
  ✅ Add behavior to any class without deep inheritance chains
  ✅ Keep classes focused and single-purpose
  ✅ Combine multiple behaviors freely

#================================================================================
"""

import json
import time
from datetime import datetime


# ============================================================
# MIXIN 1: LoggingMixin — adds print/logging to any class
# ============================================================

class LoggingMixin:
    """
    Adds logging capability to any class.
    Classes that include this mixin get log(), log_warning(), log_error() methods.

    Note: LoggingMixin has no __init__ — it just adds methods.
    Note: 'self' refers to the MIXED class instance (e.g., UserService instance)
    """

    def log(self, message):
        """Log a general info message with timestamp."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        class_name = self.__class__.__name__
        print(f"[{timestamp}] [INFO] [{class_name}] {message}")

    def log_warning(self, message):
        """Log a warning message."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        class_name = self.__class__.__name__
        print(f"[{timestamp}] [WARN] [{class_name}] ⚠️ {message}")

    def log_error(self, message):
        """Log an error message."""
        timestamp = datetime.now().strftime("%H:%M:%S")
        class_name = self.__class__.__name__
        print(f"[{timestamp}] [ERR ] [{class_name}] ❌ {message}")


# ============================================================
# MIXIN 2: SerializationMixin — convert to/from JSON and dict
# ============================================================

class SerializationMixin:
    """
    Adds serialization capability to any class.
    Any class with this mixin can be converted to/from dict and JSON.

    Requirement: The mixed class must have instance attributes in __dict__
    """

    def to_dict(self):
        """Convert object attributes to a dictionary."""
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith('_')}   # exclude private attrs

    def to_json(self):
        """Convert object to a JSON string."""
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_dict(cls, data):
        """
        Create an instance from a dictionary.
        Uses __new__ to create instance without calling __init__,
        then manually sets attributes.
        """
        obj = cls.__new__(cls)
        for key, value in data.items():
            setattr(obj, key, value)
        return obj


# ============================================================
# MIXIN 3: ValidationMixin — validate data before setting
# ============================================================

class ValidationMixin:
    """
    Adds validation helper methods to any class.
    Provides methods for common validation tasks.
    """

    def validate_positive(self, value, field_name):
        """Raise ValueError if value is not positive."""
        if value <= 0:
            raise ValueError(f"{field_name} must be positive, got: {value}")
        return value

    def validate_not_empty(self, value, field_name):
        """Raise ValueError if string is empty."""
        if not value or not str(value).strip():
            raise ValueError(f"{field_name} cannot be empty!")
        return value.strip()

    def validate_range(self, value, min_val, max_val, field_name):
        """Raise ValueError if value is out of range."""
        if not (min_val <= value <= max_val):
            raise ValueError(f"{field_name} must be between {min_val} and {max_val}")
        return value


# ============================================================
# MIXIN 4: TimestampMixin — track created/updated times
# ============================================================

class TimestampMixin:
    """
    Adds automatic timestamp tracking to any class.
    Sets created_at when object is created, updated_at when update() is called.
    """

    def __init__(self, *args, **kwargs):
        """
        This __init__ uses super() cooperatively.
        It sets timestamps and then calls the next class in MRO.
        """
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = None

    def touch(self):
        """Update the updated_at timestamp."""
        self.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Updated at: {self.updated_at}"


# ============================================================
# NOW: Combine Mixins into Real Classes
# ============================================================

# ----- Class using LoggingMixin + ValidationMixin -----------

class BankAccount(LoggingMixin, ValidationMixin):
    """
    BankAccount mixes in:
    - LoggingMixin → log() method
    - ValidationMixin → validate_positive(), validate_not_empty()

    Notice: BankAccount is the MAIN class, mixins come AFTER in inheritance.
    Convention: ClassName(MainBase, Mixin1, Mixin2)
    """

    def __init__(self, account_holder, initial_balance):
        # Use ValidationMixin methods to validate inputs
        self.account_holder = self.validate_not_empty(account_holder, "Account holder")
        self.balance = self.validate_positive(initial_balance, "Initial balance")
        self.log(f"Account created for {self.account_holder} with {self.balance} BDT")

    def deposit(self, amount):
        self.validate_positive(amount, "Deposit amount")
        self.balance += amount
        self.log(f"Deposited {amount} BDT. New balance: {self.balance}")

    def withdraw(self, amount):
        self.validate_positive(amount, "Withdrawal amount")
        if amount > self.balance:
            self.log_warning(f"Insufficient funds! Tried: {amount}, Have: {self.balance}")
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        self.log(f"Withdrew {amount} BDT. New balance: {self.balance}")

    def get_balance(self):
        return self.balance


print("=== BankAccount with LoggingMixin + ValidationMixin ===")
account = BankAccount("Tasin Mahmud", 50000)
account.deposit(10000)
account.withdraw(5000)
try:
    account.withdraw(100000)  # should fail with log warning
except ValueError as e:
    print(f"Error: {e}")

print()

# ----- Class using LoggingMixin + SerializationMixin --------

class Product(LoggingMixin, SerializationMixin):
    """
    Product mixes in:
    - LoggingMixin → logging capability
    - SerializationMixin → to_dict(), to_json(), from_dict()
    """

    def __init__(self, name, price, category, stock):
        self.name     = name
        self.price    = price
        self.category = category
        self.stock    = stock
        self.log(f"Product '{name}' created at {price} BDT")

    def update_price(self, new_price):
        old_price = self.price
        self.price = new_price
        self.log(f"Price updated: {old_price} → {new_price}")


print("=== Product with LoggingMixin + SerializationMixin ===")
p = Product("Python Book", 800, "Education", 50)
p.update_price(750)

# SerializationMixin methods
print("\nTo dict:")
print(p.to_dict())

print("\nTo JSON:")
print(p.to_json())

# Recreate from dict
data = {"name": "Java Book", "price": 900, "category": "Education", "stock": 30}
p2 = Product.from_dict(data)
print(f"\nFrom dict: {p2.name}, {p2.price} BDT")

print()

# ----- Class using ALL 4 Mixins ----------------------------

class User(TimestampMixin, LoggingMixin, SerializationMixin, ValidationMixin):
    """
    User mixes in ALL four mixins.
    This shows how freely you can combine behaviors.

    MRO order (left to right):
    User → TimestampMixin → LoggingMixin → SerializationMixin → ValidationMixin → object
    """

    def __init__(self, username, email, age):
        # ValidationMixin methods for input validation
        self.username = self.validate_not_empty(username, "Username")
        self.email    = self.validate_not_empty(email, "Email")
        self.age      = self.validate_range(age, 1, 150, "Age")
        # TimestampMixin __init__ is called via super()
        super().__init__()
        self.log(f"User '{username}' registered")

    def update_email(self, new_email):
        self.email = self.validate_not_empty(new_email, "Email")
        self.touch()   # TimestampMixin method — updates updated_at
        self.log(f"Email updated to {new_email}")


print("=== User with ALL 4 Mixins ===")
user = User("tasin44", "tasin@email.com", 24)
print(f"Created at: {user.created_at}")

user.update_email("newtasin@email.com")
print(f"Updated at: {user.updated_at}")

print("\nUser as JSON:")
print(user.to_json())

print("\nMRO order:")
for cls in User.__mro__:
    print(f"  → {cls.__name__}")

"""
SUMMARY — MIXINS:
#==================

Pattern:  class MyClass(PrimaryBase, Mixin1, Mixin2, Mixin3):

Rules:
  1. Name mixins with "Mixin" suffix
  2. Mixins should not define __init__ (usually)
  3. If mixin has __init__, use super() cooperatively
  4. Mixins are NOT standalone — always used WITH another class
  5. Keep mixins small and focused (one responsibility each)

Common Mixins in real frameworks:
  Django:  LoginRequiredMixin, PermissionMixin, TemplateResponseMixin
  Python:  ABC, io.IOBase mixins
  DRF:     CreateModelMixin, RetrieveModelMixin, etc.
"""
