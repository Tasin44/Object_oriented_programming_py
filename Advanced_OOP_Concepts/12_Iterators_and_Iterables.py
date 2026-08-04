
"""
================================================================================
  TOPIC 12: ITERATORS & ITERABLES — __iter__ and __next__
================================================================================

  WHAT ARE THEY?
  --------------
  - ITERABLE: Any object you can loop over (like a list, string, dict).
              It MUST implement the `__iter__()` method, which returns an Iterator.
  - ITERATOR: The object that actually does the counting/yielding of values.
              It MUST implement `__next__()` to get the next value, and
              raise `StopIteration` when there are no more values.
              An Iterator must also implement `__iter__()` returning `self`.

  REAL-WORLD ANALOGY:
  -------------------
  Think of a Book (Iterable) and a Bookmark (Iterator).
  - The Book has pages (data). You can get a Bookmark for it (`iter(book)`).
  - The Bookmark remembers which page you are on.
  - You flip to the next page using the Bookmark (`next(bookmark)`).

================================================================================
"""

# ============================================================
# EXAMPLE 1: Creating a Custom Range Iterable
# ============================================================

class MyRangeIterator:
    """
    The Iterator class. It keeps track of the current state.
    """
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        # An iterator must return itself when __iter__ is called
        return self

    def __next__(self):
        # If we reached the end, raise StopIteration to stop the loop
        if self.current >= self.end:
            raise StopIteration
        
        # Get the value to return, then increment state
        value = self.current
        self.current += 1
        return value


class MyRange:
    """
    The Iterable class. It represents the collection.
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # MUST return an Iterator object
        return MyRangeIterator(self.start, self.end)


print("=== Custom Iterable (MyRange) ===")
# Python's 'for' loop automatically calls iter(my_range) to get the iterator,
# and then repeatedly calls next(iterator) until StopIteration is raised.
my_range = MyRange(1, 4)
for num in my_range:
    print(f"Number: {num}")

print()

# ============================================================
# EXAMPLE 2: A simpler approach — combining Iterable and Iterator
# ============================================================

class Countdown:
    """
    Often, classes implement BOTH __iter__ and __next__ in the same class.
    This makes the object both an Iterable AND an Iterator.
    """
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        
        value = self.current
        self.current -= 1
        return value

print("=== Combined Iterable/Iterator ===")
cd = Countdown(3)
for step in cd:
    print(f"Countdown: {step}")

# Note: Once an Iterator is exhausted, you can't loop over it again!
print("\nTrying to loop again...")
for step in cd:
    print(f"Countdown: {step}") # This won't print anything because current <= 0

print()

# ============================================================
# EXAMPLE 3: Infinite Iterators
# ============================================================

class EvenNumbers:
    """
    An iterator can theoretically go on forever if it never raises StopIteration.
    """
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        return self.current

print("=== Infinite Iterator ===")
evens = EvenNumbers()
iterator = iter(evens)

print(f"1st even: {next(iterator)}")
print(f"2nd even: {next(iterator)}")
print(f"3rd even: {next(iterator)}")
print("(We stop manually so we don't loop forever!)")

"""
SUMMARY:
---------
- An Iterable is a collection of items (has __iter__).
- An Iterator is an object that fetches items one by one (has __next__).
- 'for x in obj:' is just syntactic sugar for:
      it = iter(obj)
      while True:
          try:
              x = next(it)
          except StopIteration:
              break
"""
