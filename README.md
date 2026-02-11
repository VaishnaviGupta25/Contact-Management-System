
# Contact Management System (CLI-Based)

## Project Overview

This project is a **Contact Management System** developed using **Python** as a Command Line Interface (CLI) application. It allows users to manage contacts efficiently using CRUD operations while storing data in a JSON file.

The application supports adding, viewing, searching, updating, and deleting contacts with proper validation and logging mechanisms.

Contacts are not permanently removed; instead, a **soft delete mechanism** is implemented.

---

## Features Implemented

### 1. Add New Contact

Users can add contacts with the following details:

* Name
* Phone number
* Email
* Address (optional)

Validations applied:

* Name cannot be empty.
* Phone number must contain exactly 10 digits.
* Email must be in correct format.
* Duplicate phone numbers are not allowed.

---

### 2. View All Contacts

Displays all available contacts in a formatted list while excluding deleted contacts.

---

### 3. Search Contact

Contacts can be searched using:

* Name
* Phone number

Search is case-insensitive for names.

---

### 4. Update Contact

Allows updating:

* Name
* Phone number
* Email

Validations are applied during updates, and duplicate phone numbers are prevented.

---

### 5. Delete Contact (Soft Delete)

Contacts are not removed permanently. Instead:

```
is_deleted = True
```

is applied so records remain stored but hidden.

---

## Storage Mechanism

Contacts are stored using a JSON file:

```
contacts.json
```

Example structure:

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "phone": "9876543210",
    "email": "john@example.com",
    "address": "Delhi",
    "is_deleted": false
  }
]
```

---

## Bonus Features Implemented

* Object-Oriented Programming (OOP) approach.
* Logging using Python logging module.
* Log file (`contacts.log`) records add, update, and delete actions.

---

## Project Structure

```
project_folder/
│
├── contact_manager.py
├── contacts.json
├── contacts.log
└── README.md
```

---

## Steps to Run the Project

### Step 1: Install Python

Ensure Python 3.x is installed.

Check version:

```bash
python --version
```

---

### Step 2: Download or Clone Project

Copy project files or clone repository.

---

### Step 3: Run Program

Execute:

```bash
python contact_manager.py
```

---

### Step 4: Use Menu Options

Select operations from CLI menu:

```
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
```

---

## Evaluation Compliance

This project satisfies evaluation requirements:

* Code readability and structure
* Proper validations
* JSON storage usage
* Error handling
* Logging support
* Clean output formatting

---

## Possible Future Improvements

* Flask API version
* Database integration
* CSV import/export
* User authentication
* GUI interface
* Contact grouping

---

## Author

Vaishnavi Gupta
B.Tech Computer Science | Python Developer

---


