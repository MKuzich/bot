from datetime import datetime
from chandlerbot.models.field import Field
from chandlerbot.errors import NotValidDate

class Birthday(Field):
    def __init__(self, value):
        try:
            day, month, year = map(int, value.split('.'))
            self.value = datetime(year, month, day)
        except:
            raise NotValidDate