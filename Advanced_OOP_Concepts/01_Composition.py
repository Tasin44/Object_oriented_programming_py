
"""
#================================================================================
  TOPIC 1: COMPOSITION — "Has-A" Relationship
#================================================================================

  WHAT IS COMPOSITION?
  ---------------------
  Composition is when a class CONTAINS an instance of another class as an
  attribute — instead of inheriting from it.

  Two types of relationships in OOP:
  ├── IS-A Relationship → Inheritance (Dog IS-A Animal)
  └── HAS-A Relationship → Composition (Car HAS-A Engine)

  REAL WORLD ANALOGY:
  -------------------
  Think of a Computer:
    - A Computer HAS-A CPU
    - A Computer HAS-A RAM
    - A Computer HAS-A HardDisk
  The Computer does not "inherit" from CPU — it OWNS a CPU object.

  WHY USE COMPOSITION OVER INHERITANCE?
  ---------------------------------------
  "Favor composition over inheritance" — famous OOP design principle.
  ✅ More flexible — you can swap parts (e.g., different Engine types)
  ✅ Avoids tight coupling between classes
  ✅ Easier to maintain and test
  ✅ Avoids the "fragile base class" problem

  KEY RULE:
  ---------
  In Composition: If the PARENT is destroyed, the CHILD is also destroyed.
  Example: If a Human object is deleted, its Heart object is also gone.
  (Compare this to Aggregation where the child lives independently)
#================================================================================
"""

# ============================================================
# EXAMPLE 1: Simple Composition — Engine inside Car
# ============================================================

# Step 1: Define the "component" class (the part being included)
class Engine:
    """
    Engine is a standalone class.
    But it will be COMPOSED inside a Car.
    """
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower    # e.g., 200
        self.fuel_type = fuel_type      # e.g., "Petrol"

    def start(self):
        return f"Engine started! ({self.horsepower}HP, {self.fuel_type})"

    def stop(self):
        return "Engine stopped."


# Step 2: Define the "container" class (the class that OWNS the component)
class Car:
    """
    Car HAS-A Engine (composition).
    Notice: Car does NOT inherit from Engine.
    Instead, it creates an Engine object inside itself.
    """
    def __init__(self, brand, model, horsepower, fuel_type):
        self.brand = brand
        self.model = model
        # ✅ COMPOSITION: Car CONTAINS an Engine object
        self.engine = Engine(horsepower, fuel_type)

    def start_car(self):
        # Car delegates the "start" action to its Engine component
        engine_status = self.engine.start()
        return f"{self.brand} {self.model} is ready! {engine_status}"

    def stop_car(self):
        return self.engine.stop()

    def get_info(self):
        return (f"Car: {self.brand} {self.model} | "
                f"Engine: {self.engine.horsepower}HP, {self.engine.fuel_type}")


# Using composition
my_car = Car("Toyota", "Supra", 250, "Petrol")
print(my_car.start_car())
print(my_car.stop_car())
print(my_car.get_info())

print()  # blank line separator

# ============================================================
# EXAMPLE 2: Human Body Composition
# ============================================================

class Heart:
    """
    The Heart is a component — it will live INSIDE a Human.
    If the Human object is deleted, the Heart goes with it.
    This is TRUE COMPOSITION (child does not exist without parent).
    """
    def __init__(self, rate):
        self.rate = rate  # beats per minute

    def beat(self):
        return f"Heart beating at {self.rate} BPM"


class Brain:
    def __init__(self, iq):
        self.iq = iq

    def think(self):
        return f"Brain thinking... IQ: {self.iq}"


class Human:
    """
    Human HAS-A Heart and HAS-A Brain (both created INSIDE Human).
    Human does NOT inherit from Heart or Brain.
    This is Composition — Human 'owns' these objects.
    """
    def __init__(self, name, heart_rate, iq):
        self.name = name
        # ✅ COMPOSITION: Human creates and owns Heart and Brain
        self.heart = Heart(heart_rate)
        self.brain = Brain(iq)

    def live(self):
        heart_status = self.heart.beat()
        brain_status = self.brain.think()
        return f"{self.name}: {heart_status} | {brain_status}"


person = Human("Tasin", 72, 130)
print(person.live())

print()  # blank line separator

# ============================================================
# EXAMPLE 3: Composition with Multiple Components — Library System
# ============================================================

class Address:
    """Address is a component used inside Person/Library."""
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def full_address(self):
        return f"{self.street}, {self.city}, {self.country}"


class Book:
    """Book is a component held by Library."""
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f'"{self.title}" by {self.author} ({self.pages} pages)'


class Library:
    """
    Library HAS-A Address (one address object).
    Library HAS many Books (a list of Book objects).
    This is composition — Library owns and controls them.
    """
    def __init__(self, name, street, city, country):
        self.name = name
        # ✅ Composition: Library owns one Address object
        self.address = Address(street, city, country)
        # ✅ Composition: Library owns a collection of Book objects
        self.books = []

    def add_book(self, title, author, pages):
        # Library creates and stores the Book — it owns it
        new_book = Book(title, author, pages)
        self.books.append(new_book)
        return f'Book added: "{title}"'

    def show_all_books(self):
        if not self.books:
            return "No books in the library."
        print(f"\n=== {self.name} Book Collection ===")
        for i, book in enumerate(self.books, 1):
            print(f"  {i}. {book.info()}")

    def show_location(self):
        return f"{self.name} is located at: {self.address.full_address()}"


dhaka_library = Library("Dhaka Public Library", "Mirpur Road", "Dhaka", "Bangladesh")
print(dhaka_library.add_book("Clean Code", "Robert C. Martin", 431))
print(dhaka_library.add_book("Python Crash Course", "Eric Matthes", 544))
print(dhaka_library.add_book("Design Patterns", "Gang of Four", 395))
dhaka_library.show_all_books()
print(dhaka_library.show_location())

print()  # blank line separator

# ============================================================
# COMPOSITION vs INHERITANCE COMPARISON
# ============================================================

print("=== COMPOSITION vs INHERITANCE ===")

# ❌ Bad Inheritance approach (Car should NOT inherit from Engine)
class BadEngineInheritance:
    def start(self):
        return "Engine started"

class BadCarInheritance(BadEngineInheritance):
    """
    ❌ WRONG: Car IS-A Engine? That makes no sense!
    A Car is not a type of Engine. This breaks the IS-A rule.
    """
    pass

# ✅ Good Composition approach (Car HAS-A Engine)
class GoodEngine:
    def start(self):
        return "Engine started"

class GoodCar:
    """
    ✅ CORRECT: Car HAS-A Engine. Composition is the right choice here.
    """
    def __init__(self):
        self.engine = GoodEngine()  # composition

    def start(self):
        return self.engine.start()

good_car = GoodCar()
print(good_car.start())

"""
SUMMARY:
---------
Composition = HAS-A Relationship
- The inner object (Engine) is CREATED INSIDE and OWNED by the outer class (Car)
- If Car is deleted, Engine is also deleted
- More flexible than inheritance
- Use when: objects are parts/components of another object

Golden Rule:
  Use INHERITANCE when: Dog IS-A Animal (true type relationship)
  Use COMPOSITION when: Car HAS-A Engine (ownership relationship)
"""
