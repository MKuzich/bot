from input_error import input_error


@input_error
def edit_note(args, notes_manager):
    if args:
        note_id = int(args[0])
        for note in notes_manager.notes:
            if note.note_id == note_id:
                title = input(
                    f"Current title: {note.title}\nEnter the new title of the note (or press Enter to keep the current title): "
                )
                if title:
                    note.title = title

                description = input(
                    f"Current description: {note.description}\nEnter the new description of the note (or press Enter to keep the current description): "
                )
                if description:
                    note.description = description

                tag_input = input(
                    f"Current tag(s): {', '.join(note.tag)}\nEnter the new tag(s) for the note separated by comma (or press Enter to keep the current tag(s)): "
                )
                if tag_input:
                    tag = [tag.strip() for tag in tag_input.split(",")]
                    note.tag = tag

                return print("Note edited successfully!")
        else:
            print("Note not found.")
    else:
        print("Usage: edit-note <note_id>")
