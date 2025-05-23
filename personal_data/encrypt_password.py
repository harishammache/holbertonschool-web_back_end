#!/usr/bin/env python3
"""
This module provides functionality for securely hashing passwords using bcrypt.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt and a randomly generated salt.

    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a password against a previously hashed password.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)


if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    encrypted_password = hash_password(password)
    print(encrypted_password)
    print(is_valid(encrypted_password, password))
