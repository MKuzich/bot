from helpers.table_output import table_output
from input_error import input_error
from errors import NoNotes

@input_error
def show_all_notes(notes):
    data_for_table = []

    for note in notes.display_notes():
        note_id = note.note_id or "?"
        note_title = note.title or "?"
        note_description = note.description or "?"
        note_date = note.date.strftime("%d.%m.%Y")
        note_tag = note.tag or "?"
        data_for_table.append([note_id, note_title, note_description, note_date, note_tag])

    if not data_for_table:
        raise NoNotes

    #settings for tabulate
    headers = ['ID', 'Title', 'Description', 'Date', 'Tags']
    tablefmt="grid"
    missingval="?"
    maxcolwidths=[None, 30, 30, 30, 30]

    return table_output(data_for_table, headers, tablefmt, missingval,  maxcolwidths)
