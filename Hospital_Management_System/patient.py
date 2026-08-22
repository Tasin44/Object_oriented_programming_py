"""
FILE: 8_patient.py
ROLE: Represents a Patient -- the central entity of the HMS.
      NOT an Employee. Directly inherits from Person.

OOP CONCEPTS DEMONSTRATED:
    1. Inheritance     -- Patient IS-A Person (skips Employee entirely)
    2. Encapsulation   -- medical_history and billing_amount are private, protected by setters
    3. Composition     -- Patient HAS-A MedicalRecord object inside it

SOLID PRINCIPLE APPLIED HERE: (D) Dependency Inversion Principle
    Patient depends on the abstract MedicalRecord interface, not hard-coded data.

    [DENY] BAD (Tight Coupling) -- Patient stores medical info as plain strings internally:
    # class Patient(Person):
    #     def __init__(self, ...):
    #         self.__medical_history = ""   # Just a string -- how do you add to it cleanly?
    #         self.__symptoms = ""          # Becomes a messy concatenation mess
    #
    # [-] DISADVANTAGE: If you want to add structured data (visit dates, specific symptoms), 
    #    you must completely refactor how __medical_history is stored.
    #    The Patient class has to change every time medical record structure changes.

    [OK] GOOD (Decoupled) -- Patient holds a MedicalRecord OBJECT.
    Medical record structure can evolve freely inside MedicalRecord class
    without ever touching the Patient class.

ENCAPSULATION DEEP DIVE:
    __medical_history  -> Only accessible via get_medical_history() by anyone.
                         Only writable via MedicalRecord methods called by Doctor/CareGiver.
    __billing_amount   -> Only writable via update_bill() where Receptionist is authorized.
                         Patient can view their own bill via view_bill().
"""

from person import Person                # Patient IS-A Person (not Employee!)
from medical_record import MedicalRecord # Patient HAS-A MedicalRecord (Composition)


class Patient(Person):
    """
    Represents a Patient in the hospital.
    The central entity that connects Doctors, CareGivers, Appointments, and Records.

    Inheritance Chain: Patient -> Person (ABC)
    Note: Patient does NOT inherit from Employee -- patients are not staff.
    """

    def __init__(self, name: str, age: int, gender: str, contact: str,
                 person_id: str, patient_id: str, blood_group: str, assigned_doctor=None):
        """
        Creates a Patient object with identity info (from Person) and medical info.

        Args:
            patient_id (str): Unique patient registration number.
            blood_group (str): Blood type (e.g., "A+", "O-").
            assigned_doctor: The Doctor object primarily assigned to this patient (optional).
        """
        # super() calls Person's __init__ for name, age, gender, contact, person_id
        super().__init__(name, age, gender, contact, person_id)

        self.patient_id = patient_id                # Unique patient registration number
        self.blood_group = blood_group              # Blood type for emergency reference
        self.assigned_doctor = assigned_doctor      # The Doctor object assigned to this patient

        # OOP COMPOSITION: Patient HAS-A MedicalRecord
        # We create a MedicalRecord object directly inside the Patient constructor.
        # When a Patient is created, their MedicalRecord is automatically created too.
        self.medical_record = MedicalRecord(patient=self)  # Composition -- tight binding

        # [PRIVATE] PRIVATE ATTRIBUTES -- Protected by Encapsulation
        self.__billing_amount = 0.0                # Private -- only Receptionist can set
        self.__payment_status = "Unpaid"           # Private -- tracks if bill is settled

    # --------------------------
    # OOP: Encapsulation -- Medical History Access
    # --------------------------
    def get_medical_history(self) -> None:
        """
        Public Getter -- Allows anyone to VIEW the patient's medical record.
        The medical_record object itself is semi-public (no underscore),
        but the internal data inside MedicalRecord is controlled by its own methods.
        """
        print(f"\n[RECORD] Medical History for {self.name} (Patient ID: {self.patient_id}):")
        self.medical_record.show_history()   # Delegates display to MedicalRecord class

    # --------------------------
    # OOP: Encapsulation -- Billing (with Authorization Check)
    # --------------------------
    def update_bill(self, requester_role: str, amount: float) -> None:
        """
        Controlled Setter for the private __billing_amount.
        Only a Receptionist is authorized to set/update the bill.
        Encapsulation: The private variable is hidden; access is controlled here.

        Args:
            requester_role (str): Role of whoever is trying to update the bill.
            amount (float): The billing amount to set.
        """
        if requester_role == "Receptionist":                    # Authorization gate
            self.__billing_amount += amount                     # Add to existing bill
            self.__payment_status = "Pending"                   # Mark as pending payment
            print(f"   [MONEY] Bill updated: +${amount:,.2f} | Total: ${self.__billing_amount:,.2f}")
        else:
            print(f"[DENY] ACCESS DENIED: Only Receptionist can update billing. You are '{requester_role}'.")

    def view_bill(self) -> None:
        #❓Do u think it should be named as get_bill? as I'm accessing private method for read purpose? or it is like I can use get or set anything to access private attribute
        '''
        You could name it get_bill(), which is a common naming convention for a "getter". 
        However, a getter usually returns the value (return self.__billing_amount), 
        whereas your view_bill() method seems to just print() the bill directly. 
        Naming it view_bill is actually very appropriate for a method that just prints it out.
        '''

        """
        Patient can view their own bill -- Public Getter for private billing data.
        Patients have READ access to their own billing, but NOT write access.
        """
        print(f"\n[BILLING] Bill for {self.name}:")
        print(f"   Total Amount: ${self.__billing_amount:,.2f}")
        print(f"   Payment Status: {self.__payment_status}")

    def pay_bill(self, amount: float) -> None:
        """
        Patient pays their bill. Reduces the outstanding billing amount.
        If fully paid, the payment status changes to "Paid".

        Args:
            amount (float): The amount the patient is paying now.
        """
        print(f"\n[PAYMENT] {self.name} is paying ${amount:,.2f}...")
        if amount <= 0:
            print("   [DENY] Payment amount must be greater than 0.")
            return
        self.__billing_amount -= amount                         # Deduct from outstanding balance
        if self.__billing_amount <= 0:
            self.__billing_amount = 0                           # Don't go negative
            self.__payment_status = "Paid [OK]"                  # Mark as fully settled
        print(f"   Payment received. Remaining balance: ${self.__billing_amount:,.2f}")
        print(f"   Status: {self.__payment_status}")

    # --------------------------
    # OOP: Abstraction -- Implements required abstract method from Person
    # --------------------------
    def display_role(self) -> str:
        """Patient declares its own role -- implements the abstract method from Person."""
        return f"I am {self.name}, a Patient. Patient ID: {self.patient_id}, Blood Group: {self.blood_group}."

    def __str__(self) -> str:
        """Readable string when print(patient_object) is called."""
        return (f"[Patient] {self.name} | ID: {self.patient_id} "
                f"| Blood Group: {self.blood_group} "
                f"| Doctor: {self.assigned_doctor.name if self.assigned_doctor else 'Not Assigned'}")
