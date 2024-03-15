from input_error import input_error

@input_error
def sort_notes_by_tag(args, notes_manager):
    if args:
        tag = [arg.strip() for arg in ' '.join(args).split(',')]  # Розділяємо вхідні дані на теги, враховуючи можливість введення декількох тегів через кому
    else:
        tag = None

    sorted_notes = notes_manager.sort_notes_by_tag(tag)
    if sorted_notes:
        notes_info = []
        for note in sorted_notes:
            tag_str = ', '.join(note.tag)
            note_info = f"ID: {note.note_id}, Title: {note.title}, Description: {note.description}, Tags: {tag_str}, Date: {note.date.strftime('%d.%m.%Y')}"
            notes_info.append(note_info)
        return "\n".join(notes_info)
    else:
        return "No notes found with those tags" if tag else "There are no notes."

