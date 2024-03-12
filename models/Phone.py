from models.Field import Field
from errors import NotValidPhoneNumber

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise NotValidPhoneNumber
        self.value = value