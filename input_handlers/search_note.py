from helpers.table_output import table_output
from input_error import input_error
from errors import NoteSearchError

@input_error
def search_note(args, notes_manager):
    """Output note"""
    search_query = ' '.join(args).lower()
    found_notes = []

    # Спочатку спробувати пошук за датою
    found_notes = notes_manager.search_notes_by_date(search_query)

    # Якщо по даті нічого не знайдено, спробувати текстовий пошук
    if not found_notes:
        found_notes = notes_manager.search_note(search_query)

    if found_notes:
        data_for_table = []
        for note in found_notes:
            note_id = note.note_id or "?"
            note_title = note.title or "?"
            note_description = note.description or "?"
            note_date = note.date.strftime("%d.%m.%Y")
            note_tag = note.tag or "?"

            data_for_table.append([note_id, note_title, note_description, note_tag, note_date])
            
    if not found_notes:
        raise NoteSearchError

    #settings for tabulate
    headers = ['ID', 'Title', 'Description', 'Tags', 'Date']
    tablefmt="grid"
    missingval="?"
    maxcolwidths=[None, 30, 30, 30, 30]

    return table_output(data_for_table, headers, tablefmt, missingval,  maxcolwidths)
