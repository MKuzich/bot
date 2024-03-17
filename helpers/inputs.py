"""Promts tools"""

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from input_error import input_error


def get_comleter(words):
    return WordCompleter([words], ignore_case=True)


@input_error
def get_prompt(promt_message, toolbar, style, placeholder, validator):
    completer = get_comleter(placeholder)
    return prompt(
        promt_message,
        bottom_toolbar=toolbar,
        style=style,
        refresh_interval=0.5,
        placeholder=placeholder,
        validator=validator,
        validate_while_typing=False,
        completer=completer,
    )


@input_error
def parse_input(user_input, delimeter=" ", strip=False, no_lower=False):
    cmd, *args = user_input.split(delimeter)
    cmd = cmd if no_lower else cmd.strip().lower()
    if strip:
        args = [a.strip().lstrip() for a in args]
    return cmd, *args
