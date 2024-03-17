from datetime import datetime
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

    def sort_notes_by_tag(self, tags=None):
        if tags is None:
            tags = []

        tag_set = set(tag.lower() for tag in tags)
        
        def tag_match_count(note):
            note_tags = set(t.lower() for t in note.tag)
            match_count = len(tag_set & note_tags) 
            return (match_count, note.date)
        
        sorted_notes = sorted(self.data, key=tag_match_count, reverse=True)

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
    