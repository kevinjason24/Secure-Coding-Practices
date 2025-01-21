# Secure vs Insecure Coding Practices in Python

A comprehensive demonstration of secure coding practices in Python, comparing secure implementations against common vulnerable patterns. This educational project helps developers understand security vulnerabilities and learn how to prevent them.

## Security Concepts Covered

- Input Validation & Sanitization
- Secure Password Hashing & Storage
- SQL Injection Prevention
- Secure File Handling & Path Traversal Prevention
- XSS Attack Prevention
- Safe Database Operations

## Project Structure
```
├── README.md
├── requirements.txt
├── secure/
│   ├── __init__.py
│   ├── input_validation.py
│   ├── authentication.py
│   ├── database_ops.py
│   └── file_handling.py
├── insecure/
│   ├── __init__.py
│   ├── input_validation.py
│   ├── authentication.py
│   ├── database_ops.py
│   └── file_handling.py
└── tests/
    ├── __init__.py
    ├── test_input_validation.py
    ├── test_authentication.py
    ├── test_database_ops.py
    └── test_file_handling.py
```

## ⚠️ Warning

The code in the `insecure/` directory contains intentionally vulnerable implementations for educational purposes. These examples demonstrate common security pitfalls and should **never** be used in production environments.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/secure-coding-practices-python.git
cd secure-coding-practices-python
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the demonstration script:
```bash
python main.py
```

The script demonstrates:
- Email validation and input sanitization
- Secure password hashing and verification
- Safe file operations with path validation
- Secure database operations

## Security Features Demonstrated

### 1. Input Validation
- Email format validation
- Input sanitization
- XSS prevention
- Data type checking

### 2. Authentication
- Secure password hashing using bcrypt
- Salt generation and management
- Timing attack prevention
- Secure password verification

### 3. File Handling
- Path traversal prevention
- Safe file operations
- Directory access control
- File permission management

### 4. Database Operations
- SQL injection prevention
- Parameterized queries
- Input sanitization
- Safe data retrieval

## Running Tests

Execute the test suite:
```bash
pytest tests/
```

## Acknowledgments

- Based on OWASP Secure Coding Practices
- Inspired by common security vulnerabilities and their preventions
- Created for educational purposes to promote secure coding practices

