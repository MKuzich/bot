from chandlerbot.input_error import input_error
from chandlerbot.errors import NoteFormatError
from chandlerbot.models import Note


@input_error
def add_note(args, notes_manager, counter):
    if len(args) < 2:
        raise NoteFormatError
    title = args[0]
    description = " ".join(args[1:])
    note = Note(title, description, counter)
    notes_manager.add_note(note)
    return "Note added"
