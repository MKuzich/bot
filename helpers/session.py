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
    nested_dict["show-note"] = notes_keys
    completer = NestedCompleter.from_nested_dict(
        nested_dict
    )
    return completer
