class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

class Course:
    def __init__(self, name, teacher, credit):
        self.name = name 
        self.teacher = teacher
        self.credit = credit

class Teacher:
    def __init__(self, name, course):
        self.name = name
        self.course = course

class School:
    def __init__(self, name, teachers, courses, students):
        self.name = name 
        self.teachers = teachers
        self.courses = courses
        self.students = students

    def __str__(self):
        teachers_info = ", ".join([teacher.name for teacher in self.teachers])
        courses_info = ", ".join([course.name for course in self.courses])
        students_info = "\n".join([f"{student.name}: {student.id}" for student in self.students])
        return f"School: {self.name}\nTeachers: {teachers_info}\nCourses: {courses_info}\nStudents:\n{students_info}"

school_name = "Dhaka College"
ds_course = Course("DS", "Md Ali", 3.5)
teacher1 = Teacher("Md Ali", "DSA")
algo_course = Course("Algorithm", "Abdul Bari", 3)
teacher2 = Teacher("Abdul Bari", "Algorithm")

student1 = Student("Tasin", 24, 20062)
student2 = Student("Mahmud", 23, 20068)
student3 = Student("Moon", 22, 20080)

#Creating Lists of Objects for the class Teacher,Course,Student :
teachers = [teacher1, teacher2]  
courses = [ds_course, algo_course]
students = [student1, student2, student3]

my_school = School(school_name, teachers, courses, students)

print(my_school)
