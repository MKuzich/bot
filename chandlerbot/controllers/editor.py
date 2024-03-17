"""Editro controller"""
from prompt_toolkit.formatted_text import HTML
from chandlerbot.input_error import input_error
from chandlerbot.constants import MESSAGES
from chandlerbot.input_handlers import (
    select_contact,
    edit_phone,
    add_email,
    add_address,
    add_phone,
    add_birthday,
    edit_note
)
from chandlerbot.helpers.inputs import parse_input
from chandlerbot.helpers.ui import (
    get_radio_dialog,
    get_input_dialog,
)

@input_error
def editor(args, contacts, notes_manager):
    name, value = None, None
    if len(args) == 1:
        attr, *_ = args
    elif len(args) == 2:
        attr, name = args
    elif len(args) == 3:
        attr, name, value = args
    else:
        return MESSAGES["edit_no_args"]

    if attr in ["email", "phone", "address", "birthday"]:
        if not name:
            contacts_list = [(c, c) for c, _ in contacts.items()]
            dialog = get_radio_dialog(
                "Select contact", contacts_list, "Please select contact"
            )
            name = dialog.run()
            if not name:
                return MESSAGES["canceled"]
        contact_args = "", name
        contact = select_contact(contact_args, contacts)
        if isinstance(contact, HTML):
            return contact

    if attr in ["note", "tag"]:
        notes_list = [(str(note.note_id), note.title) for note in notes_manager.data]
        if not notes_list:
            return MESSAGES["notes_not_found"]
        note_id = value
        if not note_id:
            dialog = get_radio_dialog(
                "Select note", notes_list, "Please select note to edit"
            )
            note_id = dialog.run()
            if not note_id:
                return MESSAGES["canceled"]
        note = notes_manager.get_note(int(note_id))

    if attr == "note":
        field_to_edit = [name] if name else ["title", "description", "tag"]
        result = []
        if "title" in field_to_edit:
            title = note.title if note.title else ""
            dialog = get_input_dialog(
                "Edit note", "Edit title of note", title
            )
            new_title = dialog.run()
            if not new_title:
                return MESSAGES["canceled"]
            args = note_id, "title", new_title
            result.append(edit_note(args, notes_manager))

        if "description" in field_to_edit:
            description = note.description if note.description else ""
            dialog = get_input_dialog(
                "Edit note", "Edit description of note", description
            )
            new_description = dialog.run()
            if not new_description :
                return MESSAGES["canceled"]
            args = note_id, "description", new_description
            result.append(edit_note(args, notes_manager))

        if "tag" in field_to_edit:
            dialog = get_input_dialog(
                "Edit note", "Edit tags for note", note.get_tags()
            )
            new_description = dialog.run()
            if not new_description :
                return MESSAGES["canceled"]
            args = note_id, "tag", new_description
            result.append(edit_note(args, notes_manager))
        return "\n".join(res for res in result)

    if attr == "phone":
        if len(contact.phones) == 1:
            cur_number = str(contact.phones[0].value)
            dialog = get_input_dialog(
                "Edit number", "Edit telephone number", cur_number
            )
            edited_phone = dialog.run()
            if not edited_phone:
                return MESSAGES["canceled"]
            args = name, *parse_input(edited_phone)
            return edit_phone(contacts, *args)
        elif len(contact.phones) > 1:
            phones = [(p.value, p.value) for p in contact.phones]
            dialog = get_radio_dialog(
                "Select phone", phones, "Select phone to edit"
            )
            selected_phone = dialog.run()
            if not selected_phone:
                return MESSAGES["canceled"]
            dialog = get_input_dialog(
                "Edit number", "Edit telephone number", selected_phone
            )
            edited_phone = dialog.run()
            if not edited_phone:
                return MESSAGES["canceled"]
            args = name, selected_phone, edited_phone
            return edit_phone(contacts, *args)
        else:
            default = value if value else ""
            dialog = get_input_dialog(
                "Add number", "Add telephone number", default
            )
            new_phone = dialog.run()
            if not new_phone:
                return MESSAGES["canceled"]
            args = name, *parse_input(new_phone)
        return add_phone(args, contacts)

    if attr == "email":
        if not value:
            value = contact.email.email if hasattr(contact.email, "email") else ""
        dialog = get_input_dialog("Edit email", "Edit user email", value)
        edited_email = dialog.run()
        if not edited_email:
            return MESSAGES["canceled"]
        args = name, *parse_input(edited_email)
        return add_email(args, contacts)

    if attr == "address":
        if not value:
            value = contact.address if hasattr(contact, "address") else ""
        help_text = "Input address for contact, use format" +\
                    " <street,building,city,postal code,coutnry> :"
        dialog = get_input_dialog(
            "Edit address", help_text, str(value)
        )
        edited_address = dialog.run()
        if not edited_address:
            return MESSAGES["canceled"]
        args = name, *parse_input(edited_address, delimeter=",", strip=True, no_lower=True)
        return add_address(args, contacts)

    if attr == "birthday":
        if not value:
            value = contact.get_birthday() if hasattr(contact, "birthday") else ""
        dialog = get_input_dialog(
            "Edit birthday", "Edit user birthday:", str(value)
        )
        edited_birthday = dialog.run()
        if not edited_birthday:
            return MESSAGES["canceled"]
        args = name, *parse_input(edited_birthday)
        return add_birthday(args, contacts)
