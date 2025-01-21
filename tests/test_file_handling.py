import pytest
import os
from secure.file_handling import SecureFileHandler
from insecure.file_handling import InsecureFileHandler

@pytest.fixture
def setup_test_files(tmp_path):
    # Create test files
    test_file = tmp_path / "test.txt"
    test_file.write_text("Test content")
    return tmp_path

def test_secure_file_handling(setup_test_files):
    handler = SecureFileHandler(str(setup_test_files))
    
    # Test path traversal prevention
    assert not handler.is_safe_path("../../../etc/passwd")
    assert handler.is_safe_path(str(setup_test_files / "test.txt"))
    
    # Test file validation
    test_file = setup_test_files / "test.txt"
    with open(test_file, 'rb') as f:
        content = f.read()
        assert handler.validate_file(str(test_file), content)
    
    # Test size limits
    large_file = setup_test_files / "large.txt"
    large_file.write_bytes(b"0" * (11 * 1024 * 1024))  # 11MB
    with open(large_file, 'rb') as f:
        content = f.read()
        assert not handler.validate_file(str(large_file), content)

def test_secure_file_reading(setup_test_files):
    handler = SecureFileHandler(str(setup_test_files))
    
    # Test safe file reading
    content = handler.safe_read_file(str(setup_test_files / "test.txt"))
    assert content is not None
    assert b"Test content" in content
    
    # Test reading non-existent file
    assert handler.safe_read_file("nonexistent.txt") is None
    
    # Test path traversal
    assert handler.safe_read_file("../../../etc/passwd") is None