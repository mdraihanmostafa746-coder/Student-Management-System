import mysql.connector


def add_student(connection):
    try:
        cursor = connection.cursor()

        student_name = input("Enter student name : ")
        guardian_name = input("Enter guardian name : ")
        email_id = input("Enter email id : ")
        contact_no = input("Enter mobile number : ")
        department_name = input("Enter department name : ")

        query = """
        INSERT INTO students
        (student_name, guardian_name, email_id, contact_no, department_name)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            student_name,
            guardian_name,
            email_id,
            contact_no,
            department_name
        )

        cursor.execute(query, values)
        connection.commit()

        print("Student Added Successfully!")

        cursor.close()

    except Exception as error:
        print("Error :", error)
        connection.rollback()

def view_students(connection):
    try:
        cursor = connection.cursor()

        query = "SELECT * FROM students"

        cursor.execute(query)

        rows = cursor.fetchall()

        if rows:

            print("\n========== STUDENT LIST ==========\n")

            for row in rows:
                print(f"Student ID      : {row[0]}")
                print(f"Student Name    : {row[1]}")
                print(f"Guardian Name   : {row[2]}")
                print(f"Email ID        : {row[3]}")
                print(f"Contact Number  : {row[4]}")
                print(f"Department      : {row[5]}")
                print("-" * 40)

        else:
            print("No Student Found!")

        cursor.close()

    except Exception as error:
        print("Error :", error)


def search_student(connection):
    try:
        cursor = connection.cursor()

        student_id = input("Enter Student ID : ")

        query = "SELECT * FROM students WHERE student_id = %s"

        cursor.execute(query, (student_id,))

        row = cursor.fetchone()

        if row:
            print(row)
        else:
            print("Student Not Found!")

        cursor.close()

    except Exception as error:
        print("Error :", error)


def update_student(connection):
    try:
        cursor = connection.cursor()

        student_id = input("Enter Student ID : ")

        check_query = "SELECT * FROM students WHERE student_id = %s"
        cursor.execute(check_query, (student_id,))
        row = cursor.fetchone()

        if row is None:
            print("Student Not Found!")
            cursor.close()
            return

        student_name = input("Enter New Student Name : ")
        guardian_name = input("Enter New Guardian Name : ")
        email_id = input("Enter New Email ID : ")
        contact_no = input("Enter New Mobile Number : ")
        department_name = input("Enter New Department Name : ")

        query = """
        UPDATE students
        SET student_name=%s,
            guardian_name=%s,
            email_id=%s,
            contact_no=%s,
            department_name=%s
        WHERE student_id=%s
        """

        values = (
            student_name,
            guardian_name,
            email_id,
            contact_no,
            department_name,
            student_id
        )

        cursor.execute(query, values)

        connection.commit()

        print("Student Updated Successfully!")

        cursor.close()

    except Exception as error:
        print("Error :", error)
        connection.rollback()


def delete_student(connection):
    try:
        cursor = connection.cursor()

        student_id = input("Enter Student ID : ")

        check_query = "SELECT * FROM students WHERE student_id = %s"
        cursor.execute(check_query, (student_id,))
        row = cursor.fetchone()

        if row is None:
            print("Student Not Found!")
            cursor.close()
            return

        choice = input("Are you sure? (yes/no) : ").lower()

        if choice == "yes":

            query = "DELETE FROM students WHERE student_id = %s"

            cursor.execute(query, (student_id,))

            connection.commit()

            print("Student Deleted Successfully!")

        else:
            print("Delete Cancelled!")

        cursor.close()

    except Exception as error:
        print("Error :", error)
        connection.rollback()