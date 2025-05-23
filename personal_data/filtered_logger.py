#!/usr/bin/env python3
"""
    function called filter_datum that returns the log message obfuscated
"""


import re
import logging
from typing import List
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields, redaction, message, separator):
    """
        - fields: a list of strings representing all fields to obfuscate
        - redaction: a string representing by what the field will be obfuscated
        - message: a string representing the log line
        - separator: a string representing by which character is separating
        all fields in the log line
    """
    pattern = r'(' + '|'.join(fields) + r')=.*?' + re.escape(separator)
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}{separator}",
                  message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original_message,
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger with redacting formatter.
    Returns:
        A logging.Logger instance configured to filter PII.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Connects to a MySQL database using credentials from environment variables.
    
    Returns:
        A MySQLConnection object to the database.
    """
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )

def main() -> None:
    """
    Main entry point for retrieving and logging user data with PII redaction.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields: List[str] = [desc[0] for desc in cursor.description]
    logger = get_logger()
    for row in cursor:
        row_dict = dict(zip(fields, row))
        log_message = "; ".join(
            [f"{key}={value}" for key, value in row_dict.items()])
        filtered_message = filter_datum(PII_FIELDS, "***", log_message, "; ")
        logger.info(filtered_message)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()