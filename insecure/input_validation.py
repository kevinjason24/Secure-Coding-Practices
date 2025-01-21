class InsecureInputValidator:
    def validate_email(self, email):
        """Insecurely validate email format."""
        # Vulnerable to injection and invalid input
        return '@' in email and '.' in email

    def sanitize_user_input(self, user_input):
        """No sanitization of user input - vulnerable to XSS."""
        return user_input

    def validate_user_data(self, user_data):
        """Minimal validation that can be bypassed."""
        return {} if '@' in user_data.get('email', '') else {'email': 'Invalid email'}
