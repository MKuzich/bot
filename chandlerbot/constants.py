"""File with default configurations"""

from prompt_toolkit.formatted_text import HTML

EMAIL_PATTERN = r"^\S+@\S+\.\S+$"
BULDING_PATTERN = r"^\d+(?:[\\/]?\d+[A-Za-z]*)?$"
GB_POSTAL_CODE = (
    r"(GIR[ ]?0AA|((AB|AL|B|BA|BB|BD|BH|BL|BN|BR|BS|BT|CA|CB|CF|CH|CM|CO|CR|CT|CV|"
)
GB_POSTAL_CODE += (
    r"CW|DA|DD|DE|DG|DH|DL|DN|DT|DY|E|EC|EH|EN|EX|FK|FY|G|GL|GY|GU|HA|HD|HG|HP|HR|"
)
GB_POSTAL_CODE += (
    r"HS|HU|HX|IG|IM|IP|IV|JE|KA|KT|KW|KY|L|LA|LD|LE|LL|LN|LS|LU|M|ME|MK|ML|N|NE|"
)
GB_POSTAL_CODE += (
    r"NG|NN|NP|NR|NW|OL|OX|PA|PE|PH|PL|PO|PR|RG|RH|RM|S|SA|SE|SG|SK|SL|SM|SN|SO|"
)
GB_POSTAL_CODE += (
    r"SP|SR|SS|ST|SW|SY|TA|TD|TF|TN|TQ|TR|TS|TW|UB|W|WA|WC|WD|WF|WN|WR|WS|WV|YO|"
)
GB_POSTAL_CODE += r"ZE)(\d[\dA-Z]?[ ]?\d[ABD-HJLN-UW-Z]{2}))|BFPO[ ]?\d{1,4})"

