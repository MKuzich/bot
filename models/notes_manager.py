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
    
    def search_note(self, word):
        found_notes = []
        for note in self.notes:
            if word.lower() in note.title.lower() or word.lower() in note.description.lower() or word.lower() in note.tag.lower() or word.lower() in note.date.strftime("%d.%m.%Y"):
                found_notes.append(note)
        return found_notes
    
    def sort_notes_by_tag(self, tag=None):
        if tag:
            filtered_notes = [note for note in self.notes if note.tag.lower() == tag.lower()]
        else:
            # Якщо тег не заданий, тоді працює з усіма нотатками
            filtered_notes = self.notes

        sorted_notes = sorted(filtered_notes, key=lambda note: note.date, reverse=True)
        return sorted_notes