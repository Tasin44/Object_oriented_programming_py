
"""
#================================================================================
  TOPIC 16: MULTIPLE DISPATCH — True Method Overloading (@singledispatchmethod)
#================================================================================

  WHAT IS IT?
  -----------
  We explored Method Overloading earlier. `functools.singledispatchmethod`
  allows true method overloading based on the TYPE of the FIRST argument (other than self).

  It makes code much cleaner than writing a giant `if isinstance(x, int): ... elif ...`

#================================================================================
"""

from functools import singledispatchmethod

class DocumentProcessor:
    """
    A class that processes different types of documents differently.
    """
    
    @singledispatchmethod
    def process(self, document):
        """
        The base implementation. This runs if the type doesn't match any registered types.
        """
        raise NotImplementedError(f"Cannot process document of type {type(document).__name__}")

    # Now we register specific implementations based on the argument type!
    
    @process.register(str)
    def _(self, document):
        # We often use `_` for the method name since it doesn't matter,
        # but it could be named anything.
        print(f"[String Processor] Parsing plain text: '{document[:20]}...'")

    @process.register(list)
    def _(self, document):
        print(f"[List Processor] Processing {len(document)} separate items.")
        for item in document:
            # We can recursively call the dispatcher!
            self.process(item)
            
    @process.register(dict)
    def _(self, document):
        print(f"[Dict Processor] Extracting structured JSON/Dict data. Keys: {list(document.keys())}")


print("=== Multiple Dispatch Method ===")
processor = DocumentProcessor()

# Dispatch based on string
processor.process("Hello world, this is a plain text document.")

print()
# Dispatch based on dict
processor.process({"title": "Annual Report", "year": 2026})

print()
# Dispatch based on list (which recursively dispatches to string and dict)
processor.process([
    "Item 1",
    {"key": "value"}
])

print()
try:
    processor.process(42)
except NotImplementedError as e:
    print(f"Expected Error: {e}")

"""
SUMMARY:
---------
- Use `@singledispatchmethod` to overload class methods based on the first argument's type.
- Use `@method_name.register(Type)` to add specific handlers.
- Keeps code highly modular. No more `isinstance` spaghetti!
"""