POSTAL_CODES_BY_COUNTRY = {
    "GB": GB_POSTAL_CODE,
    "JE": r"JE\d[\dA-Z]?[ ]?\d[ABD-HJLN-UW-Z]{2}",
    "GG": r"GY\d[\dA-Z]?[ ]?\d[ABD-HJLN-UW-Z]{2}",
    "IM": r"IM\d[\dA-Z]?[ ]?\d[ABD-HJLN-UW-Z]{2}",
    "US": r"\d{5}([ \-]\d{4})?",
    "CA": r"[ABCEGHJKLMNPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ ]?\d[ABCEGHJ-NPRSTV-Z]\d",
    "DE": r"\d{5}",
    "JP": r"\d{3}-\d{4}",
    "FR": r"\d{2}[ ]?\d{3}",
    "AU": r"\d{4}",
    "IT": r"\d{5}",
    "CH": r"\d{4}",
    "AT": r"\d{4}",
    "ES": r"\d{5}",
    "NL": r"\d{4}[ ]?[A-Z]{2}",
    "BE": r"\d{4}",
    "DK": r"\d{4}",
    "SE": r"\d{3}[ ]?\d{2}",
    "NO": r"\d{4}",
    "BR": r"\d{5}[\-]?\d{3}",
    "PT": r"\d{4}([\-]\d{3})?",
    "FI": r"\d{5}",
    "AX": r"22\d{3}",
    "KR": r"\d{3}[\-]\d{3}",
    "CN": r"\d{6}",
    "TW": r"\d{3}(\d{2})?",
    "SG": r"\d{6}",
    "DZ": r"\d{5}",
    "AD": r"AD\d{3}",
    "AR": r"([A-HJ-NP-Z])?\d{4}([A-Z]{3})?",
    "AM": r"(37)?\d{4}",
    "AZ": r"\d{4}",
    "BH": r"((1[0-2]|[2-9])\d{2})?",
    "BD": r"\d{4}",
    "BB": r"(BB\d{5})?",
    "BY": r"\d{6}",
    "BM": r"[A-Z]{2}[ ]?[A-Z0-9]{2}",
    "BA": r"\d{5}",
    "IO": r"BBND 1ZZ",
    "BN": r"[A-Z]{2}[ ]?\d{4}",
    "BG": r"\d{4}",
    "KH": r"\d{5}",
    "CV": r"\d{4}",
    "CL": r"\d{7}",
    "CR": r"\d{4,5}|\d{3}-\d{4}",
    "HR": r"\d{5}",
    "CY": r"\d{4}",
    "CZ": r"\d{3}[ ]?\d{2}",
    "DO": r"\d{5}",
    "EC": r"([A-Z]\d{4}[A-Z]|(?:[A-Z]{2})?\d{6})?",
    "EG": r"\d{5}",
    "EE": r"\d{5}",
    "FO": r"\d{3}",
    "GE": r"\d{4}",
    "GR": r"\d{3}[ ]?\d{2}",
    "GL": r"39\d{2}",
    "GT": r"\d{5}",
    "HT": r"\d{4}",
    "HN": r"(?:\d{5})?",
    "HU": r"\d{4}",
    "IS": r"\d{3}",
    "IN": r"\d{6}",
    "ID": r"\d{5}",
    "IL": r"\d{5}",
    "JO": r"\d{5}",
    "KZ": r"\d{6}",
    "KE": r"\d{5}",
    "KW": r"\d{5}",
    "LA": r"\d{5}",
    "LV": r"\d{4}",
    "LB": r"(\d{4}([ ]?\d{4})?)?",
    "LI": r"(948[5-9])|(949[0-7])",
    "LT": r"\d{5}",
    "LU": r"\d{4}",
    "MK": r"\d{4}",
    "MY": r"\d{5}",
    "MV": r"\d{5}",
    "MT": r"[A-Z]{3}[ ]?\d{2,4}",
    "MU": r"(\d{3}[A-Z]{2}\d{3})?",
    "MX": r"\d{5}",
    "MD": r"\d{4}",
    "MC": r"980\d{2}",
    "MA": r"\d{5}",
    "NP": r"\d{5}",
    "NZ": r"\d{4}",
    "NI": r"((\d{4}-)?\d{3}-\d{3}(-\d{1})?)?",
    "NG": r"(\d{6})?",
    "OM": r"(PC )?\d{3}",
    "PK": r"\d{5}",
    "PY": r"\d{4}",
    "PH": r"\d{4}",
    "PL": r"\d{2}-\d{3}",
    "PR": r"00[679]\d{2}([ \-]\d{4})?",
    "RO": r"\d{6}",
    "SM": r"4789\d",
    "SA": r"\d{5}",
    "SN": r"\d{5}",
    "SK": r"\d{3}[ ]?\d{2}",
    "SI": r"\d{4}",
    "ZA": r"\d{4}",
    "LK": r"\d{5}",
    "TJ": r"\d{6}",
    "TH": r"\d{5}",
    "TN": r"\d{4}",
    "TR": r"\d{5}",
    "TM": r"\d{6}",
    "UA": r"\d{5}",
    "UY": r"\d{5}",
    "UZ": r"\d{6}",
    "VA": r"00120",
    "VE": r"\d{4}",
    "ZM": r"\d{5}",
    "AS": r"96799",
    "CC": r"6799",
    "CK": r"\d{4}",
    "RS": r"\d{6}",
    "ME": r"8\d{4}",
    "CS": r"\d{5}",
    "YU": r"\d{5}",
    "CX": r"6798",
    "ET": r"\d{4}",
    "FK": r"FIQQ 1ZZ",
    "NF": r"2899",
    "FM": r"(9694[1-4])([ \-]\d{4})?",
    "GF": r"9[78]3\d{2}",
    "GN": r"\d{3}",
    "GP": r"9[78][01]\d{2}",
    "GS": r"SIQQ 1ZZ",
    "GU": r"969[123]\d([ \-]\d{4})?",
    "GW": r"\d{4}",
    "HM": r"\d{4}",
    "IQ": r"\d{5}",
    "KG": r"\d{6}",
    "LR": r"\d{4}",
    "LS": r"\d{3}",
    "MG": r"\d{3}",
    "MH": r"969[67]\d([ \-]\d{4})?",
    "MN": r"\d{6}",
    "MP": r"9695[012]([ \-]\d{4})?",
    "MQ": r"9[78]2\d{2}",
    "NC": r"988\d{2}",
    "NE": r"\d{4}",
    "VI": r"008(([0-4]\d)|(5[01]))([ \-]\d{4})?",
    "PF": r"987\d{2}",
    "PG": r"\d{3}",
    "PM": r"9[78]5\d{2}",
    "PN": r"PCRN 1ZZ",
    "PW": r"96940",
    "RE": r"9[78]4\d{2}",
    "SH": r"(ASCN|STHL) 1ZZ",
    "SJ": r"\d{4}",
    "SO": r"\d{5}",
    "SZ": r"[HLMS]\d{3}",
    "TC": r"TKCA 1ZZ",
    "WF": r"986\d{2}",
    "XK": r"\d{5}",
    "YT": r"976\d{2}",
}

