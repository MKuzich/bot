from input_error import input_error
from errors import NoteSearchTagError, NoteEmptyError

@input_error
def sort_notes_by_tag(args, notes_manager):
    if args:
        tags = [arg.strip().lower() for arg in ' '.join(args).split(',')]  
    else:
        raise NoteEmptyError

    sorted_notes = notes_manager.sort_notes_by_tag(tags)
    if not sorted_notes:
        raise NoteSearchTagError

    output = []
    for tag in tags:
        output.append(f"Tag: {tag.capitalize()}")
        for note in sorted_notes:
            if tag.lower() in [t.lower() for t in note.tag]:
                note_info = f"ID: {note.note_id}, Title: {note.title}, Description: {note.description}, Tags: {', '.join(note.tag)}, Date: {note.date.strftime('%d.%m.%Y')}"
                output.append(note_info)
    return "\n".join(output)


