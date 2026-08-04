'''
Why Use a Class-Level Dictionary?

    Fast Access:
        You can directly access an object using its key without looping through all items.
    Centralized Data:
        All instances can share and access the same data.
    Automatic Updates:
        Every time an object is added, it's stored in a shared location.

'''

class Student:
    all_students = {}  # Class-level dictionary to store all students

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        Student.all_students[student_id]=self  # # Add to class-level dictionary

    @classmethod
    def find_student(self, student_id):
        if student_id in self.all_students:
                stdobj = self.all_students[student_id]
                print(f"Found: {stdobj.name} with ID {stdobj.student_id}")
                return
        print(f"No student found with ID {student_id}")

# Create students
student1 = Student("Alice", 101)
student2 = Student("Bob", 102)

# Search for a student
Student.find_student(102)  # Output: Found: Bob with ID 102
Student.find_student(103)  # Output: No student found with ID 103


'''
Q:
Student.all_students[student_id]=self
Here, I'm already making student_id as key, then why I'm storing the whole object as self , 
can't I only store the name like self.name as value?
(will see more on Class-Level List)

Ans: 
You're storing the entire object as the value.
This allows you to later access all attributes like:

stdobj.name
stdobj.student_id
# and any other future attributes


🤔 If you do:

    Student.all_students[student_id] = self.name

You’re only storing a string. Then stdobj = self.all_students[student_id] will just be a string like "Bob", and you'll lose access to student_id or any other future data.

You could still do:

    print(f"Found: {stdobj} with ID {student_id}")

But that's all you can get — no .student_id, .grade, .age, etc.




✅ Summary: When to store what?
Store as	                            What you get	                    Use case
self (whole object)	                    All attributes (flexible)	        If you need more than just a name
self.name (string only)	                Only name	                        If you only care about name lookup
Custom dict like {name, grade}	        Partial data	                    If you only want selected fields

'''
