from pathlib import Path
from typing import Optional
import os
import mimetypes

class SecureFileHandler:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path).resolve()
        self.allowed_extensions = {'.txt', '.pdf', '.png', '.jpg', '.jpeg'}
        self.max_file_size = 10 * 1024 * 1024  # 10MB

    def is_safe_path(self, filepath: str) -> bool:
        """Prevent path traversal attacks."""
        try:
            file_path = Path(filepath).resolve()
            common_path = os.path.commonpath([file_path, self.base_path])
            return common_path.startswith(str(self.base_path))
        except Exception:
            return False

    def validate_file(self, file_path: str, content: bytes) -> bool:
        """Validate file type and size."""
        if not self.is_safe_path(file_path):
            return False

        if len(content) > self.max_file_size:
            return False

        # Check file extension
        ext = Path(file_path).suffix.lower()
        if ext not in self.allowed_extensions:
            return False

        # Basic MIME type check using mimetypes
        mime_type, _ = mimetypes.guess_type(file_path)
        allowed_mimes = {'text/plain', 'application/pdf', 'image/jpeg', 'image/png'}
        
        return mime_type in allowed_mimes

    def safe_read_file(self, filepath: str) -> Optional[bytes]:
        """Securely read file contents."""
        if not self.is_safe_path(filepath):
            return None

        try:
            with open(filepath, 'rb') as f:
                content = f.read()
                if self.validate_file(filepath, content):
                    return content
                return None
        except Exception:
            return None

