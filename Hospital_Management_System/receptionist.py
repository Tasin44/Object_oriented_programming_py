"""
FILE: 7_receptionist.py
ROLE: Represents a Receptionist -- handles scheduling and billing.

OOP CONCEPTS DEMONSTRATED:
    1. Inheritance     -- Receptionist IS-AN Employee IS-A Person
    2. Encapsulation   -- Billing update goes through Patient's private setter
    3. Composition     -- Works with Appointment objects (creates and manages them)
    4. Decoupling      -- Receptionist doesn't reach into Patient's private data directly

SOLID PRINCIPLE APPLIED HERE: (S) Single Responsibility Principle
    Receptionist handles ONLY scheduling and billing -- not medical decisions.
    Doctor handles diagnosis. CareGiver handles vitals. Receptionist handles admin.

DECOUPLING CONCEPT:
    Receptionist creates Appointment objects and calls Patient's billing method.
    It does NOT directly edit Patient's private __billing_amount.
    This keeps Receptionist and Patient classes LOOSELY COUPLED.
    If billing logic changes later, only Patient class needs updating -- not Receptionist.

    [DENY] BAD (Tight Coupling) -- Receptionist directly modifies Patient internals:
    # class Receptionist(Employee):
    #     def generate_bill(self, patient, amount):
    #         patient.__billing_amount = amount    # ? DIRECT access to private data!
    #         patient.__payment_status = "Pending" # ? Receptionist knows too much!
    #
    # [-] DISADVANTAGE: Receptionist is now tightly coupled to Patient's internal
    #    implementation. If Patient changes how it stores billing data,
    #    Receptionist ALSO breaks and must be updated. This is fragile design.

    [OK] GOOD (Decoupled) -- Receptionist calls patient.update_bill(amount).
    Patient's internal billing logic is hidden; Receptionist only sends a signal.


##❓could u plz explain this decoupling concept ?
    Decoupling means reducing the dependencies between different parts (classes) of your system. 
    If the Receptionist class knows too much about how the Appointment class works internally, 
    they are "tightly coupled" (which is bad). 
    By passing the Appointment object itself instead of meddling with its internal variables, 
    we "decouple" them. This makes the code easier to maintain because a change in Appointment won't break Receptionist.


সো ডিকাপলিং এখানে যেভাবে কাজ করছে, রিসিপশনিস্ট ডাইরেক্টলি পেশেন্টের প্রাইভেট ভেরিয়েবল গুলো ইডিট করবে না, সে শুধু  সেই প্রাইভেট ভেরিয়েবল এর উপর কাজ করে এমন মেথড টা কল করবে যেটা কিনা পেশেন্টের মধ্যে ইমপ্লিমেন্টেড হবে, সে শুধু কল করে সিগনাল দিবে, এমন নাকি ডিকাপলিং হয়? 

হ্যাঁ, আপনি একদম ঠিক বুঝেছেন! ১০০% সঠিক।

ডিকাপলিং (Decoupling) এর মূল কনসেপ্টটাই এটাই। আমি আপনাকে আরেকটু সহজ করে এবং একটা রিয়েল-লাইফ উদাহরণের সাহায্যে বুঝিয়ে বলছি:

রিয়েল-লাইফ উদাহরণ: রেস্টুরেন্ট
ধরুন আপনি একটি রেস্টুরেন্টে খেতে গেছেন।

Tight Coupling (বাজে এপ্রোচ): আপনি নিজে রান্নাঘরে ঢুকে, শেফের মশলার বাক্স ঘেঁটে, নিজের খাবার নিজে বানিয়ে নিলেন। এতে সমস্যা হলো—শেফ যদি কালকে মশলার বাক্স অন্য জায়গায় রাখে, আপনি আর খাবার বানাতে পারবেন না। (অর্থাৎ, এক জায়গায় চেঞ্জ হলে অন্য জায়গায় এরর খাবে)।
Decoupling (সঠিক এপ্রোচ): আপনি শুধু ওয়েটারকে বা শেফকে অর্ডার দিলেন (সিগন্যাল দিলেন), "আমাকে একটা বার্গার দিন।" শেফ তার নিজের মতো করে বার্গার বানাবে। সে মশলা কোথায় রাখলো বা কীভাবে বানালো—তা আপনার জানার দরকার নেই।
আপনার কোডের ক্ষেত্রে:
এখানে Receptionist হলেন আপনি, আর Patient হলো সেই শেফ।

Tight Coupling হলে যা হতো: Receptionist ডাইরেক্টলি patient.__billing_amount += 500 করে দিতো। এতে সমস্যা হতো যে, ভবিষ্যতে Patient ক্লাসে যদি বিলিং এর মেকানিজম বা ভেরিয়েবলের নাম পরিবর্তন করা হয়, তাহলে Receptionist ক্লাসও নষ্ট হয়ে যাবে (কোড ব্রেক করবে)।

Decoupling এর কারণে যা হচ্ছে: Receptionist শুধু patient.update_bill(500) মেথডটাকে কল করে একটা সিগন্যাল দিচ্ছে যে, "ভাই, তোমার বিল ৫০০ টাকা আপডেট করো।"

এখন Patient ক্লাসের ভেতরের মেথডটা তার নিজস্ব প্রাইভেট ভেরিয়েবল (__billing_amount) আপডেট করার দায়িত্ব পালন করছে। Receptionist-এর এটা জানার কোনো দরকার নেই যে Patient ভেতরে ভেতরে কীভাবে বিলটা সেভ করে রাখছে।

এর সবচেয়ে বড় সুবিধা হলো: ভবিষ্যতে যদি Patient ক্লাসে বিলিং এর নিয়মে কোনো পরিবর্তন আসে (যেমন, হয়তো বিলে ট্যাক্স যোগ করতে হবে), তখন শুধু Patient ক্লাসের update_bill মেথডটা আপডেট করলেই হবে। Receptionist ক্লাসে হাত দেওয়ার কোনো প্রয়োজনই পড়বে না।

এর মাধ্যমেই দুটি ক্লাস একে অপরের উপর থেকে নির্ভরশীলতা (Dependency) কমায়, আর এটাকেই অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং (OOP)-এ Decoupling বা Loose Coupling বলা হয়। আপনি কনসেপ্টটা একদম পারফেক্টলি ধরতে পেরেছেন!
"""

