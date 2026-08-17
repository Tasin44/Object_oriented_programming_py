"""
FILE: 3_department.py
ROLE: Represents a hospital department (e.g., Cardiology, Neurology).
      Uses COMPOSITION -- it holds a list of Doctor objects inside it.

OOP CONCEPT: Composition (Has-A Relationship)
    Department is NOT a Doctor, and Doctor is NOT a Department.
    But a Department HAS-A list of Doctors inside it.
    This is composition/aggregation -- one of the key OOP design patterns.

DESIGN PATTERN APPLIED: KISS (Keep It Simple, Stupid)
    We don't overthink this class. It does one simple job:
    manage a list of doctors for a named department.
    No inheritance needed here -- just clean, simple composition.

YAGNI PRINCIPLE APPLIED: (You Aren't Gonna Need It)
    We only add what the HMS currently needs.

    [DENY] BAD (Violating YAGNI) -- Over-engineering with unused features:
    # class Department:
    #     def __init__(self):
    #         self.budget = 0             # Not needed yet!
    #         self.floor_number = 0       # Not needed yet!
    #         self.admin_list = []        # Not needed yet!
    #         self.nurse_schedule = {}    # Not needed yet!
    #
    # [-] DISADVANTAGE: You write and maintain code that is NEVER used.
    #    It bloats the class, confuses other developers, and wastes time.

    [OK] GOOD (Following YAGNI) -- Only what is needed: department_name + doctor_list.
"""

# Note: We don't import Doctor here to avoid CIRCULAR IMPORTS.
# (Doctor imports Employee, Employee imports Person -- if Department imports Doctor
#  and Doctor imports Department, Python gets confused in a circular loop.)
# Instead, we accept any object and just call methods on it (Duck Typing).


class Department:
    """
    Represents a hospital department.
    Manages a collection of Doctor objects assigned to this department.

    DESIGN: Composition/Aggregation
        Department CONTAINS Doctors -- not inherits from them.
        This gives flexibility: a Doctor can belong to multiple departments if needed.
    """

    def __init__(self, department_name: str):
        self.department_name = department_name  # Name of the department (e.g., "Cardiology")
        self.__doctor_list = []                 # [PRIVATE] PRIVATE list -- managed only via methods

    # --------------------------
    # OOP: Encapsulation -- Add to the list via a controlled method
    # --------------------------
    def add_doctor(self, doctor) -> None:
        """
        Adds a Doctor object to this department's roster.
        We check for duplicates before adding to keep the list clean (KISS principle).

        Args:
            doctor: A Doctor instance to be added to this department.
        """
        # Check if doctor is already in the list to avoid duplicates
        if doctor in self.__doctor_list:
            print(f"[WARN]  Dr. {doctor.name} is already in {self.department_name} department.")
        else:
            self.__doctor_list.append(doctor)   # Add doctor object to the list
            print(f"[OK] Dr. {doctor.name} added to {self.department_name} department.")

    def remove_doctor(self, doctor) -> None:
        """
        Removes a Doctor object from this department (e.g., if they resign or transfer).

        Args:
            doctor: The Doctor instance to remove.
        """
        if doctor in self.__doctor_list:
            self.__doctor_list.remove(doctor)   # Remove the specific doctor object
            print(f"[OK] Dr. {doctor.name} removed from {self.department_name} department.")
        else:
            print(f"[DENY] Dr. {doctor.name} is NOT in the {self.department_name} department.")

    def show_all_doctors(self) -> None:
        """
        Loops through the doctor_list and prints each doctor's details.
        Demonstrates iterating over a list of objects.
        """
        print(f"\n--- Doctors in {self.department_name} Department ---")
        if not self.__doctor_list:                              # Check if list is empty
            print("  No doctors assigned yet.")
            return
        for index, doctor in enumerate(self.__doctor_list, 1): # enumerate gives us numbering
            print(f"  {index}. {doctor.name} | Specialization: {doctor.specialization}")

    def get_doctor_count(self) -> int:
        """Returns how many doctors are currently in this department."""
        return len(self.__doctor_list)

    def __str__(self) -> str:
        """Readable string when you print(department_object)."""
        return f"Department: {self.department_name} | Doctors: {self.get_doctor_count()}"