NONE_COMMANDS = {
    "hello": None,
    "hi": None,
    "hey": None,
    "yo": None,
    "sup": None,
    "close": None,
    "exit": None,
    "bye": None,
    "quit": None,
    "all": None,
    "show-all-notes": None,
    "search-contact": None,
    "search-note": None,
    "sort-notes": None,
    "birthdays": None,
    "show-birthday": None,
}

HELP_TEXT = HTML(
    "<strong>Hello, this is help! Available commands:</strong>\n"
    + "<ansigreen>add</ansigreen>/<ansigreen>create</ansigreen>/<ansigreen>new</ansigreen> <ansigreen>&#10094;attribute&#10095;</ansigreen> \n" 
    + "   Available attributes:\n" 
    + "   <ansigreen>email</ansigreen> - add email to existing contact\n"
    + "   <ansigreen>phone</ansigreen> - add phone to existing contact\n"
    + "   <ansigreen>birthday</ansigreen> - add birthday to existing contact\n"
    + "   <ansigreen>address</ansigreen> - add address to existing contact\n"
    + "   <ansigreen>contact</ansigreen> - add new contact\n"
    + "   <ansigreen>note</ansigreen> - add new note\n"
    + "   <ansigreen>tag</ansigreen> - add tag to existing note\n"
    + "<ansiyellow>change</ansiyellow>/<ansiyellow>edit</ansiyellow>/<ansiyellow>update</ansiyellow> <ansiyellow>&#10094;attribute&#10095;</ansiyellow> \n"
    + "   Available attributes:\n"
    + "   <ansiyellow>email</ansiyellow> - edit email of existing contact\n"
    + "   <ansiyellow>phone</ansiyellow> - edit phone of existing contact\n"
    + "   <ansiyellow>birthday</ansiyellow> - edit birthday of existing contact\n"
    + "   <ansiyellow>address</ansiyellow> - edit address of existing contact\n"
    + "   <ansiyellow>note &#10094;attribute&#10095;</ansiyellow> - edit note\n"
    + "      Available attributes:\n"
    + "      <ansiyellow>title</ansiyellow> - edit title\n"
    + "      <ansiyellow>description</ansiyellow> - edit description\n"
    + "      <ansiyellow>tags</ansiyellow> - edit tags\n"
    + "<ansired>delete</ansired>/<ansired>remove</ansired>/<ansired>drop</ansired> <ansired>&#10094;attribute&#10095;</ansired> \n"
    + "   Available attributes:\n"
    + "   <ansired>email</ansired> - delete email of existing contact\n"
    + "   <ansired>phone</ansired> - delete phone of existing contact\n"
    + "   <ansired>birthday</ansired> - delete birthday of existing contact\n"
    + "   <ansired>address</ansired> - delete address of existing contact\n"
    + "   <ansired>contact</ansired> - delete contact\n"
    + "   <ansired>note</ansired> - delete note\n"
    + "<ansiblue>all</ansiblue> - show all contacts\n"
    + "<ansiblue>show-all-notes</ansiblue> - show all notes\n"
    + "<ansiblue>hello</ansiblue>/<ansiblue>hi</ansiblue>/<ansiblue>hey</ansiblue>/<ansiblue>yo</ansiblue>/<ansiblue>sup</ansiblue> - say hello\n"
    + "<ansiblue>help</ansiblue> - show this message\n"
    + "<ansiblue>close</ansiblue>/<ansiblue>exit</ansiblue>/<ansiblue>bye</ansiblue>/<ansiblue>quit</ansiblue> - close the program\n"
    + "<ansiblue>search-contact &#10094;name&#10095;</ansiblue> - search contact by any of contact attributes\n"
    + "<ansiblue>search-note &#10094;word&#10095;</ansiblue> - search note by any of attributes\n"
    + "<ansiblue>sort-notes &#10094;tag&#10095;</ansiblue> - sort notes by tag\n"
    + "<ansiblue>phone &#10094;contact&#10095;</ansiblue> - show phone of existing contact\n"
    + "<ansiblue>birthdays &#10094;days&#10095;</ansiblue> - show birthdays in the specified period\n"
    + "<ansiblue>show-birthday &#10094;contact&#10095;</ansiblue> - show birthday of existing contact\n"
    + "<ansiblue>show-address &#10094;contact&#10095;</ansiblue> - show address of existing contact\n"
    + "<ansiblue>show-note &#10094;note id&#10095;</ansiblue> - show note by ID\n"
)

