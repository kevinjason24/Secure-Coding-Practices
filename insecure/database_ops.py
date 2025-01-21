import sqlite3

class InsecureDatabaseOperations:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_user_data(self, user_id):
        """Insecurely retrieve user data."""
        # Vulnerable to SQL injection
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
        return cursor.fetchone()