
"""
#================================================================================
  TOPIC 20: STRATEGY PATTERN
#================================================================================

  WHAT IS IT?
  -----------
  The Strategy pattern defines a family of algorithms, encapsulates each one, 
  and makes them interchangeable. Strategy lets the algorithm vary independently 
  from the clients that use it.

  Instead of putting multiple behaviors into a massive `if-elif-else` block, 
  you separate each behavior into its own class (a Strategy).

  REAL-WORLD ANALOGY:
  -------------------
  Think of going to the airport. You have a Navigation App.
  You can get to the airport by:
  - Driving Strategy
  - Walking Strategy
  - Public Transport Strategy
  The App (Context) doesn't care HOW you get there. You just plug in the 
  strategy you want, and the App executes it.

  WHEN TO USE IT:
  ---------------
  - Payment processors (Credit Card, PayPal, Crypto).
  - Sorting algorithms (QuickSort, MergeSort depending on data size).
  - Compression (ZIP, RAR, TAR).

#================================================================================
"""

from abc import ABC, abstractmethod

# ============================================================
# Step 1: Define the Strategy Interface
# ============================================================

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# ============================================================
# Step 2: Define Concrete Strategies
# ============================================================

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        # Complex logic for processing credit card
        print(f"  Paying {amount} BDT using Credit Card ending in {self.card_number[-4:]}")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        # Complex logic for processing PayPal
        print(f"  Paying {amount} BDT using PayPal account {self.email}")


class BkashPayment(PaymentStrategy):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def pay(self, amount):
        # Complex logic for processing bKash
        print(f"  Paying {amount} BDT using bKash number {self.phone_number}")


# ============================================================
# Step 3: Define the Context Class
# ============================================================

class ShoppingCart:
    """
    The Context class. It contains the core logic (adding items, calculating total),
    but delegates the payment algorithm to a Strategy object.
    """
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))
        print(f"Added {name} ({price} BDT) to cart.")

    def calculate_total(self):
        return sum(price for _, price in self.items)

    def checkout(self, payment_strategy: PaymentStrategy):
        """
        We inject the strategy via parameter!
        The ShoppingCart doesn't know HOW the payment works, it just calls .pay()
        """
        total = self.calculate_total()
        print(f"\nChecking out. Total: {total} BDT")
        
        # Delegate the actual payment to the Strategy object
        payment_strategy.pay(total)


print("=== Strategy Pattern ===")

cart = ShoppingCart()
cart.add_item("Mechanical Keyboard", 5000)
cart.add_item("Gaming Mouse", 2500)

# The user chooses to pay with Credit Card
cc_strategy = CreditCardPayment("1234-5678-9012-3456")
cart.checkout(cc_strategy)

print("-" * 40)

# Next time, the user chooses bKash
bkash_strategy = BkashPayment("01711223344")
cart.checkout(bkash_strategy)

"""
SUMMARY:
---------
- We avoided writing a massive `checkout()` method with:
    if method == "credit_card": ...
    elif method == "paypal": ...
    elif method == "bkash": ...
- Each algorithm (strategy) lives in its own class.
- The `ShoppingCart` (Context) simply calls `strategy.pay()`.
- To add a new payment method (e.g. Rocket), we just create a new `RocketPayment` 
  class. We don't have to touch the `ShoppingCart` code at all! (Open/Closed Principle).
"""
