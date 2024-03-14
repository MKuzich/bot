from data_handlers import save_data, load_data
from models.AddressBook import AddressBook
from input_handlers.add_contact import add_contact
from input_handlers.change_contact import change_contact
from input_handlers.remove_contact import remove_contact
from input_handlers.show_contact import show_contact
from input_handlers.all_contacts import all_contacts
from input_handlers.birthdays import birthdays
from input_handlers.add_birthday import add_birthday
from input_handlers.show_birthday import show_birthday
from input_handlers.add_email import add_email
from input_handlers.add_address import add_address
from input_handlers.show_address import show_address
from input_handlers.add_note import add_note
from input_handlers.edit_note import edit_note
from input_handlers.delete_note import delete_note
from input_handlers.show_note import show_note
from models.notes_manager import NotesManager
from models.note import Note


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = AddressBook()
    notes_manager = NotesManager()
    try:
        contacts = load_data()
    except FileNotFoundError: # move to handlers errors
        pass
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "quit"]:
            print("Good bye!")
            save_data(contacts)
            break
        elif command in ["hello", "hi", "hey", "yo", "sup"]:
            print("How can I help you?")
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
        elif command == "edit-note":
            edit_note(args, notes_manager)
        elif command == "delete-note":
            print(delete_note(args, notes_manager))
        elif command == "show-note":
            print(show_note(args, notes_manager))
        elif command == "show-all-notes":
            notes_manager.display_notes()
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
