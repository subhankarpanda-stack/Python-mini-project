students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    
    marks1 = int(input("Enter marks for Subject 1: "))
    marks2 = int(input("Enter marks for Subject 2: "))
    marks3 = int(input("Enter marks for Subject 3: "))
    
    total = marks1 + marks2 + marks3
    percentage = total / 3
    
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"
    
    student = {
        "Name": name,
        "Roll": roll,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }
    
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    
    for s in students:
        print(s)

def search_student():
    roll = input("Enter roll number to search: ")
    for s in students:
        if s["Roll"] == roll:
            print("Student Found:", s)
            return
    print("Student not found.\n")

def main():
    while True:
        print("===== Student Result Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")
        
        choice = ("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")

main()
