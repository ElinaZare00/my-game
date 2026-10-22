
from rich.console import Console


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


class StudentManagementSystem:
    def __init__(self):
        self.console = Console()
        self.students = []

    def add_student(self):
        name = input("Student name: ")
        grade = float(input("Student grade: "))

        student = Student(name, grade)
        self.students.append(student)

        self.console.print(
            "Student added successfully!",
            style="bold green"
        )

    def show_students(self):
        if len(self.students) == 0:
            self.console.print("No students found!", style="red")
        else:
            self.console.print("\nStudents List:", style="bold cyan")

            for student in self.students:
                self.console.print(
                    f"{student.name} - {student.grade}",
                    style="yellow"
                )

    def calculate_average(self):
        if len(self.students) == 0:
            self.console.print("No grades available!", style="red")
        else:
            total = 0

            for student in self.students:
                total += student.grade

            average = total / len(self.students)

            self.console.print(
                f"Average grade: {average:.2f}",
                style="bold green"
            )

    def run(self):
        while True:
            self.console.print(
                "\nStudent Management System",
                style="bold blue"
            )
            self.console.print("1. Add student")
            self.console.print("2. Show students")
            self.console.print("3. Calculate average")
            self.console.print("4. Exit")

            choice = input("\nChoose an option: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.show_students()

            elif choice == "3":
                self.calculate_average()

            elif choice == "4":
                self.console.print("Goodbye!", style="bold blue")
                break

            else:
                self.console.print("Invalid option!", style="bold red")


if __name__ == "__main__":
    app = StudentManagementSystem()
    app.run()
