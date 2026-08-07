
"""
#================================================================================
  TOPIC 11: CONTEXT MANAGERS — __enter__ and __exit__
#================================================================================

  WHAT IS A CONTEXT MANAGER?
  ---------------------------
  A context manager is an object that manages setup and cleanup of resources.
  You use them with the  "with"  statement.

  You've used them already with files:
    with open("file.txt") as f:    ← this uses context manager!
        data = f.read()
    # File is automatically closed here — even if an error occurs!

  WITHOUT context manager (dangerous):
    f = open("file.txt")
    data = f.read()
    # What if an error happens here? File stays open! → memory/resource leak
    f.close()

  THE "with" STATEMENT:
  ----------------------
    with MyContextManager() as cm:
        # do stuff
    # cleanup happens automatically here

  WHAT HAPPENS INTERNALLY:
  -------------------------
    1. __enter__() is called → sets up resource, returns value for "as"
    2. Your code runs inside the "with" block
    3. __exit__() is called → cleans up, even if an exception occurred!

  __exit__ PARAMETERS:
  ---------------------
    def __exit__(self, exc_type, exc_val, exc_tb):
        exc_type → type of exception (None if no exception)
        exc_val  → the exception instance (None if no exception)
        exc_tb   → traceback object (None if no exception)
        return True  → suppress the exception
        return False → let the exception propagate

#================================================================================
"""

import time
import sqlite3
import os


# ============================================================
# EXAMPLE 1: Simple Timer Context Manager
# ============================================================

class Timer:
    """
    Context manager that measures how long a block of code takes.

    Usage:
        with Timer() as t:
            # your code
        print(t.elapsed)
    """

    def __enter__(self):
        """
        Called when entering the 'with' block.
        Sets up the timer and returns 'self' so we can access elapsed later.
        'as t' captures whatever __enter__ returns.
        """
        self.start_time = time.time()
        self.elapsed    = None
        print(f"⏱  Timer started...")
        return self    # This is what "as t" receives

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Called when leaving the 'with' block (always called — even on error).
        exc_type, exc_val, exc_tb are None if no exception occurred.
        """
        self.elapsed = time.time() - self.start_time

        if exc_type is None:
            # No exception occurred
            print(f"⏱  Timer stopped. Elapsed: {self.elapsed:.4f} seconds")
        else:
            # An exception occurred — still report time, then let error propagate
            print(f"⏱  Timer stopped (with error). Elapsed: {self.elapsed:.4f} seconds")

        return False   # Don't suppress any exceptions — let them propagate


print("=== Timer Context Manager ===")
with Timer() as t:
    # Simulate some work
    total = sum(i**2 for i in range(500_000))
    print(f"Computed sum: {total}")

print(f"Elapsed (accessed after block): {t.elapsed:.4f}s")

print()

# ============================================================
# EXAMPLE 2: File Writer Context Manager
# ============================================================

class ManagedFile:
    """
    Custom file manager — works like the built-in open().
    Demonstrates the typical resource management pattern.
    """

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode     = mode
        self.file     = None

    def __enter__(self):
        """Open the file and return the file object."""
        print(f"📂 Opening file: {self.filename} (mode={self.mode})")
        self.file = open(self.filename, self.mode, encoding='utf-8')
        return self.file   # "as f" receives the file object

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Always close the file, even if an exception occurred."""
        if self.file:
            self.file.close()
            print(f"📂 File closed: {self.filename}")

        if exc_type is not None:
            print(f"❌ Exception during file operation: {exc_val}")

        return False   # propagate any exception


print("=== ManagedFile Context Manager ===")
# Write to a temp file
temp_file = "temp_context_test.txt"

