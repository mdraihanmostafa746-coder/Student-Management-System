from database import connect_database

connection = connect_database()

if connection is not None:
    print("✅ Database Connected Successfully!")
else:
    print("❌ Database Connection Failed!")
    
    