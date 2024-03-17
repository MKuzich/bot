"""Validation inputs"""

from prompt_toolkit.validation import Validator

def is_valid_email(text):
    return "@" in text

email_validator = Validator.from_callable(
    is_valid_email,
    error_message="Not a valid e-mail address (Does not contain an @).",
    move_cursor_to_end=True,
)
