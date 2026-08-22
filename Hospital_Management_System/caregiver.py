"""
FILE: 5_caregiver.py
ROLE: Represents a Nurse/CareGiver -- an Employee focused on daily patient care.

OOP CONCEPTS DEMONSTRATED:
    1. Inheritance     -- CareGiver IS-AN Employee IS-A Person
    2. Method Overriding -- calculate_bonus() uses shift-based logic (different from Doctor)
    3. Encapsulation   -- shift and ward data managed via methods

SOLID PRINCIPLE: (O) Open/Closed -- Once again demonstrating that adding a new employee type
    (CareGiver) did NOT require modifying the Employee class at all.
    We just extended it by creating a new subclass.

KISS PRINCIPLE:
    CareGiver is kept simple. It has exactly the responsibilities a nurse has --
    recording vitals and updating daily care notes. Nothing more.
"""

from employee import Employee   # CareGiver IS-AN Employee


class CareGiver(Employee):
    """
    Represents a Nurse or CareGiver in the hospital.
    Responsible for daily patient care, recording vitals, and care notes.

    Inheritance Chain: CareGiver -> Employee -> Person (ABC)
    """

    def __init__(self, name: str, age: int, gender: str, contact: str,
                 person_id: str, employee_id: str, department: str, salary: float,
                 shift_timings: str, assigned_ward: str):
        """
        Calls Employee's __init__ via super(), then adds CareGiver-specific data.

        Args:
            shift_timings (str): Work shift (e.g., "Morning 8AM-4PM", "Night 10PM-6AM")
            assigned_ward (str): The ward this nurse is responsible for (e.g., "Ward A")
        """
        super().__init__(name, age, gender, contact, person_id,
                         employee_id, department, salary)

        self.shift_timings = shift_timings          # Nurse's work shift schedule
        self.assigned_ward = assigned_ward          # Hospital ward they manage
        self.__night_shift_count = 0                # [PRIVATE] PRIVATE -- tracks night shifts done

    # --------------------------
    # OOP: Method Overriding (Polymorphism)
    # --------------------------
    def calculate_bonus(self) -> float:
        """
        Overrides Employee's calculate_bonus() with nurse-specific logic.
        Nurse bonus = flat $50 per night shift completed.

        OOP Polymorphism: When you have a list of Employees (some are Doctors,
        some are CareGivers), calling calculate_bonus() on each automatically
        picks the RIGHT version for each object type. This is runtime polymorphism.
        """
        bonus = self.__night_shift_count * 50       # $50 per night shift
        print(f"  Bonus for {self.name} (CareGiver): ${bonus:,.2f} "
              f"({self.__night_shift_count} night shifts ? $50)")
        return bonus

    def log_night_shift(self) -> None:
        """
        Records that this caregiver completed a night shift.
        Increments the private counter used for bonus calculation.
        Encapsulation: The count is private and can only increase via this method.
        """
        self.__night_shift_count += 1
        print(f"  Night shift logged for {self.name}. Total: {self.__night_shift_count}")

    # --------------------------
    # CareGiver's Core Medical Responsibilities
    # --------------------------
    def update_patient_vitals(self, patient, blood_pressure: str, temperature: float) -> None:
        """
        Records daily vital signs for a patient.
        CareGivers monitor patients; they don't diagnose (that's the Doctor's job -- SRP).

        Args:
            patient: The Patient object whose vitals are being recorded.
            blood_pressure (str): Blood pressure reading (e.g., "120/80 mmHg").
            temperature (float): Body temperature in Celsius.
        """
        print(f"\n[HOSPITAL] {self.name} updating vitals for {patient.name}...")
        # Record the vitals in the patient's medical record
        patient.medical_record.add_visit(
            date="Today",
            symptom=f"Vitals Check",
            treatment=f"BP: {blood_pressure} | Temp: {temperature}degC"
        )
        print(f"   Vitals recorded -- BP: {blood_pressure}, Temp: {temperature}degC")

    def add_care_note(self, patient, note: str) -> None:
        """
        Adds a daily care note to the patient's medical record.
        Useful for tracking patient progress, moods, or eating habits.

        Args:
            patient: The Patient object.
            note (str): A text note about the patient's condition.
        """
        print(f"[RECORD] {self.name} adding care note for {patient.name}...")
        patient.medical_record.add_visit(
            date="Today",
            symptom="Care Note",
            treatment=note                         # The note is stored as a treatment entry#❓ from where this note is coming 
        )
        '''
        The note is coming from the arguments of the function itself! 
        Look at line 95: def add_care_note(self, patient, note: str) -> None:. 
        When someone calls caregiver.add_care_note(patient, "Ate lunch well"), 
        that string "Ate lunch well" is passed into the note variable, which you are then using here.

        '''
        print(f"   Care note added: '{note}'")

    # --------------------------
    # OOP: Abstraction -- Implements required abstract method from Person
    # --------------------------
    def display_role(self) -> str:
        """Declares this person's role -- required by the abstract Person blueprint."""
        return f"I am {self.name}, a CareGiver assigned to {self.assigned_ward} ({self.shift_timings} shift)."

    def __str__(self) -> str:
        """Readable string when print(caregiver_object) is called."""
        return (f"[CareGiver] {self.name} | Ward: {self.assigned_ward} "
                f"| Shift: {self.shift_timings}")
