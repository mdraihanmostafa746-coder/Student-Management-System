DROP DATABASE IF EXISTS xyz_college_db;

CREATE DATABASE xyz_college_db;

USE xyz_college_db;

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL,
    guardian_name VARCHAR(50) NOT NULL,
    email_id VARCHAR(100) UNIQUE,
    contact_no VARCHAR(20) UNIQUE,
    department_name VARCHAR(50) NOT NULL
);

