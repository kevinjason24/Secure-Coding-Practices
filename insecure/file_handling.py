class InsecureFileHandler:
    def __init__(self, base_path):
        self.base_path = base_path

    def read_file(self, filepath):
        """Insecurely read file."""
        # Vulnerable to path traversal
        with open(filepath, 'r') as f:
            return f.read()