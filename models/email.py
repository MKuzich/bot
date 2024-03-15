"""File for Email class"""
import re
from models.field import Field
from errors import EmailNotCorrect
from constants import EMAIL_PATTERN

class Email(Field):
    """Email field for contact"""
    def __init__(self, email):
        self.__email = None
        self.email = email
        super().__init__(email)

    @property
    def email(self):
        """Return email"""
        return self.__email

    @email.setter
    def email(self, email):
        """Setter for email"""
        if not re.match(EMAIL_PATTERN, email):
            raise EmailNotCorrect
        self.__email = email

    def __str__(self):
        return self.__email