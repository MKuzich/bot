from collections import UserList
class NotesManager(UserList):
    def __init__(self):
        self.data = []

    def add_note(self, note):
        self.data.append(note)

    def display_notes(self):
        for note in self.data:
            print("ID:", note.note_id)
            print("Title:", note.title)
            print("Description:", note.description)
            print("Date:", note.date.strftime("%d.%m.%Y"))
            print("Tag:", note.tag)
            print()
        
    def search_note(self, search_query):
        found_notes = []
        search_words = [word.strip().lower() for word in search_query.split(',')]  
        for note in self.data:
            note_text = ' '.join([note.title.lower(), note.description.lower()] + [tag.lower() for tag in note.tag])
            if any(word in note_text for word in search_words):
                found_notes.append(note)
        return found_notes

    def sort_notes_by_tag(self, tag=None):
        if tag is None:
            tag = [] 

        if tag:
            filtered_notes = [
                note for note in self.data
                if any(tag.lower() in [t.lower() for t in note.tag] for tag in tag)
            ]
        else:
            filtered_notes = self.data

        sorted_notes = sorted(
            filtered_notes,
            key=lambda note: (
                min([t.lower() for t in note.tag if t.lower() in [tag.lower() for tag in tag]], default=''),
                note.date
            ),
            reverse=True
        )

        return sorted_notes

