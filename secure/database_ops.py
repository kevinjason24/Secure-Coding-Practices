import sqlite3
from typing import Optional, List, Any
from contextlib import contextmanager

class SecureDatabaseOperations:
    def __init__(self, db_path: str):
        self.db_path = db_path

    @contextmanager
    def get_connection(self):
        """Secure database connection management."""
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

    def safe_query(self, query: str, params: tuple) -> List[Any]:
        """Execute parameterized query safely."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(query, params)
                return cursor.fetchall()
            except sqlite3.Error as e:
                # Log error securely
                raise DatabaseError(f"Database error occurred: {type(e).__name__}")

    def get_user_data(self, user_id: int) -> Optional[dict]:
        """Securely retrieve user data."""
        query = "SELECT id, username, email FROM users WHERE id = ?"
        try:
            results = self.safe_query(query, (user_id,))
            return dict(zip(['id', 'username', 'email'], results[0])) if results else None
        except Exception:
            return None

class DatabaseError(Exception):
    pass