"""
FILE: 9_medical_record.py
ROLE: Stores and manages structured medical history for a patient.
      A utility class used via Composition inside the Patient class.

OOP CONCEPTS DEMONSTRATED:
    1. Composition     -- Patient HAS-A MedicalRecord (not inherits from it)
    2. Encapsulation   -- internal lists are managed via controlled methods
    3. SRP             -- This class ONLY manages medical history data, nothing else

DESIGN PATTERN: KISS (Keep It Simple, Stupid)
    Medical records are just structured lists. We don't overcomplicate this.
    Each visit entry is a simple dictionary with date, symptom, and treatment.
    This is clean, readable, and easy to extend later.

YAGNI PRINCIPLE:
    We only store what we need right now: dates, symptoms, and treatments.
    We don't add unused fields like "insurance_code", "icd10_code", etc.
    Those can be added LATER if and when required.
"""


class MedicalRecord:
    """
    Represents a patient's complete medical history.
    Stores visits, symptoms, and treatments as structured list data.

    Design: This class is created INSIDE the Patient constructor (Composition).
    One Patient -> One MedicalRecord (one-to-one relationship).
    """

    def __init__(self, patient):
        """
        Creates a new (empty) medical record for a specific patient.

        Args:
            patient: The Patient object this record belongs to.
                     We store a reference back to the patient for identification.
        """
        # Reference back to the owner patient -- used for display purposes
        self.__patient_ref = patient        # [PRIVATE] PRIVATE reference to the patient
        #❓why I'm using __patient_ref here 
        '''
        You are storing a reference to the Patient object so that the MedicalRecord knows whose record it is. 
        Making it private (__) ensures that outside code cannot randomly swap out the patient that this record belongs to.
        '''

        # Internal data storage using lists of dictionaries
        # Each entry is a dict: {"date": ..., "symptom": ..., "treatment": ...}
        self.__visit_history = []           # [PRIVATE] PRIVATE list of all visit records

    # --------------------------
    # OOP: Encapsulation -- Controlled Write Access
    # --------------------------
    def add_visit(self, date: str, symptom: str, treatment: str) -> None:
        """
        Adds a new visit entry to the patient's medical history.
        This is the ONLY way data can be written into the record.

        Called by: Doctor (diagnosis, prescription, test results), CareGiver (vitals, notes)
        Access Pattern: Doctor -> diagnose_patient() -> patient.medical_record.add_visit()
                        NOT: Doctor -> patient.__medical_history = "..."  (WRONG!)

        Args:
            date (str): Date of the visit/entry.
            symptom (str): What the patient presented with or what was checked.
            treatment (str): The treatment, prescription, or observation recorded.
        """
        # Build a structured dictionary entry for this visit
        visit_entry = {
            "date": date,
            "symptom": symptom,
            "treatment": treatment
        }
        self.__visit_history.append(visit_entry)    # Append the new entry to the private list
        #❓__visit_history is a list, then How I'm appending a dict inside it
        '''
            In Python, lists are incredibly flexible—they can contain any type of object, including dictionaries! 
            You are simply taking a dictionary object (visit_entry) and adding it as an item in the __visit_history list. 
            The list ends up looking like this: [{visit1_dict}, {visit2_dict}].
        '''
    # --------------------------
    # OOP: Encapsulation -- Controlled Read Access
    # --------------------------
    def show_history(self) -> None:
        """
        Displays all visit history entries in a readable format.
        Public read access -- any authorized caller can view the history.
        Called by: Patient.get_medical_history()
        """
        if not self.__visit_history:                # Check if the list is empty
            print("  No medical history recorded yet.")
            return

        # Loop through each visit entry and print it
        for index, entry in enumerate(self.__visit_history, 1):  # enumerate gives numbering
            print(f"  Visit {index}:")
            print(f"    [CALENDAR] Date      : {entry['date']}")
            print(f"    [SICK] Symptom   : {entry['symptom']}")
            print(f"    [MEDICINE] Treatment : {entry['treatment']}")
            print()  # Empty line between entries for readability

    def get_visit_count(self) -> int:
        """
        Returns the total number of recorded visits.
        Public read-only access to a count -- no raw list exposure.
        """
        return len(self.__visit_history)            # Return the count, not the private list

    def get_latest_entry(self) -> dict:
        """
        Returns the most recent medical entry (the last item in the list).
        Useful for quick reference to the last visit.

        Returns:
            dict: The latest visit entry, or None if no entries exist.
        """

        ##❓isn't it possible to call here the get_visit_count function to check if entry exist then return self__visit_history[-1]
        '''
        Yes, you could absolutely do if self.get_visit_count() > 0:. 
        However, if self.__visit_history: is a more Pythonic and direct way to check if a list is not empty. 
        In Python, an empty list evaluates to False, and a list with items evaluates to True.
        '''
        if self.__visit_history:
            return self.__visit_history[-1]         # Python list: -1 gives last item
        return None                                 # Return None if no history exists

    def __str__(self) -> str:
        """Readable summary when print(medical_record_object) is called."""
        return (f"[MedicalRecord] Patient: {self.__patient_ref.name} "
                f"| Total Visits: {self.get_visit_count()}")
