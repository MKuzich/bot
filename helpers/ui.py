"""Main User interface configurations"""
from datetime import datetime
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML


style = Style.from_dict(
    {
        "completion-menu.completion": "bg:#008888 #ffffff",
        "completion-menu.completion.current": "bg:#00aaaa #000000",
        "scrollbar.background": "bg:#88aaaa",
        "scrollbar.button": "bg:#222222",
        "bottom-toolbar": "#103356 bg:#ff0000",
        "bottom-toolbar.text": "#aaaa44 bg:#aa4444",
    }
)

def get_bottom_toolbar(contacts, notes_manager):
    now = datetime.now()
    contacts_len = len(contacts) if hasattr(contacts, "items") else 0
    notes_len = len(notes_manager.data)
    return HTML(f'<b>Contacts</b> {contacts_len} <b>Notes</b> {notes_len} ' + \
                f'<b>Time</b> {now.strftime("%H:%M:%S")}')
