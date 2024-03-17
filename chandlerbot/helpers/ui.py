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
from chandlerbot.constants import STYLES

style = Style.from_dict(STYLES)

def get_bottom_toolbar(contacts, notes_manager, weather_info=None):
    now = datetime.now()
    contacts_len = len(contacts) if hasattr(contacts, "items") else 0
    notes_len = len(notes_manager.data)
    count_birthdays = contacts.get_count_birthdays_per_week()

    left_part = HTML(
        f" <b>Contacts</b> {contacts_len} <b>Notes</b> {notes_len} "
        f"<b>Birthdays</b> {count_birthdays} "
    )
    if weather_info:
        temperature = weather_info["main"]["temp"]
        right_part = HTML(
            f' <b>Temperature: {temperature} </b>'
            f' <b>City: {weather_info["name"]}</b>'
            f' <b> {now.strftime("%A")} </b>'
            f'{now.strftime("%d %B")} <b>Time</b> {now.strftime("%H:%M:%S")} '
        )
    else:
        right_part = HTML(
            f' <b> {now.strftime("%A")} </b>'
            f'{now.strftime("%d %B")} <b>Time</b> {now.strftime("%H:%M:%S")} '
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

def get_bold_green_html(text):
    return HTML(f"<strong><ansigreen>{text}</ansigreen></strong>")

def get_red_html(text):
    return HTML(f'<strong><style fg="#F87168">{text}</style></strong>')

def get_radio_dialog(title, values, text):
    radios = radiolist_dialog(values=values, title=title, text=text , style=style,)
    return radios

def get_input_dialog(title, text, default,):
    dialog = input_dialog(title=title, text=text, style=style, default=default,)
    return dialog

def get_confirm_dialog(title, text):
    dialog = yes_no_dialog(title=title, text=text, style=style)
    return dialog
