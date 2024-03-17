from helpers.table_output import table_output
from input_error import input_error
from errors import NoteSearchTagError, NoteEmptyError

@input_error
def sort_notes_by_tag(args, notes_manager):
    if args:
        tags = [arg.strip().lower() for arg in ' '.join(args).split(',')]  
    else:
        raise NoteEmptyError("No tags were provided.")

    sorted_notes = notes_manager.sort_notes_by_tag(tags)
    if not sorted_notes:
        raise NoteSearchTagError("No notes found with those tags.")

    data_for_table = []
    for note in sorted_notes:
        note_id = note.note_id
        note_title = note.title or "?"
        note_description = note.description or "?"
        note_tag = ', '.join(note.tag) or "?"
        note_date = note.date.strftime("%d.%m.%Y")

        data_for_table.append([note_id, note_title, note_description, note_tag, note_date])

    headers = ['ID', 'Title', 'Description', 'Tags', 'Date']
    table_format = "grid"
    missing_value = "?"
    maxcolwidths = [None, 30, 30, 30, 30] 

    return table_output(data_for_table, headers, table_format, missing_value, maxcolwidths)

