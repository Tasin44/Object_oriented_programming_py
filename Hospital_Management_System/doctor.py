"""
FILE: 4_doctor.py
ROLE: Represents a Doctor -- a specialized Employee with medical capabilities.

OOP CONCEPTS DEMONSTRATED:
    1. Inheritance     -- Doctor IS-AN Employee IS-A Person (3-level chain)
    2. Method Overriding -- Overrides calculate_bonus() with its own logic
    3. Encapsulation   -- Medical actions are controlled via public methods

SOLID PRINCIPLE APPLIED HERE: (L) Liskov Substitution Principle
    The LSP says: "A subclass object should be usable wherever its parent is used,
    WITHOUT breaking the application."
    A Doctor IS-AN Employee. So anywhere Employee is expected, Doctor must work fine.

    [DENY] BAD (Violating LSP) -- Subclass breaks parent's contract:
    # class Employee:
    #     def calculate_bonus(self) -> float:
    #         return self.salary * 0.05   # always returns a float
    #
    # class Doctor(Employee):
    #     def calculate_bonus(self):
    #         raise NotImplementedError("Doctors don't get bonuses!")  # ? CRASH!
    #         # OR returns a string instead of float -- breaks calling code
    #
    # [-] DISADVANTAGE: Any code that loops through employees and calls
    #    calculate_bonus() will crash when it hits a Doctor. The subclass
    #    is NOT a safe substitute for the parent -- this breaks the entire system.

    [OK] GOOD (Following LSP) -- Doctor overrides calculate_bonus() but still returns
    a proper float value. The calling code works identically for ALL employee types.

SOLID PRINCIPLE APPLIED HERE: (S) Single Responsibility Principle
    Doctor only handles MEDICAL responsibilities (diagnosis, prescriptions, results).
    It does NOT handle billing, scheduling, or HR -- those belong in other classes.
"""

from employee import Employee      # Doctor IS-AN Employee


class Doctor(Employee):
    """
    Represents a Doctor in the hospital.
    Inherits from Employee (which inherits from Person) -- 3-level inheritance chain.

    Inheritance Chain: Doctor -> Employee -> Person (ABC)
    """

    def __init__(self, name: str, age: int, gender: str, contact: str,
                 person_id: str, employee_id: str, department: str, salary: float,
                 specialization: str, consultation_fee: float):
        """
        Calls Employee's __init__ via super() to inherit all employee attributes,
        then adds Doctor-specific attributes.
        """
        # super() calls Employee's __init__, which in turn calls Person's __init__
        super().__init__(name, age, gender, contact, person_id,
                         employee_id, department, salary)

        self.specialization = specialization        # Medical area (e.g., "Cardiologist")
        self.consultation_fee = consultation_fee    # Fee per patient visit
        self.__patient_count = 0                    # [PRIVATE] PRIVATE -- tracks patients seen today

    # --------------------------
    # OOP: Method Overriding (Polymorphism)
    # --------------------------
    def calculate_bonus(self) -> float:
        """
        Overrides Employee's calculate_bonus() with Doctor-specific logic.
        Doctor's bonus = consultation_fee ? patients_seen_this_month.

        OOP: Polymorphism -- calling calculate_bonus() on a list of mixed Employees
             will call THIS version for Doctor objects automatically.
        """
        # Doctor bonus: 20% of salary + $10 per patient seen
        bonus = (self.get_salary() * 0.20) + (self.__patient_count * 10)
        print(f"  Bonus for Dr. {self.name} (Doctor): ${bonus:,.2f} "
              f"(20% salary + $10 ? {self.__patient_count} patients)")
        return bonus

    # --------------------------
    # Medical Methods (Doctor's Core Responsibilities)
    # --------------------------
    def diagnose_patient(self, patient, symptom: str, disease: str) -> None:
        """
        Doctor adds a diagnosis to the patient's Medical Record.

        Decoupling: Doctor doesn't directly modify Patient's private attributes.
        Instead, it calls a controlled method on the MedicalRecord object.
        This keeps Doctor and Patient LOOSELY COUPLED.

        Args:
            patient: A Patient object to diagnose.
            symptom (str): What the patient is complaining about.
            disease (str): Doctor's diagnosis conclusion.
        """
        print(f"\n[DIAGNOSE] Dr. {self.name} is diagnosing {patient.name}...")
        # Access the patient's medical record object and call its add_visit method
        patient.medical_record.add_visit(
            date="Today",                           # In a real app, use datetime.now()
            symptom=symptom,
            treatment=f"Diagnosis: {disease}"      # Record the diagnosis as treatment
        )
        self.__patient_count += 1                  # Increment private patient counter
        print(f"   Diagnosis recorded: {disease} for patient {patient.name}")

    def prescribe_medicine(self, patient, medicine: str) -> None:
        """
        Doctor adds a prescription to the patient's Medical Record.

        Args:
            patient: A Patient object to prescribe to.
            medicine (str): Name of the medicine and dosage.
        """
        print(f"[MEDICINE] Dr. {self.name} prescribing '{medicine}' to {patient.name}...")
        # Add prescription info into patient's medical record
        patient.medical_record.add_visit(
            date="Today",
            symptom="Follow-up prescription",
            treatment=f"Prescription: {medicine}"
        )
        print(f"   Prescription added to {patient.name}'s record.")

    def record_test_results(self, patient, test_name: str, result: str) -> None:
        """
        Doctor records lab/test results for a patient.

        Args:
            patient: A Patient object whose results to record.
            test_name (str): Name of the test (e.g., "Blood Test", "MRI").
            result (str): The test outcome.
        """
        print(f"[LAB] Recording test '{test_name}' result for {patient.name}...")
        patient.medical_record.add_visit(
            date="Today",
            symptom=f"Test: {test_name}",
            treatment=f"Result: {result}"
        )
        print(f"   Test result recorded: {result}")

    def view_appointments(self, appointment_list: list) -> None:
        """
        Filters and displays only THIS doctor's appointments from the master list.

        Decoupling: Doctor doesn't store appointments internally. Instead, it
        reads from the shared appointment_list. This keeps concerns separated.

        Args:
            appointment_list (list): The hospital's complete list of Appointment objects.
        """
        print(f"\n[CALENDAR] Appointments for Dr. {self.name}:")
        my_appointments = [              # Filter only appointments for this doctor
            appt for appt in appointment_list
            if appt.doctor.employee_id == self.employee_id  # Match by employee ID
        ]
        if not my_appointments:
            print("  No appointments scheduled.")
            return
        for appt in my_appointments:    # Print each filtered appointment
            print(f"  - Patient: {appt.patient.name} | Time: {appt.time_slot} | Status: {appt.status}")

    # --------------------------
    # OOP: Abstraction -- Implements the required abstract method from Person
    # --------------------------
    def display_role(self) -> str:
        """Overrides Person's abstract method -- Doctor declares its own role."""
        return f"I am Dr. {self.name}, specializing in {self.specialization}."

    def __str__(self) -> str:
        """Readable string representation for print(doctor_object)."""
        return (f"[Doctor] Dr. {self.name} | Specialization: {self.specialization} "
                f"| Department: {self.department} | Fee: ${self.consultation_fee}")
