"""File for adder controller"""
from input_error import input_error
from constants import MESSAGES
from input_handlers import (
    select_contact,
    add_contact,
    add_birthday,
    add_email,
    add_address,
    add_phone,
    add_note,
)
from helpers.inputs import parse_input
from helpers.ui import (
    get_radio_dialog,
    get_input_dialog,
)


@input_error
def adder(args, contacts, notes_manager, counter):
    name, value = None, None
    if len(args) == 1:
        command, *_ = args
    if len(args) == 2:
        command, name = args
    if len(args) == 3:
        command, name, value = args

    if command == "contact":
        if not name:
            dialog = get_input_dialog("Input name", "Input name of contact", "")
            name = dialog.run()
            if not name:
                return MESSAGES["canceled"]
        if not value:
            dialog = get_input_dialog(
                "Input telephone", "Input telephone for contact", ""
            )
            value = dialog.run()
            if not value:
                return MESSAGES["canceled"]
        args = name, value
        return add_contact(args, contacts)

    if command  == "note":
        if not name:
            dialog = get_input_dialog("Input name", "Input name of note", "")
            name = dialog.run()
            if not name:
                return MESSAGES["canceled"]
        if not value:
            dialog = get_input_dialog(
                "Input description", "Input description for note", ""
            )
            value = dialog.run()
            if not value:
                return MESSAGES["canceled"]
        args = name, value
        note = add_note(args, notes_manager, counter)
        if note == "Note added":
            counter += 1
        return note

    if command == "tag":
        pass

    if command in ["phone", "email", "address", "birthday"]:
        contacts_list = [(c, c) for c, _ in contacts.items()]
        if not name:
            dialog = get_radio_dialog(
                "Select contact", contacts_list, "Please select contact"
            )
            name = dialog.run()
            if not name:
                return MESSAGES["canceled"]
        contact_args = "", name
        contact = select_contact(contact_args, contacts)
        if command == "birthday":
            if not value:
                dialog = get_input_dialog(
                    "Input birthday",
                    "Input birthday for contact, use format<DD:MM:YYYY> :",
                    "",
                )
                value = dialog.run()
                if not value:
                    return MESSAGES["canceled"]
            args = contact, *parse_input(value)
            return add_birthday(args, contacts)

        if command == "email":
            if not value:
                init_text = str(contact.email) if hasattr(contact, "email") else ""
                dialog = get_input_dialog(
                    "Input email",
                    "Input email for contact:",
                    init_text,
                )
                value = dialog.run()
                if not value:
                    return MESSAGES["canceled"]
            args = contact.name.value, *parse_input(value)
            return add_email(args, contacts)

        if command == "phone":
            if not value:
                dialog = get_input_dialog(
                    "Input phone",
                    "Input phone for contact:",
                    "",
                )
                value = dialog.run()
                if not value:
                    return MESSAGES["canceled"]
            args = contact.name.value, *parse_input(value)
            return add_phone(args, contacts)

        if command == "address":
            if not value:
                help_text = "Input address for contact, use format" +\
                      " <street, building, city, postal code, coutnry> :"
                init_text = str(contact.address) if hasattr(contact, "address") else ""
                dialog = get_input_dialog("Input address", help_text, init_text)
                value = dialog.run()
                if not value:
                    return MESSAGES["canceled"]
            args = contact.name.value, *parse_input(value, delimeter=",", strip=True)
            return add_address(args, contacts)
    return MESSAGES["invalid_commad"]
