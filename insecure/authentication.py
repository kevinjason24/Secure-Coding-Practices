import hashlib

class InsecureAuthentication:
    def hash_password(self, password):
        """Insecurely hash password using MD5."""
        # Vulnerable: Uses weak hashing, no salt
        return hashlib.md5(password.encode()).hexdigest()

    def verify_password(self, password, stored_hash):
        """Insecurely verify password."""
        # Vulnerable: Timing attack possible, weak hash
        return hashlib.md5(password.encode()).hexdigest() == stored_hash