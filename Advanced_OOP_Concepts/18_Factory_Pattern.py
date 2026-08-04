
"""
================================================================================
  TOPIC 18: FACTORY PATTERN
================================================================================

  WHAT IS IT?
  -----------
  The Factory pattern provides a way to create objects without specifying the 
  exact class of object that will be created. You pass in some data, and the 
  Factory decides which subclass to instantiate and return.

  REAL-WORLD ANALOGY:
  -------------------
  Think of a Logistics Company. You tell them you need to deliver a package 
  by "road" or "sea". You don't build the Truck or the Ship yourself. The 
  Logistics Factory decides whether to dispatch a Truck or a Ship based on 
  your request.

  WHEN TO USE IT:
  ---------------
  - When the exact types and dependencies of the objects you need to create 
    aren't known beforehand.
  - When you want to centralize the object creation logic (to easily add new 
    types later).

================================================================================
"""

# ============================================================
# Step 1: Create the Base Class (Interface)
# ============================================================
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


# ============================================================
# Step 2: Create Concrete Classes (The actual objects)
# ============================================================

class Truck(Transport):
    def deliver(self):
        return "Delivering cargo by ROAD in a Truck."

class Ship(Transport):
    def deliver(self):
        return "Delivering cargo by SEA in a Ship."

class Airplane(Transport):
    def deliver(self):
        return "Delivering cargo by AIR in an Airplane."


# ============================================================
# Step 3: Create the Factory
# ============================================================

class TransportFactory:
    """
    The Factory Class. It has a single responsibility: Create objects.
    """
    @staticmethod
    def create_transport(transport_type):
        """
        Based on the input string, return the correct object.
        """
        # Using a dictionary for clean mapping (avoids giant if-else blocks)
        transports = {
            "road": Truck,
            "sea": Ship,
            "air": Airplane
        }
        
        transport_class = transports.get(transport_type.lower())
        
        if transport_class:
            return transport_class()
        else:
            raise ValueError(f"Unknown transport type: {transport_type}")


print("=== Factory Pattern ===")

# The Client (us) doesn't need to know about Truck, Ship, or Airplane classes directly!
# We just ask the factory for what we need.

road_logistics = TransportFactory.create_transport("road")
print(road_logistics.deliver())

sea_logistics = TransportFactory.create_transport("sea")
print(sea_logistics.deliver())

air_logistics = TransportFactory.create_transport("air")
print(air_logistics.deliver())

print()

try:
    space_logistics = TransportFactory.create_transport("space")
except ValueError as e:
    print(f"Error caught: {e}")

"""
SUMMARY:
---------
- A Factory separates the object *creation* logic from the object *usage* logic.
- Promotes loose coupling: The client code doesn't depend on concrete classes, 
  only on the interface (`Transport`) and the Factory.
- Makes it very easy to add a new type (e.g., `Train`) later: just write the 
  `Train` class and update the Factory's dictionary. Client code remains unchanged!
"""