from employee import Employee                # Receptionist IS-AN Employee
from appointment import Appointment         # Receptionist creates Appointment objects


class Receptionist(Employee):
    """
    Represents a Hospital Receptionist.
    Manages patient appointments and billing -- the front desk operations.

    Inheritance Chain: Receptionist -> Employee -> Person (ABC)
    """

    def __init__(self, name: str, age: int, gender: str, contact: str,
                 person_id: str, employee_id: str, department: str, salary: float):
        """All attributes are inherited -- no new Receptionist-specific attributes needed."""
        super().__init__(name, age, gender, contact, person_id,
                         employee_id, department, salary)

        # The receptionist manages the hospital's appointment book
        self.__appointment_registry = []       # [PRIVATE] PRIVATE -- master list of appointments

    # --------------------------
    # Appointment Management
    # --------------------------
    def book_appointment(self, patient, doctor, time_slot: str) -> "Appointment":
        """
        Creates a new Appointment object linking a Patient to a Doctor at a time slot.
        Composition: An Appointment object is created and CONTAINS references to
        the Doctor and Patient objects. This is the Has-A relationship.

        Args:
            patient: The Patient object requesting the appointment.
            doctor: The Doctor object being assigned.
            time_slot (str): The date/time string (e.g., "2026-08-20 10:00 AM").

        Returns:
            Appointment: The newly created Appointment object.
        """
        print(f"\n[CALENDAR] {self.name} booking appointment...")
        # Create a new Appointment object -- this is Composition (Appointment HAS a Doctor and Patient)
        new_appointment = Appointment(doctor=doctor, patient=patient, time_slot=time_slot)
        self.__appointment_registry.append(new_appointment)  # Add to registry list
        print(f"   [OK] Appointment booked: {patient.name} -> Dr. {doctor.name} at {time_slot}")
        return new_appointment      # Return the object so the caller can reference it

    def cancel_appointment(self, appointment: "Appointment") -> None:#❓what does here appointment:"Appointment" means
        """
        Cancels an appointment by changing its status to 'Cancelled'.

        Decoupling: Receptionist doesn't delete the appointment from memory.
        It calls mark_cancelled() on the Appointment object -- single responsibility.

        Args:
            appointment: The Appointment object to cancel.
        """
        appointment.mark_cancelled()          # Delegates status change to Appointment class
        print(f"   [DENY] Appointment cancelled for {appointment.patient.name}.")

    def view_all_appointments(self) -> None:
        """Prints all appointments in the registry (the full hospital schedule)."""
        print(f"\n--- [RECORD] Full Appointment Registry ---")
        if not self.__appointment_registry:
            print("  No appointments booked yet.")
            return
        for index, appt in enumerate(self.__appointment_registry, 1):
            print(f"  {index}. {appt}")   # Calls Appointment's __str__ method

    def get_appointment_registry(self) -> list:
        """
        Returns the appointment list -- used by Doctor to filter its own appointments.
        Encapsulation: Returns the list but the private attribute stays protected.
        """
        return self.__appointment_registry     # Return the private registry list

    # --------------------------
    # Billing Management
    # --------------------------
    def generate_bill(self, patient, doctor) -> None:
        """
        Calculates and applies a bill to the patient.
        Decoupling: Does NOT directly set patient's __billing_amount.
        Instead, calls patient.update_bill() -- a controlled public method.

        Args:
            patient: The Patient object to bill.
            doctor: The treating Doctor (needed to get consultation fee).
        """
        print(f"\n[RECEIPT] {self.name} generating bill for {patient.name}...")
        total_amount = doctor.consultation_fee              # Bill = doctor's consultation fee
        # Call Patient's controlled public method -- Encapsulation + Decoupling
        patient.update_bill(requester_role="Receptionist", amount=total_amount)
        print(f"   Bill of ${total_amount:,.2f} generated for {patient.name}.")

    # --------------------------
    # OOP: Abstraction -- Implements required abstract method from Person
    # --------------------------
    def display_role(self) -> str:
        """Receptionist declares its own role -- required by the abstract Person blueprint."""
        return f"I am {self.name}, the Hospital Receptionist."

    def __str__(self) -> str:
        """Readable string when print(receptionist_object) is called."""
        return f"[Receptionist] {self.name} | Department: {self.department}"
