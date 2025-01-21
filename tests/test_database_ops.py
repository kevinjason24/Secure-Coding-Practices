import pytest
import sqlite3
from secure.database_ops import SecureDatabaseOperations, DatabaseError
from insecure.database_ops import InsecureDatabaseOperations

@pytest.fixture
def setup_database():
    # Create test database
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    cursor.execute("INSERT INTO users VALUES (1, 'testuser', 'test@example.com')")
    conn.commit()
    return conn

def test_secure_database_operations(setup_database):
    db = SecureDatabaseOperations(':memory:')
    
    # Test safe query execution
    result = db.safe_query("SELECT * FROM users WHERE id = ?", (1,))
    assert result[0][1] == 'testuser'
    
    # Test SQL injection prevention
    with pytest.raises(DatabaseError):
        db.safe_query("SELECT * FROM users WHERE id = " + "1; DROP TABLE users;", ())
    
    # Test parameter validation
    assert db.get_user_data(1) is not None
    assert db.get_user_data("1; DROP TABLE users;") is None
