"""Helpers for user session"""

from prompt_toolkit import PromptSession
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.history import FileHistory


bot_history = FileHistory(".bot-history-file")


def get_completer(none_commands, contacts=None, notes=None):
    """Return completer for words"""
    contacts_keys, notes_keys = None, None

    if hasattr(contacts, "items"):
        contacts_keys = {c: None for c, _ in contacts.items()}
    if hasattr(notes, "data"):
        notes_keys = {str(n.note_id): None for n in notes.data}

    nested_dict = dict(none_commands)
    nested_dict["add"] = {
        "email": contacts_keys,
        "phone": contacts_keys,
        "birthday": contacts_keys,
        "address": contacts_keys,
        "contact": None,
        "note": None,
        "tag": None
    }
    nested_dict["create"] = nested_dict["add"]
    nested_dict["new"] = nested_dict["add"]

    nested_dict["delete"] = {
        "email": contacts_keys,
        "phone": contacts_keys,
        "birthday": contacts_keys,
        "address": contacts_keys,
        "contact": contacts_keys,
        "note": None,
    }
    nested_dict["remove"] =  nested_dict["delete"]
    nested_dict["drop"] = nested_dict["delete"]

    nested_dict["edit"] = {
        "email": contacts_keys,
        "phone": contacts_keys,
        "birthday": contacts_keys,
        "address": contacts_keys,
        "note": {
            "title" : notes_keys,
            "description": notes_keys,
            "tags": notes_keys,
        },
    }
    nested_dict["update"] = nested_dict["edit"]
    nested_dict["change"] = nested_dict["edit"]

    nested_dict["phone"] = contacts_keys
    nested_dict["show-address"] = contacts_keys
    nested_dict["show-note"] = notes_keys
    completer = NestedCompleter.from_nested_dict(nested_dict)
    return completer


def open_session(default_commands, contacts, notes, style):
    return PromptSession(
        completer=get_completer(
            default_commands,
            contacts,
            notes,
        ),
        style=style,
        history=bot_history,
        auto_suggest=AutoSuggestFromHistory(),
    )
