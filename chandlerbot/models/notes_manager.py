from datetime import datetime
from collections import UserList

class NotesManager(UserList):
    def __init__(self):
        self.data = []

    def add_note(self, note):
        self.data.append(note)

    def get_note(self, note_id):
        for note in self.data:
            if note_id == note.note_id:
                return note
    def display_notes(self):
        list_note = []
        for note in self.data:
            list_note.append(note)

        return list_note
        
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

    def date_str_formats(self, note):
        date_formats = [
            note.date.strftime('%d.%m.%Y').lower(),
            note.date.strftime('%d.%m').lower(),
            note.date.strftime('%d %B').lower(),
            note.date.strftime('%B').lower(),
            note.date.strftime('%d').lower(),
            note.date.strftime('%m').lower(),
            note.date.strftime('%m').lstrip('0').lower(),
            note.date.strftime('%Y').lower(),
        ]
        return date_formats

    def search_notes_by_date(self, search_value):
        found_notes = []
        search_value = search_value.lower()
        for note in self.data:
            if any(search_value in format for format in self.date_str_formats(note)):
                found_notes.append(note)
        return found_notes