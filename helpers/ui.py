"""Main User interface configurations"""

from datetime import datetime
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog, yes_no_dialog


from prompt_toolkit.formatted_text import (
    fragment_list_width,
    merge_formatted_text,
    to_formatted_text,
)
from prompt_toolkit.application import get_app

style = Style.from_dict(
    {
        "completion-menu.completion": "bg:#008888 #ffffff",
        "completion-menu.completion.current": "bg:#00aaaa #000000",
        "scrollbar.background": "bg:#88aaaa",
        "scrollbar.button": "bg:#222222",
        "bottom-toolbar": "#103356 bg:#ff0000",
        "bottom-toolbar.text": "#aaaa44 bg:#aa4444",
        "padding": "#103356 bg:#ff0000",
    }
)


def get_bottom_toolbar(contacts, notes_manager):
    now = datetime.now()
    contacts_len = len(contacts) if hasattr(contacts, "items") else 0
    notes_len = len(notes_manager.data)

    left_part = HTML(f"<b>Contacts</b> {contacts_len} <b>Notes</b> {notes_len} ")
    right_part = HTML(
        f' <b> {now.strftime("%A")} </b>'
        f'{now.strftime("%d %B")} <b>Time</b> {now.strftime("%H:%M:%S")}'
    )
    used_width = sum(
        [
            fragment_list_width(to_formatted_text(left_part)),
            fragment_list_width(to_formatted_text(right_part)),
        ]
    )
    total_width = get_app().output.get_size().columns
    padding_size = total_width - used_width

    padding = HTML("<padding>%s</padding>") % (" " * padding_size,)

    return merge_formatted_text([left_part, padding, right_part])


def get_green_html(text):
    return HTML(f"<ansigreen>{text}</ansigreen>")


def get_red_html(text):
    return HTML(f'<strong><style fg="#F87168">{text}</style></strong>')


def get_radio_dialog(title, values, text):
    radios = radiolist_dialog(values=values, title=title, text=text)
    return radios


def get_input_dialog(title, text, default):
    dialog = input_dialog(title=title, text=text, style=style, default=default)
    return dialog


def get_confirm_dialog(title, text):
    dialog = yes_no_dialog(title=title, text=text, style=style)
    return dialog
