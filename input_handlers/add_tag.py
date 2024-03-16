from input_error import input_error
from errors import NoteIdNotInList, NoteIdNotCorrect, NoteIdNotEntered

@input_error
def add_tag(args, notes_manager):
    if len(args) == 0 or args[0].strip() == '':
        raise NoteIdNotEntered("Note ID must be entered.")

    try:
        note_id = int(args[0])
    except ValueError:
        raise NoteIdNotCorrect("Note ID must be an integer.")

    tags = args[1:]
    for note in notes_manager.data:
        if note.note_id == note_id:
            note.tag.extend(tags)
            return f"Tag {', '.join(tags)} added to note with ID {note_id}."
    raise NoteIdNotInList
