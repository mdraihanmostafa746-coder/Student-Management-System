from database import connect_database
from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student,
)

connection = connect_database()

if connection is not None:

    while True:

        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("\nEnter Your Choice : ")

        if choice == "1":
            add_student(connection)

        elif choice == "2":
            view_students(connection)

        elif choice == "3":
            search_student(connection)

        elif choice == "4":
            update_student(connection)

        elif choice == "5":
            delete_student(connection)

        elif choice == "6":
            print("Thank You For Using Student Management System.")
            break

        else:
            print("Invalid Choice!")

else:
    print("Database Connection Failed!")