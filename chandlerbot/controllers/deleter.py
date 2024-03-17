from prompt_toolkit.formatted_text import HTML
from chandlerbot.input_error import input_error
from chandlerbot.constants import MESSAGES
from chandlerbot.input_handlers import (
    select_contact,
    remove_phone,
    remove_contact,
    remove_email,
    remove_address,
    remove_birthday,
    delete_note
)
from chandlerbot.helpers.ui import (
    get_radio_dialog,
    get_confirm_dialog,
)

@input_error
def deleter(args, contacts, notes_manager):
    name, value = None, None
    if len(args) == 1:
        attr, *_ = args
    elif len(args) == 2:
        attr, name = args
    elif len(args) == 3:
        attr, name, value = args
    else:
        return MESSAGES["not_correct_format"]

    if attr in [ "phone", "email", "address", "birthday", "contact"]:
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

    if attr == "phone":
        if not value:
            if len(contact.phones) == 1:
                value = str(contact.phones[0].value)
            elif len(contact.phones) > 1:
                phones = [(p.value, p.value) for p in contact.phones]
                dialog = get_radio_dialog(
                    "Select phone", phones, "Select phone to remove"
                )
                value = dialog.run()
                if not value:
                    return MESSAGES["canceled"]
            else:
                return MESSAGES["phone_not_set"]
        dialog = get_confirm_dialog(
                    "Phone deletion", "Do you want to delete phone?"
                )
        confirmed = dialog.run()
        if not confirmed:
            return MESSAGES["canceled"]
        return remove_phone((name, value), contacts)

    if attr == "email":
        if not hasattr(contact, "email"):
            return MESSAGES["email_not_set"]
        dialog = get_confirm_dialog(
                    "Email deletion", "Do you want to delete email?"
                )
        confirmed = dialog.run()
        if not confirmed:
            return MESSAGES["canceled"]
        return remove_email(contact.name.value, contacts)

    if attr == "address":
        if  not hasattr(contact, "address"):
            return MESSAGES["address_not_set"]
        dialog = get_confirm_dialog(
                    "Address deletion", "Do you want to delete address?"
                )
        confirmed = dialog.run()
        if not confirmed:
            return MESSAGES["canceled"]
        return remove_address(contact.name.value, contacts)

    if attr == "birthday":
        print(contact)
        if not hasattr(contact, "birthday"):
            return MESSAGES["birthday_not_set"]
        dialog = get_confirm_dialog(
                    "Birthday deletion", "Do you want to delete birthday?"
                )
        confirmed = dialog.run()
        if not confirmed:
            return MESSAGES["canceled"]
        return remove_birthday(contact.name.value, contacts)

    if attr == "contact":
        dialog = get_confirm_dialog(
                    "Contact deletion", "Do you want to delete contact?"
                )
        confirmed = dialog.run()
        if not confirmed:
            return MESSAGES["canceled"]
        return remove_contact(contact.name.value, contacts)

    if attr == "note":
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
        dialog = get_confirm_dialog(
                    "Contact deletion", "Do you want to delete contact?"
                )
        confirmed = dialog.run()
        if not confirmed:
            return MESSAGES["canceled"]
        args = (str(note_id),)
        return delete_note(args, notes_manager)
