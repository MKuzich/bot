class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def display_notes(self):
        for note in self.notes:
            print("ID:", note.note_id)
            print("Title:", note.title)
            print("Description:", note.description)
            print("Date:", note.date.strftime("%d.%m.%Y"))
            print("Tag:", note.tag)
            print()
