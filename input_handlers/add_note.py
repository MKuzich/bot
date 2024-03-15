from input_error import input_error
from models import Note


@input_error
def add_note(args, notes_manager):
    title = args[0]
    description = " ".join(args[1:])
    note = Note(title, description)
    notes_manager.add_note(note)
    return "Note added"
