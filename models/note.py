import datetime


class Note:

    def __init__(self, title, description, note_id, date=None,  tag=[]):
        self.title = title
        self.description = description
        self.date = datetime.datetime.now()
        self.note_id = note_id
        self.tag = tag
