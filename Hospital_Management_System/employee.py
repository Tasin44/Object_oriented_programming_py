"""
FILE: 2_employee.py
ROLE: Middle-layer class between Person and all hospital staff roles.

OOP CONCEPT: Inheritance
    Employee inherits from Person, adding work-specific attributes.
    It then serves as the parent for Doctor, CareGiver, Admin, Receptionist.

SOLID PRINCIPLE APPLIED HERE: (S) Single Responsibility Principle
    The SRP says: "A class should have only ONE reason to change."
    Employee handles only: salary, department, and bonus logic.
    It does NOT handle appointments, medical records, or billing.

    [DENY] BAD (Violating SRP) -- One massive class doing everything:
    # class Employee(Person):
    #     def __init__(...):
    #         self.salary = salary
    #         self.patient_list = []       # ? belongs to Receptionist!
    #         self.appointments = []       # ? belongs to Doctor!
    #         self.diagnosis_history = []  # ? belongs to Doctor!
    #
    #     def book_appointment(self): ...  # ? Not every employee books appointments!
    #     def prescribe_medicine(self): .. # ? Not every employee prescribes!
    #
    # [-] DISADVANTAGE: If appointment logic changes, you must edit THIS class,
    #    even though 90% of employees have nothing to do with appointments.
    #    Every unrelated change risks breaking other employees' logic.

    [OK] GOOD (Following SRP) -- Employee only knows about employee-level concerns.
    Doctor/Receptionist subclasses will handle their own specific responsibilities.

SOLID PRINCIPLE APPLIED HERE: (O) Open/Closed Principle
    The OCP says: "Open for EXTENSION, Closed for MODIFICATION."
    calculate_bonus() is defined here with a DEFAULT logic.
    When we add a new staff type (e.g., Surgeon), we DON'T touch this file.
    The new class just overrides calculate_bonus() with its own logic.

    [DENY] BAD (Violating OCP) -- Using if/elif to handle every new employee type:
    # def calculate_bonus(self, role):
    #     if role == "Doctor":
    #         return self.salary * 0.20
    #     elif role == "Nurse":
    #         return self.salary * 0.10
    #     elif role == "Admin":           # ? every new role = editing this file!
    #         return self.salary * 0.05
    #
    # [-] DISADVANTAGE: Every time HR adds a new staff type, you must open
    #    this file and add another elif. This risks introducing bugs in
    #    existing, already-tested logic.

    [OK] GOOD (Following OCP) -- Default bonus here, each subclass overrides its own.
"""

from person import Person  # Import the abstract Person blueprint


class Employee(Person):
    """
    Represents any hospital staff member who receives a salary.
    Inherits shared identity from Person and adds employment-specific data.
    All staff roles (Doctor, Nurse, Admin, Receptionist) inherit from this.
    """

    def __init__(self, name: str, age: int, gender: str, contact: str,
                 person_id: str, employee_id: str, department: str, salary: float):
        ##❓is it necessary to use str here, can't I just use (name,department,salary) like this
        '''
        No, it is not strictly necessary. 
        You can just write person_id, employee_id, department, salary. 
        The : str and : float are Type Hints. 
        They don't change how the code runs, they just help you and your code editor know what type of data is supposed to be passed in.
        '''
        """
        Calls Person's __init__ first via super() to initialize shared attributes,
        then adds Employee-specific attributes on top.
        """
        # super() calls the Parent class (Person) constructor -- avoids code repetition
        super().__init__(name, age, gender, contact, person_id)

        self.employee_id = employee_id          # Unique ID for payroll tracking
        self.department = department            # Department name (e.g., "Cardiology")
        self.__salary = salary                  # [PRIVATE] PRIVATE -- only Admin can modify

    # --------------------------
    # OOP: Encapsulation -- Getter
    # --------------------------
    def get_salary(self) -> float:
        #❓Maybe I'm using here float because I've used salary: float on the init right? if I didn't mention salary: float, I think I can then use here def get_salary(self)

        '''
        Exactly! -> float is just a type hint saying "this returns a float". 
        If you removed : float from __init__, you could definitely remove -> float here. 
        Even if you kept : float in __init__, you don't have to use -> float here. 
        But it's good practice to keep your type hints consistent!
        '''
        """
        Public Getter for the private __salary attribute.
        Encapsulation: The salary data is HIDDEN, but we allow CONTROLLED READ access.
        Any role can VIEW the salary, but cannot directly change the underlying value.
        """
        return self.__salary

    # --------------------------
    # OOP: Encapsulation -- Setter (with Authorization Check)
    # --------------------------
    def set_salary(self, requester_role: str, new_salary: float) -> None:
        """
        Public Setter for the private __salary attribute.
        Encapsulation: Only allows modification if the requester is an Admin.

        Args:
            requester_role (str): The role of whoever is trying to change salary.
            new_salary (float): The new salary amount to set.
        """
        if requester_role == "Admin":           # Authorization check before modifying
            self.__salary = new_salary          # Only Admin can change private salary
            print(f"[OK] Salary updated for {self.name}: ${new_salary:,.2f}")#❓what does this line doing - .2f ensures it always shows exactly two decimal places (e.g., .00).
        else:
            # Deny access if the requester is not authorized
            print(f"[DENY] ACCESS DENIED: Only Admin can change salary. You are '{requester_role}'.")

    # --------------------------
    # OOP: Polymorphism -- Method Overriding (Base version)
    # --------------------------
    def calculate_bonus(self) -> float:
        """
        Default bonus calculation: 5% of salary.
        This is the BASE version -- Doctor and CareGiver will OVERRIDE this
        with their own specific bonus logic (Polymorphism / Method Overriding).
        """
        bonus = self.__salary * 0.05            # Default: 5% bonus for all staff
        print(f"  Bonus for {self.name} ({self.__class__.__name__}): ${bonus:,.2f} (Default 5%)")
        return bonus

    # --------------------------
    # OOP: Abstraction -- Forced display_role implementation
    # --------------------------
    def display_role(self) -> str:
        """
        Implements the abstract method from Person.
        Employee-level display -- subclasses will override with their specific role name.
        """
        return f"I am an Employee at department: {self.department}"
