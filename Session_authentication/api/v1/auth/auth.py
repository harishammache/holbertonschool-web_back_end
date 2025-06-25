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
        if path is None or not excluded_paths:
            return True

        if not path.endswith('/'):
            path = path + '/'

        for excluded_path in excluded_paths:
            if not excluded_path.endswith('/'):
                excluded_path += '/'

            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """public method"""
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """public method"""
        return None
