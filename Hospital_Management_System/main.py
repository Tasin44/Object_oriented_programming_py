"""
FILE: 11_main.py
ROLE: The main runner -- creates all objects and demonstrates the full HMS workflow.
      This file is the ENTRY POINT of the Hospital Management System.

HOW TO RUN:
    Open a terminal in the Hospital_Management_System folder and run:
    python 11_main.py

WHAT THIS FILE DEMONSTRATES:
    [OK] Abstraction    -- Person ABC forces display_role() on all subclasses
    [OK] Inheritance    -- 3-level chain: Doctor -> Employee -> Person
    [OK] Encapsulation  -- Private salary, billing, medical history with authorized access
    [OK] Polymorphism   -- calculate_bonus() behaves differently for Doctor vs CareGiver
    [OK] Method Override-- Doctor and CareGiver have their own bonus logic
    [OK] Composition    -- Patient HAS-A MedicalRecord, Appointment HAS a Doctor + Patient
    [OK] SOLID          -- SRP, OCP, LSP, ISP, DIP shown across all files
    [OK] KISS           -- Each class does ONE thing simply and clearly
    [OK] YAGNI          -- No unused code or over-engineered features
    [OK] Decoupling     -- Classes interact through public methods, not direct private access

NOTE ON IMPORTS:
    We use sys.path.insert to allow Python to find all files in the same folder.
    In a production project, you'd use a proper package structure with __init__.py.
"""

import sys
import os

# Add the current directory to Python's module search path so imports work correctly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ----- Import all our classes -----
from person import Person                      # Abstract Base Class
from employee import Employee                  # Middle layer for staff
from department import Department              # Manages list of doctors
from doctor import Doctor                      # Specialized employee
from caregiver import CareGiver                # Nurse/CareGiver
from admin import Admin                        # Hospital administrator
from receptionist import Receptionist          # Front-desk manager
from patient import Patient                    # The patient (not employee!)
from medical_record import MedicalRecord       # Patient's history (composition)
from appointment import Appointment           # Scheduled visit (composition)


# ============================================================
# HELPER FUNCTION: Print a styled section header for readability
# ============================================================
def print_section(title: str) -> None:
    """Prints a formatted section divider for cleaner console output."""
    print(f"\n{'='*65}")
    print(f"  [HOSPITAL]  {title}")
    print(f"{'='*65}")


# ============================================================
# SECTION 1: Create the Hospital Staff
# ============================================================
print_section("STEP 1: Creating Hospital Staff")

# --- Create the Admin ---
# Admin is an Employee is a Person -- 3-level inheritance
admin = Admin(
    name="Mr. Robert King",
    age=50, gender="Male",
    contact="01700000001",
    person_id="P001",
    employee_id="E001",
    department="Administration",
    salary=80000.00
)
print(f"[OK] Created: {admin}")                       # Calls Admin.__str__()
print(f"   Role: {admin.display_role()}")           # Polymorphism: Admin's own display_role


# --- Create the Doctor ---
doctor = Doctor(
    name="Sarah Ahmed",
    age=42, gender="Female",
    contact="01700000002",
    person_id="P002",
    employee_id="E002",
    department="Cardiology",
    salary=120000.00,
    specialization="Cardiologist",
    consultation_fee=500.00
)
print(f"\n[OK] Created: {doctor}")                    # Calls Doctor.__str__()
print(f"   Role: {doctor.display_role()}")          # Polymorphism: Doctor's own display_role


# --- Create the CareGiver ---
nurse = CareGiver(
    name="Maria Santos",
    age=30, gender="Female",
    contact="01700000003",
    person_id="P003",
    employee_id="E003",
    department="Cardiology",
    salary=40000.00,
    shift_timings="Night 10PM-6AM",
    assigned_ward="Ward A"
)
print(f"\n[OK] Created: {nurse}")                     # Calls CareGiver.__str__()
print(f"   Role: {nurse.display_role()}")           # Polymorphism: CareGiver's display_role


# --- Create the Receptionist ---
receptionist = Receptionist(
    name="Ali Hassan",
    age=28, gender="Male",
    contact="01700000004",
    person_id="P004",
    employee_id="E004",
    department="Front Desk",
    salary=35000.00
)
print(f"\n[OK] Created: {receptionist}")
print(f"   Role: {receptionist.display_role()}")


