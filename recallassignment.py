students = []

subjects = ("Maths", "Physics", "Chemistry")

marks = {}

while True:
    print("\n.Student Data Menu ")
    print("1. Add Student Name (List)")
    print("2. Show Subjects (Tuple)")
    print("3. Enter Student Marks (Dictionary)")
    print("4. Show Unique Marks (Set)")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully")
        print("Student List:", students)

    elif choice == 2:
        print("Subjects are:", subjects)

    elif choice == 3:
        name = input("Enter student name: ")
        mark = int(input("Enter marks: "))
        marks[name] = mark
        print("Marks stored successfully")
        print("Student Marks:", marks)

    elif choice == 4:
        unique_marks = set(marks.values())
        print("Unique Marks:", unique_marks)

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid choice")