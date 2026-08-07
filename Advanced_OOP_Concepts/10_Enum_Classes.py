
"""
#================================================================================
  TOPIC 10: ENUM CLASSES — Named Constants with OOP Power
#================================================================================

  WHAT IS AN ENUM?
  -----------------
  Enum (Enumeration) is a set of named constants grouped together in a class.
  Instead of using magic numbers or raw strings, you use descriptive names.

  WITHOUT ENUM (messy code):
    status = 1        # What does 1 mean?? Active? Pending? Error?
    direction = "N"   # Is "N" valid? What about "n" or "North"?

  WITH ENUM (clean code):
    status    = Status.ACTIVE      # Crystal clear!
    direction = Direction.NORTH    # No room for typos!

  WHY USE ENUMS?
  --------------
  ✅ Readable code — names instead of magic numbers
  ✅ Type safety — prevents invalid values
  ✅ Iterable — you can loop through all values
  ✅ Comparable — can use == and 'in' operator
  ✅ Serializable — has .name and .value attributes
  ✅ Works with match/case (Python 3.10+)

  TYPES OF ENUMS IN PYTHON:
  -------------------------
  enum.Enum        → basic enum
  enum.IntEnum     → values are integers (supports int comparison)
  enum.StrEnum     → values are strings (Python 3.11+)
  enum.Flag        → bitwise flags, can be combined with | and &
  enum.IntFlag     → integer-based flag enum
  enum.auto()      → auto-assign integer values

#================================================================================
"""

from enum import Enum, IntEnum, Flag, IntFlag, auto, unique
import enum


# ============================================================
# EXAMPLE 1: Basic Enum
# ============================================================

class Color(Enum):
    """
    A simple color enum.
    Each member has a NAME (RED, GREEN, BLUE) and a VALUE (1, 2, 3).
    """
    RED   = 1
    GREEN = 2
    BLUE  = 3


print("=== Basic Enum ===")
print(Color.RED)           # Color.RED
print(Color.RED.name)      # 'RED'
print(Color.RED.value)     # 1
print(type(Color.RED))     # <enum 'Color'>

# Comparing enums
print(Color.RED == Color.RED)   # True
print(Color.RED == Color.BLUE)  # False
print(Color.RED is Color.RED)   # True (same object, enums are singletons)

# Getting enum by value
print(Color(2))            # Color.GREEN
print(Color["BLUE"])       # Color.BLUE — get by name

# Iterating
print("\nAll Colors:")
for color in Color:
    print(f"  {color.name}: {color.value}")

print()

# ============================================================
# EXAMPLE 2: Status Enum with auto() — auto-assign values
# ============================================================

class OrderStatus(Enum):
    """
    auto() automatically assigns incrementing integer values.
    This saves you from manually numbering: 1, 2, 3, 4...
    """
    PENDING    = auto()   # → 1
    CONFIRMED  = auto()   # → 2
    SHIPPED    = auto()   # → 3
    DELIVERED  = auto()   # → 4
    CANCELLED  = auto()   # → 5
    REFUNDED   = auto()   # → 6


class Order:
    """An order that uses OrderStatus enum for its state."""

    def __init__(self, order_id, product, quantity):
        self.order_id  = order_id
        self.product   = product
        self.quantity  = quantity
        self.status    = OrderStatus.PENDING   # ← start with enum value

    def update_status(self, new_status):
        """
        Only allow valid status transitions.
        Enum makes this clean and readable.
        """
        if not isinstance(new_status, OrderStatus):
            raise TypeError(f"Invalid status. Must be OrderStatus enum.")

        valid_transitions = {
            OrderStatus.PENDING:   [OrderStatus.CONFIRMED, OrderStatus.CANCELLED],
            OrderStatus.CONFIRMED: [OrderStatus.SHIPPED,   OrderStatus.CANCELLED],
            OrderStatus.SHIPPED:   [OrderStatus.DELIVERED],
            OrderStatus.DELIVERED: [OrderStatus.REFUNDED],
        }

        allowed = valid_transitions.get(self.status, [])
        if new_status not in allowed:
            raise ValueError(f"Cannot go from {self.status.name} to {new_status.name}")

        old_status = self.status
        self.status = new_status
        print(f"Order #{self.order_id}: {old_status.name} → {new_status.name}")

    def __str__(self):
        return f"Order #{self.order_id} | {self.product} x{self.quantity} | Status: {self.status.name}"


print("=== OrderStatus Enum ===")
order = Order(1001, "Laptop", 1)
print(order)

order.update_status(OrderStatus.CONFIRMED)
order.update_status(OrderStatus.SHIPPED)
order.update_status(OrderStatus.DELIVERED)

try:
    order.update_status(OrderStatus.PENDING)  # ❌ Invalid transition
except ValueError as e:
    print(f"Error: {e}")

print()

# ============================================================
# EXAMPLE 3: IntEnum — works like integers
# ============================================================

class Priority(IntEnum):
    """
    IntEnum makes enum values behave like integers.
    You can compare them with <, >, sort them, etc.
    Useful for numeric priority/level systems.
    """
    LOW    = 1
    MEDIUM = 2
    HIGH   = 3
    URGENT = 4


print("=== IntEnum: Priority ===")
task_priority = Priority.HIGH

# IntEnum supports integer comparison (regular Enum doesn't!)
print(f"HIGH > LOW?   {Priority.HIGH > Priority.LOW}")    # True
print(f"URGENT == 4?  {Priority.URGENT == 4}")             # True (int comparison)

