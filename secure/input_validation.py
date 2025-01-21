from typing import Dict, Optional
import re
import html

class SecureInputValidator:
    def __init__(self):
        self.email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        self.username_pattern = re.compile(r'^[a-zA-Z0-9_]{3,20}$')

    def validate_email(self, email: str) -> bool:
        """Securely validate email format."""
        if not isinstance(email, str):
            return False
        return bool(self.email_pattern.match(email))

    def sanitize_user_input(self, user_input: str) -> str:
        """Sanitize user input to prevent XSS."""
        if not isinstance(user_input, str):
            return ""
        return html.escape(user_input.strip())

    def validate_user_data(self, user_data: Dict) -> Dict[str, str]:
        """Validate and sanitize user registration data."""
        errors = {}
        
        if not user_data.get('username') or not self.username_pattern.match(user_data['username']):
            errors['username'] = "Invalid username format"
            
        if not user_data.get('email') or not self.validate_email(user_data['email']):
            errors['email'] = "Invalid email format"
            
        return errors