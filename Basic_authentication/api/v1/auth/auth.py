#!/usr/bin/env python3
"""
    create a class to manage the API authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """class auth"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method"""
        if path is None or excluded_paths is None:
            return True
        
        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False
        
        if not path.endswith('/'):
            path = path + '/'
        
        return True

    def authorization_header(self, request=None) -> str:
        """public method"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """public method"""
        return None
