import pytest
from secure.input_validation import SecureInputValidator
from insecure.input_validation import InsecureInputValidator

def test_secure_email_validation():
    validator = SecureInputValidator()
    
    # Test valid emails
    assert validator.validate_email("test@example.com")
    assert validator.validate_email("user.name+tag@example.co.uk")
    
    # Test invalid emails
    assert not validator.validate_email("invalid.email")
    assert not validator.validate_email("<script>alert('xss')</script>@evil.com")
    assert not validator.validate_email(None)
    assert not validator.validate_email(123)
    assert not validator.validate_email("")

def test_secure_input_sanitization():
    validator = SecureInputValidator()
    
    # Test XSS prevention
    xss_input = "<script>alert('xss')</script>"
    sanitized = validator.sanitize_user_input(xss_input)
    assert "<script>" not in sanitized
    assert sanitized == "&lt;script&gt;alert(&#x27;xss&#x27;)&lt;/script&gt;"
    
    # Test other dangerous inputs
    assert validator.sanitize_user_input('"> <img src="x" onerror="alert(1)">') != '"> <img src="x" onerror="alert(1)">'
    assert validator.sanitize_user_input(None) == ""

def test_secure_user_data_validation():
    validator = SecureInputValidator()
    
    # Test valid user data
    valid_data = {
        'username': 'validuser123',
        'email': 'valid@example.com'
    }
    assert validator.validate_user_data(valid_data) == {}
    
    # Test invalid user data
    invalid_data = {
        'username': 'in valid@user',  # Invalid characters
        'email': 'invalid.email'      # Invalid email format
    }
    errors = validator.validate_user_data(invalid_data)
    assert 'username' in errors
    assert 'email' in errors