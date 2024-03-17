from helpers.table_output import table_output
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

    data_for_table = []
    for tag in tags:
        #data_for_table.append(f"Tag: {tag.capitalize()}")
        for note in sorted_notes:
            if tag.lower() in [t.lower() for t in note.tag]:
                note_id = note.note_id
                note_title = note.title or "?"
                note_description = note.description or "?"
                note_tag = ', '.join(note.tag) or "?"
                note_date = note.date.strftime("%d.%m.%Y")

                data_for_table.append([note_id, note_title, note_description, note_tag, note_date])

    #settings for tabulate
    headers=['ID', 'Title', 'Description', 'Tags', 'Date']
    tablefmt="grid"
    missingval="?"
    maxcolwidths=[None, 30, 30, 30, 30]

    return table_output(data_for_table, headers, tablefmt, missingval,  maxcolwidths)
