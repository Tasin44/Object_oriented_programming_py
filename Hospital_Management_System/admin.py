"""
FILE: 6_admin.py
ROLE: Represents a Hospital Administrator -- highest authority in the HMS.

OOP CONCEPTS DEMONSTRATED:
    1. Inheritance -- Admin IS-AN Employee IS-A Person
    2. Encapsulation -- Admin is the ONLY role that can change salaries (authorized access)
    3. Abstraction -- implements display_role() from Person ABC

SOLID PRINCIPLE APPLIED HERE: (D) Dependency Inversion Principle
    The DIP says: "High-level modules should NOT depend on low-level modules.
    Both should depend on ABSTRACTIONS."
    Admin's hire/fire methods accept ANY Employee object (or subtype: Doctor, Nurse, etc.)
    NOT specifically typed as "Doctor" or "CareGiver".

    [DENY] BAD (Violating DIP) -- Admin tightly coupled to concrete types:
    # class Admin(Employee):
    #     def hire_doctor(self, doctor: Doctor): ...       # ? only works for Doctor!
    #     def hire_nurse(self, nurse: CareGiver): ...      # ? only works for CareGiver!
    #     def hire_receptionist(self, rec: Receptionist): # ? need a NEW method each time!
    #
    # [-] DISADVANTAGE: Every time a new staff role is created (e.g., Pharmacist),
    #    you must open this Admin class and add yet another hire method.
    #    This violates both DIP AND the Open/Closed Principle.

    [OK] GOOD (Following DIP) -- Admin accepts any Employee-compatible object.
    Hire/fire works for Doctor, Nurse, Receptionist, or any future employee type
    without ever modifying this file.
"""

from employee import Employee   # Admin IS-AN Employee


class Admin(Employee):
    """
    Represents a Hospital Administrator.
    Has the highest privileges: manages staff roster and can change salaries.

    Inheritance Chain: Admin -> Employee -> Person (ABC)
    """

    def __init__(self, name: str, age: int, gender: str, contact: str,
                 person_id: str, employee_id: str, department: str, salary: float):
        """All attributes come from Employee and Person -- Admin adds no new attributes."""
        super().__init__(name, age, gender, contact, person_id,
                         employee_id, department, salary)

        self.__staff_registry = []     # [PRIVATE] PRIVATE list -- only Admin manages the full staff list

    # --------------------------
    # Admin's Core Responsibilities
    # --------------------------
    def hire_employee(self, new_employee) -> None:
        """
        Adds a new employee to the hospital's staff registry.

        SOLID DIP: Accepts ANY Employee subtype (Doctor, Nurse, Receptionist, etc.)
        No need to write separate methods for each staff type.

        Args:
            new_employee: Any object that inherits from Employee.
        """
        self.__staff_registry.append(new_employee)           # Add to private staff list
        print(f"[OK] {new_employee.name} ({new_employee.__class__.__name__}) has been HIRED.")

    def fire_employee(self, employee) -> None:
        """
        Removes an employee from the hospital's staff registry.

        Args:
            employee: The Employee object to remove.
        """
        if employee in self.__staff_registry:
            self.__staff_registry.remove(employee)           # Remove from registry
            print(f"[DENY] {employee.name} has been TERMINATED from the hospital.")
        else:
            print(f"[WARN]  {employee.name} is NOT in the staff registry.")

    def change_employee_salary(self, employee, new_salary: float) -> None:
        """
        Updates an employee's salary. Passes "Admin" as the authorized requester.
        Encapsulation: The actual salary change happens inside Employee.set_salary()
        which checks if requester_role == "Admin" before allowing the change.

        Args:
            employee: The Employee object whose salary to update.
            new_salary (float): The new salary amount.
        """
        print(f"\n[KEY] Admin {self.name} is updating salary for {employee.name}...")
        # Calls the Employee's controlled setter method with "Admin" authorization
        employee.set_salary(requester_role="Admin", new_salary=new_salary)

    def view_all_staff(self) -> None:
        """
        Prints a summary of all currently registered staff members.
        Admin has full visibility of the entire workforce.
        """
        print(f"\n--- [RECORD] Full Staff Registry (Admin: {self.name}) ---")
        if not self.__staff_registry:
            print("  No staff hired yet.")
            return
        for index, staff in enumerate(self.__staff_registry, 1):   # enumerate for numbering
            print(f"  {index}. {staff.name} | Role: {staff.__class__.__name__} "
                  f"| Dept: {staff.department} | Salary: ${staff.get_salary():,.2f}")

    def run_payroll(self) -> None:
        """
        Calculates and prints bonuses for ALL staff members.

        OOP Polymorphism in action: We call calculate_bonus() on EACH employee object.
        Python automatically calls the correct version:
            - Doctor's calculate_bonus() for Doctor objects
            - CareGiver's calculate_bonus() for CareGiver objects
            - Employee's default calculate_bonus() for Admin/Receptionist objects
        This is RUNTIME POLYMORPHISM -- the same method call -> different behavior.
        """
        print(f"\n--- [MONEY] Running Payroll Bonus Calculation ---")
        total_bonus = 0
        for staff in self.__staff_registry:
            bonus = staff.calculate_bonus()  # Polymorphism: calls each class's own version
            total_bonus += bonus
        print(f"\n  Total Bonus Payout: ${total_bonus:,.2f}")

    # --------------------------
    # OOP: Abstraction -- Implements required abstract method from Person
    # --------------------------
    def display_role(self) -> str:
        """Admin declares its own role -- implements the abstract method from Person."""
        return f"I am {self.name}, the Hospital Administrator."

    def __str__(self) -> str:
        """Readable string when print(admin_object) is called."""
        return f"[Admin] {self.name} | Department: {self.department}"
