from database import connect_database
from student import add_student

connection = connect_database()

if connection is not None:
    print("✅ Database Connected Successfully!")
    add_student(connection)
else:
    print("❌ Database Connection Failed!")
    
    