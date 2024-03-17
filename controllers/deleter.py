from prompt_toolkit.formatted_text import HTML
from input_error import input_error
from constants import MESSAGES
from input_handlers import (
    select_contact,
    remove_phone
)
from helpers.ui import (
    get_radio_dialog,
    get_confirm_dialog,
)

@input_error
def deleter(args, contacts, notes_manager):
    attr, name = args
    if not name:
        return MESSAGES["not_correct"]
    if attr in [ "phone", "email", "address", "birthday", "contact"]:
        contact = select_contact(("", name,),contacts,)
        if isinstance(contact, HTML):
            return contact, name
        if attr == "phone":
            if len(contact.phones) == 1:
                cur_number = str(contact.phones[0].value)
                dialog = get_confirm_dialog(
                    "Phone deletion", "Do you want to delete phone?"
                )
                confirmed = dialog.run()
                if not confirmed:
                    return MESSAGES["canceled"]
                return remove_phone((name, cur_number), contacts)
            elif len(contact.phones) > 1:
                phones = [(p.value, p.value) for p in contact.phones]
                dialog = get_radio_dialog(
                    "Select phone", phones, "Select phone to remove"
                )
                selected_phone = dialog.run()
                if not selected_phone:
                    return MESSAGES["canceled"]
                dialog = get_confirm_dialog(
                    "Phone deletion", "Do you want to delete phone?"
                )
                confirmed = dialog.run()
                if not confirmed:
                    return MESSAGES["canceled"]
                return remove_phone((name, selected_phone), contacts)
            else:
                return MESSAGES["phone_not_set"]
        if attr == "email":
            return MESSAGES["dev"]
        if attr == "address":
            return MESSAGES["dev"]
        if attr == "birtday":
            return MESSAGES["dev"]
        if attr == "contact":
            return MESSAGES["dev"]

    if attr in [ "note", "tag"]:
        pass
