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

    # Перетворення тегів на малі літери
    new_tags = [tag.strip().lower() for tag in tags if tag.strip() != '']

    for note in notes_manager.data:
        if note.note_id == note_id:
            # Додаємо унікальні теги, зберігаючи порядок
            for tag in new_tags:
                if tag not in note.tag:
                    note.tag.append(tag)
            return f"Tag {', '.join(new_tags)} added to note with ID {note_id}."
    raise NoteIdNotInList
