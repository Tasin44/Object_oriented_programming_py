"""
FILE: 10_appointment.py
ROLE: Represents a single scheduled appointment between a Patient and a Doctor.
      A pure Composition class -- it CONTAINS Doctor and Patient objects.

OOP CONCEPTS DEMONSTRATED:
    1. Composition (Has-A) -- Appointment HAS a Doctor, HAS a Patient
    2. Encapsulation       -- Status can only change via controlled methods
    3. SRP                 -- This class ONLY manages appointment state

SOLID PRINCIPLE APPLIED HERE: (D) Dependency Inversion Principle
    Appointment doesn't care about the concrete implementation of Doctor or Patient.
    It just holds references to them and calls their public attributes/methods.
    If we later add a "VirtualDoctor" class, Appointment works the same way
    as long as VirtualDoctor has a .name and .employee_id attribute.

    [DENY] BAD (Tight Coupling) -- Appointment directly imports and depends on Doctor/Patient:
    # from doctor import Doctor
    # from patient import Patient
    # class Appointment:
    #     def __init__(self, doctor: Doctor, patient: Patient, ...):
    #         # Only accepts Doctor and Patient -- breaks if new types are added
    #
    # [-] DISADVANTAGE: If you create a "Specialist" class or "Therapist" class,
    #    this Appointment class needs to be rewritten to accept them too.
    #    Hard coupling = fragile code.

    [OK] GOOD (Following DIP) -- Appointment accepts any object with compatible attributes.
    Python's Duck Typing handles this naturally -- if it has a .name, it works.

NOTE ON CIRCULAR IMPORTS:
    We do NOT import Doctor or Patient here.
    Importing them would create circular dependencies:
    Patient imports MedicalRecord -> Appointment imports Patient -> cycle!
    Python's Duck Typing allows us to accept any object without strict type imports.
"""


class Appointment:
    """
    Represents a single medical appointment.
    Connects a Patient and Doctor at a specific date/time.

    Composition: Appointment CONTAINS references to Doctor and Patient objects.
    State Management: Status moves from "Scheduled" -> "Completed" or "Cancelled".
    """

    def __init__(self, doctor, patient, time_slot: str):
        """
        Creates a new appointment.

        Args:
            doctor: A Doctor object assigned to this appointment.
            patient: A Patient object requesting this appointment.
            time_slot (str): Date and time of appointment (e.g., "2026-08-20 10:00 AM").
        """
        # Store references to the Doctor and Patient objects (Composition)
        self.doctor = doctor                        # Doctor object (HAS-A Doctor)
        self.patient = patient                      # Patient object (HAS-A Patient)
        self.time_slot = time_slot                  # Scheduled date and time
        self.__status = "Scheduled"                 # [PRIVATE] PRIVATE status -- only changed via methods

    # --------------------------
    # OOP: Encapsulation -- Status can only change through controlled methods
    # --------------------------
    def mark_completed(self) -> None:
        """
        Marks the appointment as completed after the patient has been seen.
        Only valid if the appointment is currently 'Scheduled'.
        """
        if self.__status == "Scheduled":
            self.__status = "Completed [OK]"          # Update the private status
            print(f"   [OK] Appointment for {self.patient.name} marked as Completed.")
        else:
            print(f"   [WARN]  Cannot complete -- appointment is already '{self.__status}'.")

    def mark_cancelled(self) -> None:
        """
        Marks the appointment as cancelled.
        Called by Receptionist.cancel_appointment() -- decoupled interaction.
        """
        if self.__status == "Scheduled":
            self.__status = "Cancelled [DENY]"          # Update the private status
            print(f"   [DENY] Appointment for {self.patient.name} has been Cancelled.")
        else:
            print(f"   [WARN]  Cannot cancel -- appointment status is '{self.__status}'.")

    def reschedule(self, new_time_slot: str) -> None:
        """
        Updates the appointment's time to a new slot.
        Only valid for 'Scheduled' appointments -- not completed or cancelled ones.

        Args:
            new_time_slot (str): The new date/time string to use.
        """
        if self.__status == "Scheduled":
            old_slot = self.time_slot               # Store old time for the log message
            self.time_slot = new_time_slot          # Update to the new time slot
            print(f"   [RESCHEDULE] Appointment rescheduled for {self.patient.name}: "
                  f"{old_slot} -> {new_time_slot}")
        else:
            print(f"   [WARN]  Cannot reschedule -- appointment is '{self.__status}'.")

    @property
    def status(self) -> str:##❓why this method required? I'm using __status on the own class then why it's required
        '''
        Because __status is private (it has double underscores), 
        it cannot be accessed from outside the Appointment class. 
        By creating a method called status(self) (usually with a @property decorator above it), 
        you create a controlled, public way for other classes (like Doctor or Receptionist) to 
        read the status without allowing them to modify the private __status variable directly.
        '''
        
        """
        Property to safely read the private __status from outside the class.
        Using @property is a Pythonic way to create a public getter.
        e.g., appointment.status -> returns the private __status string.
        """
        return self.__status                        # Controlled read-only access to private status

    def __str__(self) -> str:
        """Readable summary when print(appointment_object) is called."""
        return (f"[Appointment] Patient: {self.patient.name} -> "
                f"Dr. {self.doctor.name} | Time: {self.time_slot} | Status: {self.__status}")
