"""Editro controller"""
from prompt_toolkit.formatted_text import HTML
from input_error import input_error
from constants import MESSAGES
from input_handlers import (
    select_contact,
    edit_phone,
    add_email,
    add_address,
    add_phone
)
from helpers.inputs import parse_input
from helpers.ui import (
    get_radio_dialog,
    get_input_dialog,
)

@input_error
def editor(args, contacts):
    if not len(args) == 2:
        return MESSAGES["edit_no_args"]
    attr, name = args
    if attr in ["email", "phone", "address"]:
        contact = select_contact(args, contacts)
        if isinstance(contact, HTML):
            return(contact, name)
    if attr in ["note", "tag"]:
        pass

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
            dialog = get_input_dialog(
                "Add number", "Add telephone number", ""
            )
            new_phone = dialog.run()
            if not new_phone:
                return MESSAGES["canceled"]
            args = name, *parse_input(new_phone)
            return add_phone(args, contacts)

    if attr == "email":
        cur_email = contact.email.email if hasattr(contact.email, "email") else ""
        dialog = get_input_dialog("Edit email", "Edit user email", cur_email)
        edited_email = dialog.run()
        if not edited_email:
            return MESSAGES["canceled"]
        args = name, *parse_input(edited_email)
        return add_email(args, contacts)

    if attr == "address":
        dialog = get_input_dialog(
            "Edit address", "Edit user address:", str(contact.address)
        )
        edited_address = dialog.run()
        if not edited_address:
            return MESSAGES["canceled"]
        args = name, *parse_input(edited_address, delimeter=",", strip=True)
        return add_address(args, contacts)
