# 🎓 Student Management System

A simple **Student Management System** built using **Python** and **MySQL**. This is a command-line (CLI) application that allows users to manage student records with complete CRUD (Create, Read, Update, Delete) operations.

---

# 📌 Project Overview

The Student Management System is designed to manage student information efficiently using Python and MySQL.

This project demonstrates:

- Python Modular Programming
- MySQL Database Connectivity
- CRUD Operations
- Exception Handling
- Environment Variables (.env)
- Git & GitHub Version Control

---

# ✨ Features

- ➕ Add Student
- 📋 View All Students
- 🔍 Search Student by ID
- ✏️ Update Student Details
- 🗑 Delete Student
- 🔐 Secure Database Credentials using `.env`
- ⚠ Error Handling
- 💾 MySQL Database Integration

---

# 📂 Folder Structure

```text
Student-Management-System/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── database.py
├── student.py
└── sql/
    └── student_management.sql
```

---

# 🛠 Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- python-dotenv
- Git
- GitHub
- VS Code

---

# ⚙ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Student-Management-System.git
```

---

## 2. Move into the Project Folder

```bash
cd Student-Management-System
```

---

## 3. Create Virtual Environment

### Windows

```bash
python -m venv venv
```

### macOS / Linux

```bash
python3 -m venv venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Setup

Open MySQL and execute:

```sql
SOURCE sql/student_management.sql;
```

This will automatically create:

- Database
- Students Table

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=xyz_college_db
```

> ⚠ Never upload your `.env` file to GitHub.

---

# ▶ How to Run

Run the application:

```bash
python main.py
```

or

```bash
python3 main.py
```

---

Example:

- Main Menu
- Add Student
- View Students
- Search Student
- Update Student
- Delete Student

---

# 🚀 Future Improvements

- Input Validation
- Email Validation
- Mobile Number Validation
- Better Table Formatting
- Login System
- GUI Version (Tkinter)
- Flask Web Version
- Django Version
- AI-powered Student Analytics

---

# 👨‍💻 Author

**Md Raihan Mostafa**

- GitHub: https://github.com/mdraihanmostafa746-coder

---

# 📄 License

This project is developed for learning purposes.