# Sort a list of tasks by priority
tasks = [
    {"name": "Write report",   "priority": Priority.MEDIUM},
    {"name": "Fix critical bug","priority": Priority.URGENT},
    {"name": "Read emails",    "priority": Priority.LOW},
    {"name": "Team meeting",   "priority": Priority.HIGH},
]

sorted_tasks = sorted(tasks, key=lambda t: t["priority"], reverse=True)
print("\nTasks sorted by priority (highest first):")
for task in sorted_tasks:
    print(f"  [{task['priority'].name:6}] {task['name']}")

print()

# ============================================================
# EXAMPLE 4: Flag Enum — Combine with | (bitwise OR)
# ============================================================

class Permission(Flag):
    """
    Flag enum allows COMBINING values using | (bitwise OR).
    Perfect for permission systems, file modes, settings.

    Each value is a power of 2 (1, 2, 4, 8...) so they can be combined.
    """
    NONE    = 0
    READ    = auto()    # 1  (binary: 001)
    WRITE   = auto()    # 2  (binary: 010)
    EXECUTE = auto()    # 4  (binary: 100)
    DELETE  = auto()    # 8  (binary: 1000)

    # Combined permissions (shortcuts)
    READ_WRITE    = READ | WRITE          # 3
    FULL_ACCESS   = READ | WRITE | EXECUTE | DELETE  # 15


class User:
    def __init__(self, username, permissions: Permission):
        self.username    = username
        self.permissions = permissions

    def can_read(self):
        return Permission.READ in self.permissions

    def can_write(self):
        return Permission.WRITE in self.permissions

    def can_execute(self):
        return Permission.EXECUTE in self.permissions

    def can_delete(self):
        return Permission.DELETE in self.permissions

    def grant(self, perm: Permission):
        self.permissions |= perm   # add permission

    def revoke(self, perm: Permission):
        self.permissions &= ~perm  # remove permission

    def __str__(self):
        return f"User({self.username}) → {self.permissions}"


print("=== Flag Enum: Permissions ===")
# Admin has full access
admin = User("admin", Permission.FULL_ACCESS)
print(f"Admin permissions: {admin}")

# Regular user has read-only
reader = User("tasin", Permission.READ)
print(f"Reader permissions: {reader}")
print(f"  Can read?  {reader.can_read()}")
print(f"  Can write? {reader.can_write()}")

# Grant write permission
reader.grant(Permission.WRITE)
print(f"After granting WRITE: {reader}")
print(f"  Can write? {reader.can_write()}")

# Revoke write
reader.revoke(Permission.WRITE)
print(f"After revoking WRITE: {reader}")

print()

# ============================================================
# EXAMPLE 5: Enum with methods and custom behavior
# ============================================================

class DayOfWeek(Enum):
    """
    Enum with custom methods!
    Enums can have regular methods just like classes.
    """
    MONDAY    = 1
    TUESDAY   = 2
    WEDNESDAY = 3
    THURSDAY  = 4
    FRIDAY    = 5
    SATURDAY  = 6
    SUNDAY    = 7

    def is_weekend(self):
        """Method on an enum — checks if it's a weekend day."""
        return self in (DayOfWeek.SATURDAY, DayOfWeek.SUNDAY)

    def next_day(self):
        """Returns the next day of the week."""
        next_value = (self.value % 7) + 1
        return DayOfWeek(next_value)

    def days_until_weekend(self):
        """How many days until Saturday?"""
        return (DayOfWeek.SATURDAY.value - self.value) % 7


print("=== DayOfWeek Enum with Methods ===")
today = DayOfWeek.WEDNESDAY
print(f"Today: {today.name}")
print(f"Is weekend? {today.is_weekend()}")
print(f"Next day: {today.next_day().name}")
print(f"Days until weekend: {today.days_until_weekend()}")

saturday = DayOfWeek.SATURDAY
print(f"\nSaturday is weekend? {saturday.is_weekend()}")
print(f"Next day after Saturday: {saturday.next_day().name}")

print()

# ============================================================
# EXAMPLE 6: @unique decorator — prevent duplicate values
# ============================================================

try:
    @unique
    class BadEnum(Enum):
        """
        @unique raises ValueError if any two members have the same value.
        Protects against accidental duplicates.
        """
        A = 1
        B = 2
        C = 1   # ❌ Duplicate of A!

except ValueError as e:
    print(f"@unique caught duplicate: {e}")

"""
SUMMARY — ENUM:
#================

BASIC:
  class Color(Enum):
      RED = 1
      GREEN = 2

ACCESS:
  Color.RED           → member
  Color.RED.name      → "RED"
  Color.RED.value     → 1
  Color(1)            → Color.RED (by value)
  Color["RED"]        → Color.RED (by name)

TYPES:
  Enum     → basic named constants
  IntEnum  → values behave as integers (supports int math/comparison)
  Flag     → combine with | operator (bitmasks)
  auto()   → auto-increment values

USE CASES:
  - States (PENDING, ACTIVE, CLOSED)
  - Directions (NORTH, SOUTH, EAST, WEST)
  - Permissions (READ, WRITE, EXECUTE)
  - HTTP methods (GET, POST, PUT, DELETE)
  - Days, Months, Colors, etc.

ADVANTAGES over plain variables/constants:
  - Group related constants together
  - Readable: Status.ACTIVE vs status=1
  - Iterable: for s in Status: ...
  - Prevents invalid values (typo protection)
  - Has .name and .value for display/serialization
"""
