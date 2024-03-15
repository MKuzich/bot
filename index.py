"""Index bot file"""

from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit import print_formatted_text
from data_handlers import save_data, load_data
from models import AddressBook, NotesManager
from input_handlers import (
    add_contact,
    change_contact,
    remove_contact,
    show_contact,
    all_contacts,
    birthdays,
    add_birthday,
    show_birthday,
    add_email,
    add_address,
    show_address,
    add_note,
    add_tag,
    edit_note,
    delete_note,
    show_note,
    search_note,
    sort_notes_by_tag,
)
from helpers.ui import style, get_bottom_toolbar
from helpers.session import get_completer, bot_history
from constants import NONE_COMMANDS, HELP_TEXT, HI_TEXT, PROMT


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


print = print_formatted_text


def main():
    """Main bot functions"""

    def get_toolbar():
        return get_bottom_toolbar(contacts, notes_manager)

    contacts = AddressBook()
    notes_manager = NotesManager()
    session = PromptSession(
        completer=get_completer(
            NONE_COMMANDS,
            contacts,
            notes_manager,
        ),
        style=style,
        history=bot_history,
        auto_suggest=AutoSuggestFromHistory(),
    )
    try:
        contacts = load_data()
    except FileNotFoundError:  # move to handlers errors
        pass
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
            save_data(contacts)
            break

        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "quit"]:
            print("Good bye!")
            save_data(contacts)
            break
        elif command in ["hello", "hi", "hey", "yo", "sup"]:
            print(HI_TEXT)
        elif command in ["help"]:
            print(HELP_TEXT)
        elif command in ["add", "create", "new"]:
            print(add_contact(args, contacts))
        elif command in ["change", "edit", "update"]:
            print(change_contact(args, contacts))
        elif command in ["delete", "remove", "drop"]:
            print(remove_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        elif command == "birthdays":
            print(birthdays(args, contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "add-email":
            print(add_email(args, contacts))
        elif command == "add-address":
            print(add_address(args, contacts))
        elif command == "show-address":
            print(show_address(args, contacts))
        elif command == "add-note":
            print(add_note(notes_manager))
        elif command == "add-tag":
            print(add_tag(args, notes_manager))
        elif command == "edit-note":
            edit_note(args, notes_manager)
        elif command == "delete-note":
            print(delete_note(args, notes_manager))
        elif command == "show-note":
            print(show_note(args, notes_manager))
        elif command == "show-all-notes":
            notes_manager.display_notes()
        elif command == "search-contact":
            print(search_contact(args, contacts))
            notes_manager.display_notes()
        elif command == "search-note":
            print(search_note(args, notes_manager))
        elif command == "sort-notes":
            print(sort_notes_by_tag(args, notes_manager))
        else:
            print("Invalid command.")
        session.completer = get_completer(NONE_COMMANDS, contacts, notes_manager)


if __name__ == "__main__":
    main()
