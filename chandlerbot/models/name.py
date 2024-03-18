from chandlerbot.models.field import Field

class Name(Field):
    def __init__(self, value):
        self.value = value
