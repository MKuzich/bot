from datetime import datetime
from models.field import Field
from errors import NotValidDate

class Birthday(Field):
    def __init__(self, value):
        try:
            day, month, year = map(int, value.split('.'))
            self.value = datetime(year, month, day)
        except:
            raise NotValidDate