import datetime


class Note:

    def __init__(self, title, description, date=None, note_id=None, tag=None):
        self.title = title
        self.description = description
        self.date = datetime.datetime.now()
        self.note_id = self.generate_id()
        self.tag = tag if tag is not None else []

    id_counter = 1

    @classmethod
    def generate_id(cls):
        note_id = cls.id_counter
        cls.id_counter += 1
        return note_id
