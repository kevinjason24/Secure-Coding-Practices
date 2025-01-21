
import pytest
from secure.authentication import SecureAuthentication
from insecure.authentication import InsecureAuthentication

def test_secure_password_hashing():
    auth = SecureAuthentication()
    password = "MySecurePassword123"
    
    # Test basic hashing
    hashed, salt = auth.hash_password(password)
    assert hashed != password
    assert len(hashed) > 0
    assert len(salt) > 0
    
    # Test verification
    assert auth.verify_password(password, hashed, salt)
    assert not auth.verify_password("WrongPassword", hashed, salt)
    
    # Test against common vulnerabilities
    with pytest.raises(ValueError):
        auth.hash_password(None)
    
    # Test timing attack resistance
    import time
    
    def time_verification(pwd):
        start = time.perf_counter()
        auth.verify_password(pwd, hashed, salt)
        return time.perf_counter() - start
    
    # Times should be similar regardless of password length
    time1 = time_verification("a")
    time2 = time_verification("a" * 1000)
    assert abs(time1 - time2) < 0.1  # Timing difference should be minimal
