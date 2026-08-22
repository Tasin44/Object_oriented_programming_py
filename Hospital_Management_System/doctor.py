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
    # Medical Methods (Doctor's Core Responsibilities)একদম নিছে ব্যাখা করা আছে 
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
            print(f"  - Patient: {appt.patient.name} | Time: {appt.time_slot} | Status: {appt.status}")#❓I've seen the status is private, then how the dr accessing this?where did u make it's permission for dr?

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


'''
❓❓❓❓❓❓❓
def diagnose_patient(self, patient: "Patient", symptom: str, disease: str) -> None:

Question:
এখানে কি আমি পেশেন্ট ক্লাসের পেশেন অব্জেক্ট টা পাঠাচ্ছি যাতে করে ডাক্তার এই মেথড টা ইমপ্লিমেন্ট করতে পারে? 
যহি তাই হয় , তাহলে এটা কিভাবে সম্ভব, ওওপি তে কি এমন পসিবল লাইক আমি একটা ক্লাস কে 
আরেকটা ক্লাসেরে অব্জেক্ট হিসেবে পাঠাব যাতে সে মডিফাই করতে পারে, 
২য়ত ডাক্তার যে মেডিকেল রেকর্ড মডিফাই করছে  patient.medical_record.add_visit() 
এই পারমিশন ডাক্টার কোথায় পেলো? পেশেন্ট ত তার চাইল্ড ক্লাস না, আলাদা ক্লাস 

Answer:

২. "OOP তে কি এমন পসিবল যে আমি একটা ক্লাসকে আরেকটা ক্লাসের অবজেক্ট হিসেবে পাঠাবো?"
উত্তর: হ্যাঁ, ১০০% পসিবল এবং OOP তে এটাই সবচেয়ে বেশি করা হয়!

এর একটা সুন্দর নাম আছে, একে বলা হয় Association (অ্যাসোসিয়েশন) বা Dependency (নির্ভরশীলতা)। OOP এর দুনিয়ায় অবজেক্টরা একা একা কাজ করতে পারে না। তারা একে অপরের সাথে কথা বলে (যাকে বলা হয় Message Passing)।

যেমন বাস্তবে: একজন "ডাক্তার" (Doctor Object) একটা "রোগী" (Patient Object)-কে চেক করে। ডাক্তার নিজে রোগী নয়, আবার রোগীও ডাক্তার নয়। কিন্তু তারা একে অপরের সাথে ইন্টারেক্ট করছে। ঠিক তেমনি কোডেও আমরা Doctor ক্লাসের মেথডের ভেতরে Patient ক্লাসের একটা অবজেক্টকে প্যারামিটার হিসেবে পাঠাই, যাতে ডাক্তার ওই পেশেন্টের ডেটা দেখতে বা পরিবর্তন করতে পারে।

৩. "ডাক্তার যে মেডিকেল রেকর্ড মডিফাই করছে, এই পারমিশন ডাক্তার কোথায় পেলো? পেশেন্ট তো তার চাইল্ড ক্লাস না!"
উত্তর: খুব সুন্দর একটা প্রশ্ন! আপনার কনফিউশনটা হলো ইনহেরিট্যান্স (Inheritance - Parent/Child) নিয়ে।

সত্যিটা হলো: এক ক্লাসের ডেটা অন্য ক্লাস থেকে অ্যাক্সেস করার জন্য Parent/Child হওয়ার কোনো দরকার নেই।

OOP তে পারমিশনের মূল চাবিকাঠি হলো Public (পাবলিক) এবং Private (প্রাইভেট)।

আপনি যদি খেয়াল করেন, Patient ক্লাসের ভেতরে medical_record ভেরিয়েবলটা তৈরি করা হয়েছে পাবলিক হিসেবে (এর আগে কোনো __ ডাবল আন্ডারস্কোর নেই)।
আবার MedicalRecord ক্লাসের ভেতরে add_visit() মেথডটাও পাবলিক (এর আগেও কোনো __ নেই)।
যেহেতু এগুলো পাবলিক (Public), তার মানে হলো—বিশ্বের যে কারও কাছে যদি Patient অবজেক্টটা থাকে, সে চাইলেই patient.medical_record.add_visit() কল করতে পারবে। এর জন্য ডাক্তারকে পেশেন্টের Parent বা Child হতে হবে না।

এক কথায় বলতে গেলে: যেহেতু medical_record এবং add_visit() কে প্রাইভেট করে তালা মেরে দেওয়া হয়নি, তাই ডাইরেক্ট রেফারেন্স (প্যারামিটার হিসেবে পাওয়া patient অবজেক্ট) ব্যবহার করে ডাক্তার খুব সহজেই এটা মডিফাই করতে পারছে!
'''