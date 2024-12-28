# OOP Component

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentSystem:
    def __init__(self, initial_students=None):
        self.students = []
        if initial_students:
            for student_data in initial_students:
                self.add_student(student_data['name'], student_data['age'], student_data['grade'])

    def add_student(self, name, age, grade):
        student = Student(name, age, grade)
        self.students.append(student)
        print(f"Student {name} has been added.")

    def view_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            print("\nList of Students:")
            for i, student in enumerate(self.students, start=1):
                print(f"{i}. {student}")
            print()

    def delete_student(self, name):
        initial_count = len(self.students)
        self.students = [student for student in self.students if student.name != name]
        if len(self.students) < initial_count:
            print(f"Student {name} has been removed.")
        else:
            print(f"Student {name} not found.")

    def filter_by_grade(self, grade):
        filtered_students = [student for student in self.students if student.grade == grade]
        if not filtered_students:
            print(f"No students found with grade {grade}.")
        else:
            print(f"\nStudents with grade {grade}:")
            for student in filtered_students:
                print(student)


# List of initial students
initial_students = [
    {"name": "Alex", "age": 20, "grade": "A"},
    {"name": "Biniyam", "age": 22, "grade": "B"},
    {"name": "Chere", "age": 19, "grade": "C"},
    {"name": "Dagi", "age": 21, "grade": "A"},
    {"name": "Eden", "age": 23, "grade": "B"}
]


# Main Program
def main():
    system = StudentSystem(initial_students)  
    while True:
        print("\nStudent Information System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Delete Student")
        print("4. Filter by Grade")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter student's name: ")
            age = input("Enter student's age: ")
            grade = input("Enter student's grade: ")
            system.add_student(name, age, grade)
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            name = input("Enter the name of the student to remove: ")
            system.delete_student(name)
        elif choice == "4":
            grade = input("Enter the grade to filter by: ")
            system.filter_by_grade(grade)
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
