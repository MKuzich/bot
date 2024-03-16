from input_error import input_error
from errors import NoteIdNotInList, NoteIdNotCorrect, NoteIdAndTagNotEntered, TagNotEntered

@input_error
def add_tag(args, notes_manager):
    if len(args) == 0 or args[0].strip() == '':
        raise NoteIdAndTagNotEntered

    try:
        note_id = int(args[0])
    except ValueError:
        raise NoteIdNotCorrect

    tags = args[1:]
    if not tags or all(tag.strip() == '' for tag in tags):
        raise TagNotEntered

    for note in notes_manager.data:
        if note.note_id == note_id:
            note.tag.extend(tags)
            return f"Tag {', '.join(tags)} added to note with ID {note_id}."
    raise NoteIdNotInList
