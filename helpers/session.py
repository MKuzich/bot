"""Helpers for user session"""
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.history import FileHistory
bot_history = FileHistory(".bot-history-file")


def get_completer(none_commands, contacts=None, notes=None):
    """Return completer for words"""
    contacts_keys, notes_keys = None, None

    if hasattr(contacts, "items"):
        contacts_keys = {c:None for c, _ in contacts.items()}
    if hasattr(notes, "items"):
        notes_keys = {n:None for n, _ in notes.items()}
    nested_dict = dict(none_commands)
    nested_dict["phone"] = contacts_keys
    nested_dict["show-address"] = contacts_keys
    nested_dict["add-email"] = contacts_keys
    nested_dict["add-address"] = contacts_keys
    nested_dict["show-address"] = contacts_keys
    nested_dict["add-birthday"] = contacts_keys
    nested_dict["remove"] = contacts_keys
    nested_dict["delete"] = contacts_keys
    nested_dict["drop"] = contacts_keys
    nested_dict["show-note"] = notes_keys
    nested_dict["edit"] = {
        "email" : contacts_keys,
        "phone" : contacts_keys,
        "birthday": contacts_keys,
        "address" : contacts_keys
    }
    completer = NestedCompleter.from_nested_dict(
        nested_dict
    )
    return completer
