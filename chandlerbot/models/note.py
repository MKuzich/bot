import datetime


class Note:
    
    def __init__(self, title, description, note_id, date=None, tag=None):
        self.title = title
        self.description = description
        self.date = date if date else datetime.datetime.now()
        self.note_id = note_id
        self.tag = tag if tag else []

    def get_tags(self,):
        tags=""
        for tag in self.tag:
            tags +=f"{tag},"
        return tags.rstrip(",")
