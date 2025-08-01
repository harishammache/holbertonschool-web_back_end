#!/usr/bin/env python3
"""
    Database connection and session management for user authentication service
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """Database connection and session management class"""

    def __init__(self) -> None:
        """Initialize a new DB instance """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a user to the database"""
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by arbitrary keyword arguments"""
        try:
            for key in kwargs.keys():
                if not hasattr(User, key):
                    raise InvalidRequestError(f"Invalid attribute: {key}")

            user = self._session.query(User).filter_by(**kwargs).one()
            return user

        except AttributeError:
            raise InvalidRequestError("Invalid query arguments")

        except NoResultFound:
            raise NoResultFound("No user found")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user attributes by user ID"""
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if not hasattr(User, key):
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)

        self._session.commit()
