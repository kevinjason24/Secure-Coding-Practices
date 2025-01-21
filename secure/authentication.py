import bcrypt
import secrets
import hmac

class SecureAuthentication:
    def __init__(self):
        self.pepper = secrets.token_bytes(32)  # Server-side secret

    def hash_password(self, password: str) -> tuple[bytes, bytes]:
        """Securely hash password using bcrypt with salt and pepper."""
        if not isinstance(password, str):
            raise ValueError("Password must be a string")
        
        # Add pepper before hashing
        peppered = hmac.new(self.pepper, password.encode(), 'sha256').digest()
        
        # Generate a random salt and hash
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(peppered, salt)
        
        return hashed, salt

    def verify_password(self, password: str, stored_hash: bytes, salt: bytes) -> bool:
        """Securely verify password."""
        if not isinstance(password, str):
            return False
            
        try:
            peppered = hmac.new(self.pepper, password.encode(), 'sha256').digest()
            return hmac.compare_digest(
                bcrypt.hashpw(peppered, salt),
                stored_hash
            )
        except Exception:
            return False