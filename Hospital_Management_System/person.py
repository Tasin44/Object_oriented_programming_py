"""
FILE: 1_person.py
ROLE: Abstract Base Class (ABC) -- The root of the entire HMS class hierarchy.

OOP CONCEPT: Abstraction
    - We define WHAT every person must have (name, age, contact, role),
      but we do NOT implement the full detail here.
    - You CANNOT create a plain "Person" object -- it's just a blueprint.

SOLID PRINCIPLE APPLIED HERE: (I) Interface Segregation Principle
    The ISP says: "A class should not be forced to implement methods it does not need."
    We keep Person's abstract interface MINIMAL -- only things EVERY person truly shares.

    [DENY] BAD (Violating ISP) -- Dumping everything into Person:
    # class Person(ABC):
    #     @abstractmethod
    #     def calculate_bonus(self): pass     # ? Patients don't have bonuses!
    #     @abstractmethod
    #     def book_appointment(self): pass    # ? Admins don't book appointments!
    #     @abstractmethod
    #     def set_diagnosis(self): pass       # ? Only Doctors set diagnosis!
    #
    # [-] DISADVANTAGE: Every class (Patient, Admin, Receptionist) is forced to
    #    implement methods they don't need at all, causing messy, meaningless code.

    [OK] GOOD (Following ISP) -- Keep Person lean. Each subclass adds ONLY what it needs.
"""

from abc import ABC, abstractmethod  # Import ABC toolkit to make abstract classes


class Person(ABC):
    """
    Abstract Base Class: Person
    Every human in the HMS (Doctor, Patient, Admin, etc.) IS-A Person.
    This class defines the shared identity attributes and enforces
    that every subclass declares its own role via display_role().
    """

    def __init__(self, name: str, age: int, gender: str, contact: str, person_id: str):
        # --- Public Attributes (shared identity data) ---
        self.name = name                # Full name of the person (e.g., "Dr. Smith")
        self.age = age                  # Age as an integer (e.g., 35)
        self.gender = gender            # Gender string (e.g., "Male", "Female")
        self.contact = contact          # Contact number or email
        self.person_id = person_id      # Unique ID for every person in the system

    # --- Abstract Method (MUST be overridden by every child class) ---
    @abstractmethod
    def display_role(self) -> str:
        """
        OOP: Abstraction + Polymorphism
        Forces every child class to declare its own role.
        Each class will print a DIFFERENT message -- that's Polymorphism.
        If a child class forgets to implement this, Python will raise a TypeError.
        """
        pass  # No implementation here -- just the blueprint

    # --- Public Method (shared by all, no need to override) ---
    def get_contact_info(self) -> str:
        """
        Returns a formatted string of this person's contact details.
        Public because every role in the system may need to look up contacts.
        """
        return f"Name: {self.name} | Contact: {self.contact} | ID: {self.person_id}"

    # --- Python Special Method (Dunder) ---
    def __str__(self) -> str:
        """
        Called automatically when you print(person_object).
        Returns a clean, readable representation of this person.
        """
        return f"[{self.__class__.__name__}] {self.name} (ID: {self.person_id})"
