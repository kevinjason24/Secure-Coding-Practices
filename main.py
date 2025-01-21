import os
from secure.input_validation import SecureInputValidator
from secure.authentication import SecureAuthentication
from secure.database_ops import SecureDatabaseOperations
from secure.file_handling import SecureFileHandler

def demonstrate_input_validation():
    print("\n=== Input Validation Demo ===")
    validator = SecureInputValidator()
    
    # Email validation
    test_emails = [
        "valid.user@example.com",
        "invalid@email",
        "<script>alert('xss')</script>@evil.com"
    ]
    
    for email in test_emails:
        result = validator.validate_email(email)
        print(f"Email '{email}': {'Valid' if result else 'Invalid'}")
    
    # Input sanitization
    dangerous_input = "<script>alert('xss')</script>"
    safe_output = validator.sanitize_user_input(dangerous_input)
    print(f"\nOriginal input: {dangerous_input}")
    print(f"Sanitized output: {safe_output}")

def demonstrate_authentication():
    print("\n=== Authentication Demo ===")
    auth = SecureAuthentication()
    
    # Password hashing and verification
    test_password = "SecurePass123!"
    print(f"Original password: {test_password}")
    
    hashed, salt = auth.hash_password(test_password)
    print(f"Hashed password (first 20 chars): {hashed[:20]}...")
    
    # Verify correct and incorrect passwords
    is_valid = auth.verify_password(test_password, hashed, salt)
    is_invalid = auth.verify_password("WrongPassword", hashed, salt)
    
    print(f"Correct password verification: {is_valid}")
    print(f"Incorrect password verification: {is_invalid}")

def demonstrate_file_handling():
    print("\n=== File Handling Demo ===")
    # Create a temporary test file
    base_path = os.path.dirname(os.path.abspath(__file__))
    handler = SecureFileHandler(base_path)
    
    test_file_path = os.path.join(base_path, "test.txt")
    with open(test_file_path, "w") as f:
        f.write("Test content")
    
    # Demonstrate path validation
    print(f"Safe path check for 'test.txt': {handler.is_safe_path(test_file_path)}")
    print(f"Safe path check for '../etc/passwd': {handler.is_safe_path('../etc/passwd')}")
    
    # Read file content
    content = handler.safe_read_file(test_file_path)
    print(f"Safe file read result: {content is not None}")
    
    # Cleanup
    os.remove(test_file_path)

def main():
    print("Secure Coding Practices Demonstration")
    print("====================================")
    
    try:
        demonstrate_input_validation()
        demonstrate_authentication()
        demonstrate_file_handling()
        
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
    
    print("\nDemonstration completed.")

if __name__ == "__main__":
    main()