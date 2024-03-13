from input_error import input_error


@input_error
def show_note(args, notes_manager):
    if args:
        note_id = int(args[0])
        for note in notes_manager.notes:
            if note.note_id == note_id:
                print("ID:", note.note_id)
                print("Title:", note.title)
                print("Description:", note.description)
                print("Date:", note.date.strftime("%d.%m.%Y"))
                print("Tag:", note.tag)
                return ""
        print("Note not found.")
        return ""
    else:
        print("Usage: show-note <note_id>")
        return ""
