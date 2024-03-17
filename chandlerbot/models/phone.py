from chandlerbot.models.field import Field
from chandlerbot.errors import NotValidPhoneNumber

class Phone(Field):
    def __init__(self, value):
        if (len(value) < 10 or len(value) > 12) or not value.isdigit():
            raise NotValidPhoneNumber
        super().__init__(value)
        