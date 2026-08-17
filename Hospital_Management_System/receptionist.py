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

    def cancel_appointment(self, appointment: "Appointment") -> None:
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
