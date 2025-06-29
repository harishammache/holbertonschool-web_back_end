#!/usr/bin/env python3
"""
    Empty session
"""


from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """class SessionAuth that inherits from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """instance method"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ instance method """
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ instance method """
        if request is None:
            return None

        session_cookie = self.session_cookie(request)

        if session_cookie is None:
            return None

        user_id = self.user_id_for_session_id(session_cookie)

        if user_id is None:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        """
            Deletes the user session / logout
        """
        if request is None:
            return False
        session_cookie = self.session_cookie(request)

        if session_cookie is None:
            return False

        user_id = self.user_id_for_session_id(session_cookie)

        if user_id is None:
            return False

        del self.user_id_by_session_id[session_cookie]
        return True
