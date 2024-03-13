from input_error import input_error
from models.note import Note


@input_error
def add_note(notes_manager):
    title = input("Enter the title of the note: ")
    description = input("Enter the description of the note: ")
    tag = input("Enter the tag for the note: ")
    note = Note(title, description, tag=tag)
    notes_manager.add_note(note)
    return "Note added successfully!"
