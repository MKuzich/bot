from input_error import input_error


@input_error
def edit_note(args, notes_manager):
    if len(args) < 2:
        print("Usage: edit-note <note_id> <field> <new_value>")
        return

    note_id = int(args[0])
    field = args[1].lower()
    new_value = " ".join(args[2:])

    for note in notes_manager.data:
        if note.note_id == note_id:
            if field == "title":
                note.title = new_value
                return print(f"Title for note {note_id} changed")
            elif field == "description":
                note.description = new_value
                return print(f"Description for note {note_id} changed")
            elif field == "tag":
                note.tag = new_value.split(",")
                return print(f"Tag for note {note_id} changed")
            else:
                return print("Invalid field. Allowed fields: title, description, tag.")
    else:
        return "Note not found."
