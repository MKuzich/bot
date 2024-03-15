## How to Use

    1. Clone the repository to your local machine.
    2. Navigate to the directory containing the CLI bot.
    3. Installl venv `python3 -m venv venv`.
    4. Activate venv `source venv/bin/activate` (`source ./venv/scripts/activate` for Windows).
    5. Install requirements `pip install -r requirements.txt`
    6. Run the CLI bot script `py main.py`.
    7. Enter commands as per the provided documentation.

## Commands and Functionalities

- **Close:** Exits the CLI bot, saving any changes made.

  ```
  close | exit | bye | quit
  ```

- **Greeting:** Responds with a greeting message.

  ```
  hello | hi | hey | yo | sup
  ```

- **Help:** Displays the help text with available commands.

  ```
  help
  ```

- **Add Contact:** Adds a new contact.

  ```
  add | create | new <contact_name> <contact_phone>
  ```

- **Change Contact:** Updates an existing contact.

  ```
  change | edit | update <contact_name> <new_contact_phone>
  ```

- **Delete Contact:** Removes a contact.

  ```
  delete | remove | drop <contact_name>
  ```

- **Show Phone:** Displays the phone number of a contact.

  ```
  phone <contact_name>
  ```

- **Show All Contacts:** Displays all contacts.

  ```
  all
  ```

- **Birthdays:** Displays upcoming birthdays.

  ```
  birthdays <days amount>
  ```

- **Add Birthday:** Adds a birthday for a contact.

  ```
  add-birthday <contact_name> <birthday_date>
  ```

- **Show Birthday:** Displays the birthday of a contact.

  ```
  show-birthday <contact_name>
  ```

- **Add Email:** Adds an email address to a contact.

  ```
  add-email <contact_name> <email_address>
  ```

- **Add Address:** Adds an address to a contact.

  ```
  add-address <contact_name> <street> <building> <city> <additional>
  ```

- **Show Address:** Displays the address of a contact.

  ```
  show-address <contact_name>
  ```

- **Add Note:** Adds a note with optional tags.

  ```
  add-note  <title> <note_content>
  ```

- **Add Tag:** Adds a tag to an existing note.

  ```
  add-tag <note_id> [<tag>]
  ```

- **Edit Note:** Edits an existing note.

  ```
  edit-note <note_id> <new_content>
  ```

- **Delete Note:** Deletes a note.

  ```
  delete-note <note_id>
  ```

- **Show Note:** Displays a note.

  ```
  show-note <note_id>
  ```

- **Show All Notes:** Displays all notes.

  ```
  show-all-notes
  ```

- **Search Contact:** Searches for a contact by name.

  ```
  search-contact <contact piece of data>
  ```

- **Search Note:** Searches for a note by content.

  ```
  search-note <key phrase>
  ```

- **Sort Notes:** Sorts notes by tag.
  ```
  sort-notes [<tag>]
  ```
