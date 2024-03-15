from input_error import input_error


@input_error
def add_tag(args, notes_manager):
    note_id = int(args[0])
    tags = args[1:]
    for note in notes_manager.data:
        if note.note_id == note_id:
            note.tag.extend(tags)
            return f"Tag {', '.join(tags)} added to note with ID {note_id}."
    return "Note not found."
