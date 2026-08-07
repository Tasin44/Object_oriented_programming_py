
"""
#================================================================================
  TOPIC 2: AGGREGATION — Weak "Has-A" Relationship
#================================================================================

  WHAT IS AGGREGATION?
  ---------------------
  Aggregation is a WEAKER form of Composition.
  It is also a "Has-A" relationship, but with one key difference:

  ┌────────────────────────────────────────────────────────┐
  │  COMPOSITION  : Child CANNOT exist without Parent      │
  │  AGGREGATION  : Child CAN exist independently          │
  └────────────────────────────────────────────────────────┘

  REAL WORLD ANALOGY:
  -------------------
  🏫 University & Professor:
     - A University HAS Professors (aggregation)
     - If the University closes, the Professors still EXIST
     - The Professor object is created OUTSIDE and passed IN

  ❤️ Human & Heart:
     - A Human HAS a Heart (composition)
     - If the Human dies, the Heart is gone too
     - The Heart is created INSIDE the Human class

  COMPOSITION vs AGGREGATION:
  ---------------------------
  Composition → object created INSIDE the parent class
               → child dies with parent
  Aggregation → object created OUTSIDE and PASSED IN to parent
               → child lives independently

#================================================================================
"""

# ============================================================
# EXAMPLE 1: University and Professors (Aggregation)
# ============================================================

class Professor:
    """
    Professor is an INDEPENDENT object.
    It is NOT created inside University.
    It exists on its own and can be assigned to any university.
    """
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        return f"Prof. {self.name} is teaching {self.subject}"

    def __repr__(self):
        return f"Professor({self.name}, {self.subject})"


class University:
    """
    University HAS-A list of Professors — AGGREGATION.
    Key: Professors are passed IN from outside, not created inside.
    If University is deleted, Professor objects still live in memory.
    """
    def __init__(self, name):
        self.name = name
        self.professors = []   # will hold references to Professor objects

    def hire_professor(self, professor):
        # ✅ AGGREGATION: Professor passed in from outside
        # We just store a REFERENCE, not ownership
        self.professors.append(professor)

    def show_faculty(self):
        print(f"\n=== {self.name} Faculty ===")
        for prof in self.professors:
            print(f"  - {prof.teach()}")

    def fire_professor(self, name):
        # Remove from university but the Professor object still exists!
        self.professors = [p for p in self.professors if p.name != name]
        print(f"Prof. {name} left the university. But they still exist as an object!")


# ✅ Professors are created INDEPENDENTLY (outside University)
prof1 = Professor("Dr. Rahman", "Mathematics")
prof2 = Professor("Dr. Ahmed", "Physics")
prof3 = Professor("Dr. Karim", "Computer Science")

# Now we PASS them into the University (aggregation)
buet = University("BUET")
buet.hire_professor(prof1)
buet.hire_professor(prof2)
buet.hire_professor(prof3)

buet.show_faculty()

# Fire a professor — professor still exists!
buet.fire_professor("Dr. Ahmed")

# Prof2 still exists independently even after leaving the university
print(f"\nProf2 still exists: {prof2}")   # Output: Professor(Dr. Ahmed, Physics)
print(prof2.teach())   # Still works!

print()  # blank line separator

# ============================================================
# EXAMPLE 2: Team and Players (Aggregation)
# ============================================================

class Player:
    """
    Player exists independently.
    A player can be on different teams at different times.
    """
    def __init__(self, name, position, rating):
        self.name = name
        self.position = position   # e.g., "Forward", "Goalkeeper"
        self.rating = rating

    def play(self):
        return f"{self.name} ({self.position}, Rating: {self.rating}) is playing!"


class FootballTeam:
    """
    Team HAS Players — AGGREGATION.
    Players are created outside and passed in.
    Players can leave the team and join another — they exist independently.
    """
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = []   # list of Player references (not ownership)

    def add_player(self, player):
        # AGGREGATION: Just storing reference, not creating
        self.players.append(player)
        print(f"{player.name} joined {self.team_name}!")

    def remove_player(self, player_name):
        self.players = [p for p in self.players if p.name != player_name]

    def show_lineup(self):
        print(f"\n=== {self.team_name} Lineup (Coach: {self.coach}) ===")
        for player in self.players:
            print(f"  • {player.play()}")


# Players created INDEPENDENTLY
messi    = Player("Messi",   "Forward",    99)
ronaldo  = Player("Ronaldo", "Forward",    98)
neuer    = Player("Neuer",   "Goalkeeper", 95)

# Assign to Team A (aggregation — we just pass references)
team_a = FootballTeam("Barcelona FC", "Xavi")
team_a.add_player(messi)
team_a.add_player(neuer)

team_a.show_lineup()

# Ronaldo is in Team B
team_b = FootballTeam("Real Madrid CF", "Ancelotti")
team_b.add_player(ronaldo)
team_b.show_lineup()

# Messi transfers — the Player object is the SAME one!
team_a.remove_player("Messi")
team_b.add_player(messi)  # same messi object, now in team B
print(f"\nAfter transfer:")
team_a.show_lineup()
team_b.show_lineup()

print()  # blank line separator

# ============================================================
# EXAMPLE 3: Order and Customer (Aggregation in E-Commerce)
# ============================================================

class Customer:
    """Customer exists independently from any order."""
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id})"


class Product:
    """Product exists independently."""
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Order:
    """
    Order HAS-A Customer (aggregation) and HAS Products (aggregation).
    The Customer and Products exist outside and are passed in.
    Deleting an Order doesn't delete the Customer.
    """
    def __init__(self, order_id, customer):
        self.order_id = order_id
        # AGGREGATION: Customer passed in, exists independently
        self.customer = customer
        self.items = []    # list of (Product, quantity) tuples

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def get_total(self):
        return sum(p.price * q for p, q in self.items)

    def show_receipt(self):
        print(f"\n=== Order #{self.order_id} ===")
        print(f"Customer: {self.customer.name}")
        for product, qty in self.items:
            print(f"  {product.name} x{qty} = {product.price * qty} BDT")
        print(f"  TOTAL: {self.get_total()} BDT")


# Independent objects created outside
tasin   = Customer(1, "Tasin", "tasin@email.com")
shirt   = Product(101, "Shirt",  500)
laptop  = Product(102, "Laptop", 75000)

# Order aggregates them — Tasin and shirt still exist independently
order1 = Order(1001, tasin)
order1.add_item(shirt, 2)
order1.add_item(laptop, 1)
order1.show_receipt()

# tasin still exists if we delete order1
print(f"\nCustomer still alive: {tasin}")

"""
SUMMARY: COMPOSITION vs AGGREGATION
#=====================================

COMPOSITION (strong HAS-A):
  • Child object created INSIDE the parent
  • Parent OWNS the child (child cannot exist without parent)
  • Example: Car → Engine (engine only exists as part of the car)

AGGREGATION (weak HAS-A):
  • Child object created OUTSIDE and PASSED IN to parent
  • Parent only holds a REFERENCE (child exists independently)
  • Example: University → Professor (professor exists after university closes)

Both are "Has-A" relationships, but differ in LIFETIME dependency.

Inheritance  = IS-A  → Dog is an Animal
Composition  = HAS-A (strong) → Human has a Heart
Aggregation  = HAS-A (weak)   → University has Professors
"""
