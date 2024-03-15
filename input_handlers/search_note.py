from input_error import input_error

@input_error
def search_note(args, notes_manager):
    word = ' '.join(args)
    found_notes = notes_manager.search_note(word)
    if found_notes:
        notes_info = []
        for note in found_notes:
            note_info = f"ID: {note.note_id}, Title: {note.title}, Description: {note.description}, Tags: {note.tag}, Date: {note.date.strftime('%d.%m.%Y')}"
            notes_info.append(note_info)
        return "\n".join(notes_info)
    else:
        return "No notes found with that word"