# ============================================================
# SECTION 2: Create the Department and Add Doctors
# ============================================================
print_section("STEP 2: Setting Up Department (Composition)")

# Create a Cardiology Department -- Composition: Department CONTAINS Doctors
cardiology_dept = Department(department_name="Cardiology")
cardiology_dept.add_doctor(doctor)                  # Add our doctor to the department
cardiology_dept.show_all_doctors()                  # Display the department's roster
print(f"   {cardiology_dept}")                      # Department's __str__ summary


# ============================================================
# SECTION 3: Admin Hires Staff
# ============================================================
print_section("STEP 3: Admin Hires All Staff (DIP + Polymorphism)")

# SOLID DIP: hire_employee() accepts ANY Employee subtype -- not hard-coded types
admin.hire_employee(doctor)                         # Hires Doctor object
admin.hire_employee(nurse)                          # Hires CareGiver object
admin.hire_employee(receptionist)                   # Hires Receptionist object
admin.view_all_staff()                              # Admin views full registry


# ============================================================
# SECTION 4: Encapsulation -- Salary Access Control
# ============================================================
print_section("STEP 4: Encapsulation -- Salary Access Control")

# [OK] Admin CAN change salary (authorized)
admin.change_employee_salary(doctor, 130000.00)     # Goes through set_salary("Admin", ...)

# [DENY] Doctor tries to change nurse's salary (unauthorized -- should be denied)
print("\n[Testing unauthorized salary change...]")
nurse.set_salary(requester_role="Doctor", new_salary=9999.00)  # Should print ACCESS DENIED


# ============================================================
# SECTION 5: Create a Patient
# ============================================================
print_section("STEP 5: Creating a Patient (Inheritance + Composition)")

# Patient is a PERSON but NOT an Employee -- different inheritance branch
patient = Patient(
    name="John Rahman",
    age=45, gender="Male",
    contact="01711111111",
    person_id="P100",
    patient_id="PAT001",
    blood_group="O+",
    assigned_doctor=doctor                          # Reference to Doctor object
)
print(f"[OK] Created: {patient}")                    # Patient's __str__
print(f"   Role: {patient.display_role()}")         # Polymorphism -- patient's display_role
# MedicalRecord was automatically created inside Patient's constructor (Composition)
print(f"   {patient.medical_record}")               # Shows MedicalRecord summary


# ============================================================
# SECTION 6: Receptionist Books an Appointment
# ============================================================
print_section("STEP 6: Receptionist Books Appointment (Composition)")

# Appointment object is created -- it CONTAINS Doctor and Patient references
appointment = receptionist.book_appointment(
    patient=patient,
    doctor=doctor,
    time_slot="2026-08-20 10:00 AM"
)
print(f"   {appointment}")                          # Appointment's __str__

# View the doctor's appointments from the shared registry
appointment_registry = receptionist.get_appointment_registry()
doctor.view_appointments(appointment_registry)      # Doctor filters its own appointments


# ============================================================
# SECTION 7: Doctor Diagnoses and Prescribes
# ============================================================
print_section("STEP 7: Doctor Diagnoses Patient (SRP + Decoupling)")

# Doctor calls controlled methods -- doesn't directly modify Patient's private data
doctor.diagnose_patient(patient, symptom="Chest pain and shortness of breath", disease="Angina Pectoris")
doctor.prescribe_medicine(patient, medicine="Aspirin 100mg -- once daily after meals")
doctor.record_test_results(patient, test_name="ECG", result="Mild ST depression observed")


# ============================================================
# SECTION 8: CareGiver Updates Patient Vitals
# ============================================================
print_section("STEP 8: CareGiver Updates Vitals + Logs Night Shift")

nurse.update_patient_vitals(patient, blood_pressure="130/85 mmHg", temperature=37.2)
nurse.add_care_note(patient, note="Patient is stable. Eating well. No complaints.")

# Log some night shifts for bonus calculation later
nurse.log_night_shift()
nurse.log_night_shift()
nurse.log_night_shift()                             # 3 night shifts logged


# ============================================================
# SECTION 9: Patient Views Medical History
# ============================================================
print_section("STEP 9: Patient Views Own Medical History (Encapsulation)")

# Patient can read their own record -- via controlled public method
patient.get_medical_history()


