from input_error import input_error
from errors import NoteSearchError
from datetime import datetime

@input_error
def search_note(args, notes_manager):
    search_query = ' '.join(args).lower()
    found_notes = []

    # Спочатку спробувати пошук за датою
    found_notes = notes_manager.search_notes_by_date(search_query)
    
    # Якщо по даті нічого не знайдено, спробувати текстовий пошук
    if not found_notes:
        found_notes = notes_manager.search_note(search_query)

    if found_notes:
        notes_info = []
        for note in found_notes:
            note_info = f"ID: {note.note_id}, Title: {note.title}, Description: {note.description}, Tags: {note.tag}, Date: {note.date.strftime('%d.%m.%Y')}"
            notes_info.append(note_info)
        return "\n".join(notes_info)
    else:
        raise NoteSearchError
