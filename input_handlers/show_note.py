from tabulate import tabulate
from input_error import input_error
from errors import NoteEmptyError, NoteValueArgsError

@input_error
def show_note(args, notes_manager):
    if not args or args[0].isalpha():
        raise NoteValueArgsError

    note_id = int(args[0])
    data_for_table = []

    #
    for note in notes_manager.data:
        if note_id == note.note_id:
            note_title = note.title or "?"
            note_description = note.description or "?"
            note_date = note.date.strftime("%d.%m.%Y")
            note_tag = note.tag or "?"
            data_for_table.append([note_id, note_title, note_description, note_date, note_tag])

    if not data_for_table:
        raise NoteEmptyError

    return "\n" + tabulate(data_for_table, headers=['ID', 'Title', 'Description', 'Date', 'Tags'], tablefmt="grid", missingval="?", maxcolwidths=[None, 30, 30, 30, 30]) + "\n"
