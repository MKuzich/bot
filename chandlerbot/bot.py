"""Index bot file"""

from prompt_toolkit import print_formatted_text
from chandlerbot.data_handlers import save_data, load_data
from chandlerbot.models import AddressBook, NotesManager
from chandlerbot.input_handlers import (
    show_contact,
    all_contacts,
    birthdays,
    show_birthday,
    show_address,
    add_note,
    add_tag,
    edit_note,
    delete_note,
    show_note,
    search_note,
    sort_notes_by_tag,
    search_contact,
    show_all_notes,
)
from chandlerbot.controllers import editor, deleter, adder
from chandlerbot.helpers.ui import (
    style,
    get_bottom_toolbar
)
from chandlerbot.helpers.session import get_completer, open_session
from chandlerbot.helpers.weather import get_weather_info
from chandlerbot.helpers.inputs import parse_input
from chandlerbot.constants import NONE_COMMANDS, HELP_TEXT, HI_TEXT, PROMT, MESSAGES


print = print_formatted_text
weather_info = get_weather_info()

def main():
    """Main bot functions"""

    def get_toolbar():
        return get_bottom_toolbar(contacts, notes_manager, weather_info)

    counter = 1
    contacts = AddressBook()
    notes_manager = NotesManager()

    try:
        contacts, notes_manager, counter = load_data()
    except FileNotFoundError:
        pass
    session = open_session(NONE_COMMANDS, contacts, notes_manager, style)
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = session.prompt(
                PROMT, bottom_toolbar=get_toolbar, refresh_interval=0.5
            )
        except KeyboardInterrupt:
            # pressed ctrl+C
            user_input = "help"
        except EOFError:
            print("Good bye!")
            save_data(contacts, notes_manager, counter)
            break

        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "quit"]:
            print("Good bye!")
            save_data(contacts, notes_manager, counter)
            break
        elif command in ["hello", "hi", "hey", "yo", "sup"]:
            print(HI_TEXT)
        elif command in ["help"]:
            print(HELP_TEXT)
        elif command in ["add", "create", "new"]:
            print(adder(args, contacts, notes_manager, counter))
        elif command in ["change", "edit", "update"]:
            print(editor(args, contacts, notes_manager))
        elif command in ["delete", "remove", "drop"]:
            print(deleter(args, contacts, notes_manager))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        elif command == "birthdays":
            print(birthdays(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "show-address":
            print(show_address(args, contacts))
        elif command == "add-note":
            print(add_note(args, notes_manager, counter))
            counter += 1
        elif command == "add-tag":
            print(add_tag(args, notes_manager))
        elif command == "edit-note":
            edit_note(args, notes_manager)
        elif command == "delete-note":
            print(delete_note(args, notes_manager))
        elif command == "show-note":
            print(show_note(args, notes_manager))
        elif command == "show-all-notes":
            print(show_all_notes(notes_manager))
        elif command == "search-contact":
            print(search_contact(args, contacts))
        elif command == "search-note":
            print(search_note(args, notes_manager))
        elif command == "sort-notes":
            print(sort_notes_by_tag(args, notes_manager))
        else:
            print(MESSAGES["invalid_commad"])
        session.completer = get_completer(NONE_COMMANDS, contacts, notes_manager)


if __name__ == "__main__":
    main()
