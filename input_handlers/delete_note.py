from input_error import input_error


@input_error
def delete_note(args, notes_manager):
    if args:
        note_id = int(args[0])
        for i, note in enumerate(notes_manager.notes):
            if note.note_id == note_id:
                del notes_manager.notes[i]
                return f"Note with ID {note_id} deleted successfully."
        return "Note not found."
    else:
        print("Usage: delete-note <note_id>")