HI_TEXT = HTML(
    "<strong>How can I help you?</strong> I can do this: \n"
    + "<ansigreen>Add</ansigreen>/"
    + "<ansiyellow>edit</ansiyellow>/"
    + "<ansired>delete</ansired> "
    + "contacts and notes\n"
    + "Type <ansiblue>help</ansiblue> to show usage of commads."
)
PROMT_ = HTML('<style fg="#00aa00">>>> </style>')

MESSAGES = {
    "edit_no_args": HTML(
        '<strong><style fg="#F87168">Error: Given format not supported\n</style></strong>'
        '<strong><style fg="#00aa00">Usage: edit [what]* [contact\\note] </style></strong>'
    ),
    "not_found": HTML(
        '<style fg="#DC620C">I`m sorry, but I cannot find this..</style>'
    ),
    "canceled": HTML('<strong><style fg="#00aa00">Ok. Canceled!</style></strong>'),
    "phone_not_set": HTML(
        '<strong><style fg="#F87168">Error: No phones found\n</style></strong>'
        '<strong><style fg="#00aa00">Usage: add phone* [contact] [phone] </style></strong>'
    ),
    "email_not_set": HTML(
        '<strong><style fg="#F87168">Error: Email not found\n</style></strong>'
        '<strong><style fg="#00aa00">Usage: add  email* [contact] [email] </style></strong>'
    ),
    "address_not_set": HTML(
        '<strong><style fg="#F87168">Error: No address found\n</style></strong>'
        '<strong><style fg="#00aa00">Usage: add address* [contact]'
        '[street* buliding* city* postal code country] </style></strong>'
    ),
    "birthday_not_set": HTML(
        '<strong><style fg="#F87168">Error: Birthday not found\n</style></strong>'
        '<strong><style fg="#00aa00">Usage: add birthday* [contact] [birthday] </style></strong>'
    ),
    "not_correct_format": HTML(
        '<strong><style fg="#F87168">Error: No correct input\n</style></strong>'
        'Type <style fg="#00aa00"><strong>help</strong></style> to show usage of commads.'
    ),
    "invalid_commad": HTML(
        '<strong><style fg="#F87168">Error: invalid command input\n</style></strong>'
        'Type <style fg="#00aa00"><strong>help</strong></style> to show usage of commads.'
    ),
    "dev": HTML(
        '<strong><style fg="#F87168">Error: in development\n</style></strong>'
        'Type <style fg="#00aa00"><strong>help</strong></style> to show usage of commads.'
    ),
    "notes_not_found": HTML(
        '<strong><style fg="#F87168">Error: Any note not found\n</style></strong>'
        '<strong><style fg="#00aa00">Usage: add  note* [title]'
        '[description] [tags]</style></strong>'
    ),
}
STYLES = {
    "completion-menu.completion": "bg:#008888 #ffffff",
    "completion-menu.completion.current": "bg:#00aaaa #000000",
    "scrollbar.background": "bg:#88aaaa",
    "scrollbar.button": "bg:#222222",
    "bottom-toolbar": "#103356 bg:#ff0000",
    "bottom-toolbar.text": "#aaaa44 bg:#000000",
    "padding": "#008888 bg:#ff0000",
    "dialog": "bg:#103356",
    "dialog frame.label": "bg:#88aaaa #000000",
    "dialog.body": "#000000 bg:#aaaa44",
    "dialog shadow": "bg:#88aaaa",
}
PROMT = HTML(
    '<style fg="#aaaa44">45`ers</style>'
    '<style fg="#072F68">@</style>'
    '<style fg="#aaaa44">Chandler </style>'
    '<style fg="#00aa00">> </style>'
)
