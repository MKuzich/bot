from input_error import input_error
from models.note import Note


def add_note(notes_manager):
    title = input("Enter the title of the note: ")
    description = input("Enter the description of the note: ")
    tag_input = input("Enter the tag(s) for the note separated by comma: ")
    tag = [tag.strip() for tag in tag_input.split(",")]
    note = Note(title, description, tag=tag)
    notes_manager.add_note(note)
    return "Note added successfully!"