# ============================================================
# SECTION 10: Billing and Payment
# ============================================================
print_section("STEP 10: Billing (Encapsulation + Decoupling)")

# Receptionist generates the bill -- calls patient.update_bill("Receptionist", ...)
receptionist.generate_bill(patient=patient, doctor=doctor)

# Patient views their bill -- read-only access via public getter
patient.view_bill()

# [DENY] Doctor tries to update billing (unauthorized -- should be denied)
print("\n[Testing unauthorized billing update...]")
patient.update_bill(requester_role="Doctor", amount=9999.00)   # Should be denied

# [OK] Patient pays their bill
patient.pay_bill(amount=500.00)
patient.view_bill()                                 # Bill should now show $0 or reduced


# ============================================================
# SECTION 11: Admin Runs Payroll -- Polymorphism in Action
# ============================================================
print_section("STEP 11: Admin Runs Payroll (METHOD OVERRIDING POLYMORPHISM)")

# THIS IS THE KEY POLYMORPHISM DEMO:
# Admin loops through ALL staff and calls calculate_bonus() on each.
# Python automatically calls the CORRECT version for each object:
#   - Doctor.calculate_bonus()    -> 20% salary + $10 per patient
#   - CareGiver.calculate_bonus() -> $50 per night shift
#   - Receptionist.calculate_bonus() -> Default Employee: 5% salary (not overridden)
# Same method call -- DIFFERENT behavior. This is Runtime Polymorphism.
admin.run_payroll()


# ============================================================
# SECTION 12: Appointment Lifecycle
# ============================================================
print_section("STEP 12: Appointment State Changes (Encapsulation)")

print(f"Before: {appointment}")                     # Status = Scheduled
appointment.mark_completed()                        # Status changes to Completed
print(f"After:  {appointment}")                     # Status = Completed [OK]

# Try to cancel an already-completed appointment (should be denied)
print("\n[Trying to cancel a completed appointment...]")
appointment.mark_cancelled()                        # Should print a warning


# ============================================================
# SECTION 13: Abstraction Demo -- display_role() Polymorphism
# ============================================================
print_section("STEP 13: ABSTRACTION -- All Roles Declaring Themselves")

# Store all people in ONE list -- mixing different types (Polymorphism!)
all_people = [admin, doctor, nurse, receptionist, patient]

print("All HMS members declaring their roles (Polymorphism via Abstract Method):\n")
for person in all_people:
    # display_role() is abstract in Person -- each class implements it differently
    # Python calls the CORRECT version for each object type automatically
    print(f"  -> {person.display_role()}")


# ============================================================
# SECTION 14: Department Management
# ============================================================
print_section("STEP 14: Department -- Composition + Encapsulation")

# Create a second doctor and add to department
doctor2 = Doctor(
    name="Khalid Hasan",
    age=38, gender="Male",
    contact="01700000099",
    person_id="P010",
    employee_id="E010",
    department="Cardiology",
    salary=110000.00,
    specialization="Cardiac Surgeon",
    consultation_fee=800.00
)
cardiology_dept.add_doctor(doctor2)                 # Add second doctor
cardiology_dept.show_all_doctors()                  # Shows both doctors

# Remove original doctor (e.g., they resigned)
print()
cardiology_dept.remove_doctor(doctor)               # Remove first doctor
cardiology_dept.show_all_doctors()                  # Now shows only doctor2


# ============================================================
# DONE
# ============================================================
print_section("[OK] HOSPITAL MANAGEMENT SYSTEM DEMO COMPLETE")
print("""
  All OOP Concepts Demonstrated:
  -----------------------------------------------
  [OK] Abstraction      -- Person ABC + abstract display_role()
  [OK] Inheritance      -- 3-level chain (Doctor->Employee->Person)
  [OK] Encapsulation    -- Private salary, billing, medical_history
  [OK] Polymorphism     -- calculate_bonus(), display_role()
  [OK] Method Overriding-- Doctor & CareGiver override calculate_bonus()
  [OK] Composition      -- Patient HAS-A MedicalRecord, Appointment HAS Doctor+Patient
  [OK] SOLID Principles -- S, O, L, I, D all applied with comments
  [OK] KISS             -- Each class is focused and simple
  [OK] YAGNI            -- No unused features added
  [OK] Decoupling       -- Classes talk via public methods, not private data
""")