with ManagedFile(temp_file, 'w') as f:
    f.write("Hello from context manager!\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
    print("Wrote 3 lines to file.")

# Read from it
with ManagedFile(temp_file, 'r') as f:
    content = f.read()
    print(f"Read content:\n{content}")

# Cleanup
os.remove(temp_file)

print()

# ============================================================
# EXAMPLE 3: Database Connection Manager
# ============================================================

class DatabaseManager:
    """
    Real-world context manager for SQLite database connections.
    Automatically commits on success and rolls back on failure.
    """

    def __init__(self, db_path):
        self.db_path    = db_path
        self.connection = None
        self.cursor     = None

    def __enter__(self):
        """Open connection and return cursor."""
        print(f"🔌 Connecting to database: {self.db_path}")
        self.connection = sqlite3.connect(self.db_path)
        self.cursor     = self.connection.cursor()
        return self.cursor   # "as cursor" gets this

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Commit on success, rollback on failure, always close."""
        if exc_type is None:
            # No exception — commit the transaction
            self.connection.commit()
            print("✅ Transaction committed successfully")
        else:
            # Exception occurred — rollback to undo changes
            self.connection.rollback()
            print(f"❌ Error: {exc_val}")
            print("↩️  Transaction rolled back")

        self.connection.close()
        print("🔌 Database connection closed")
        return False   # propagate the exception


print("=== DatabaseManager Context Manager ===")
db_file = ":memory:"   # in-memory SQLite (no file created)

# Successful transaction
with DatabaseManager(db_file) as cursor:
    cursor.execute("CREATE TABLE users (id INTEGER, name TEXT, age INTEGER)")
    cursor.execute("INSERT INTO users VALUES (1, 'Tasin', 24)")
    cursor.execute("INSERT INTO users VALUES (2, 'Mahmud', 23)")
    print("Rows inserted.")

print()

# ============================================================
# EXAMPLE 4: Retry / Suppressor Context Manager
# ============================================================

class SuppressErrors:
    """
    Context manager that suppresses specific exception types.
    Similar to Python's built-in contextlib.suppress()

    Usage:
        with SuppressErrors(ValueError, KeyError):
            risky_code()
        # execution continues even if ValueError/KeyError is raised!
    """

    def __init__(self, *exception_types):
        """Accept any number of exception types to suppress."""
        self.exception_types = exception_types

    def __enter__(self):
        return self   # can ignore — we return self for convenience

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Return True to SUPPRESS the exception (don't propagate).
        Return False to let it propagate.
        Check if exc_type is one we want to suppress.
        """
        if exc_type is not None and issubclass(exc_type, self.exception_types):
            print(f"⚠️  Suppressed {exc_type.__name__}: {exc_val}")
            return True   # ← True = suppress (swallow the error)
        return False      # ← False = let other errors through


print("=== SuppressErrors Context Manager ===")

# Without SuppressErrors — code stops at error
print("With suppressor:")
with SuppressErrors(ValueError, KeyError):
    data = {"name": "Tasin"}
    print(f"Name: {data['name']}")
    print(int("not-a-number"))    # raises ValueError → suppressed!
    print("This line won't be reached")

print("Execution continues after with block! ✅")

# Errors NOT in suppression list still propagate
print("\nOther errors still propagate:")
try:
    with SuppressErrors(ValueError):
        raise TypeError("This is NOT suppressed!")
except TypeError as e:
    print(f"TypeError propagated: {e}")

print()

# ============================================================
# EXAMPLE 5: Context Manager using contextlib.contextmanager (Generator Style)
# ============================================================

from contextlib import contextmanager

"""
contextlib.contextmanager lets you write context managers
as simple GENERATOR functions instead of classes.
This is often simpler for straightforward cases.
"""

@contextmanager
def managed_indent(prefix="  "):
    """
    Context manager using generator syntax.
    Everything BEFORE yield → __enter__
    yield → the value returned to "as"
    Everything AFTER yield → __exit__
    """
    print(f"Entering indented section:")
    try:
        yield prefix   # This is what "as p" receives
        print(f"Exiting indented section cleanly.")
    except Exception as e:
        print(f"Error inside indented section: {e}")
        raise   # re-raise the exception


@contextmanager
def temp_config(settings_dict, **overrides):
    """
    Temporarily override settings, then restore them.
    Very useful for testing!
    """
    original = {k: settings_dict.get(k) for k in overrides}
    settings_dict.update(overrides)    # apply overrides
    try:
        yield settings_dict
    finally:
        # Restore original values (runs even on exception)
        for k, v in original.items():
            if v is None:
                settings_dict.pop(k, None)
            else:
                settings_dict[k] = v


print("=== @contextmanager (Generator Style) ===")
with managed_indent(">>> ") as prefix:
    print(f"{prefix}Line 1 inside block")
    print(f"{prefix}Line 2 inside block")

print()

# Temporary config override
app_config = {"debug": False, "host": "localhost", "port": 8000}
print(f"Before: {app_config}")

with temp_config(app_config, debug=True, port=9999) as cfg:
    print(f"During: {cfg}")   # debug=True, port=9999

print(f"After:  {app_config}")   # restored to original!

print()

# ============================================================
# EXAMPLE 6: Nested Context Managers
# ============================================================

print("=== Nested Context Managers ===")

with Timer() as outer:
    print("  Outer block started")

    with Timer() as inner:
        time.sleep(0.01)   # simulate work
        print("  Inner block done")

    print(f"  Inner elapsed: {inner.elapsed:.4f}s")

print(f"Outer elapsed: {outer.elapsed:.4f}s")

# You can also use multiple context managers on one line:
print("\nMultiple on one line:")
temp1 = "temp1.txt"
temp2 = "temp2.txt"

with open(temp1, 'w') as f1, open(temp2, 'w') as f2:
    f1.write("File 1")
    f2.write("File 2")
    print("Both files written!")

os.remove(temp1)
os.remove(temp2)

"""
SUMMARY — CONTEXT MANAGERS:
#==============================

IMPLEMENT A CONTEXT MANAGER:

Method 1: Class-based
  class MyManager:
      def __enter__(self):
          # setup code
          return something    # "as x" receives this

      def __exit__(self, exc_type, exc_val, exc_tb):
          # cleanup code
          return False        # False = propagate exceptions
                              # True  = suppress exceptions

Method 2: Generator (simpler)
  from contextlib import contextmanager
  @contextmanager
  def my_manager():
      # setup
      try:
          yield value         # "as x" receives this
      finally:
          # cleanup (always runs!)

COMMON USE CASES:
  - File operations           → auto close
  - Database connections      → auto commit/rollback/close
  - Network connections       → auto disconnect
  - Locks / threading         → auto release lock
  - Timer / profiling         → measure elapsed time
  - Temporary settings        → restore original values
  - Testing mocks             → restore original state

WHY USE IT:
  ✅ Guaranteed cleanup (even if exception occurs)
  ✅ Cleaner code (no need for try/finally everywhere)
  ✅ Resources never leak
"""
