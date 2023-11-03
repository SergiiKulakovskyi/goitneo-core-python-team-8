# Address Book and Notes Bot (by CodeCrafters)

This is an address book and notes bot written in Python. It allows you to add, edit, delete, and search for contacts and notes. You can also use it to view a list of upcoming birthdays.

#### Before running the bot, you need to install the following Python packages:

```
pip install levenshtein
pip install tabulate
```

#### To start the bot, run the following command:

```
python bot.py
```

#### Saving and loading data:

The bot saves and loads data to and from local files. This means that you can keep your data even after you close the bot. When you start the bot, it will automatically load the data.

#### Auto-Suggestion Feature

The bot has an auto-suggestion feature that can help you when you mistype a command. If you enter an incorrect or misspelled command, the bot will suggest the closest valid command using the Levenshtein distance method. This can be handy if you are not sure about the exact command syntax.

## Available commands:

#### Address book commands

`add`: Add a new contact to the address book.

`change`: Change an existing contact in the address book.

`delete`: Delete an existing contact from the address book.

`all`: Show all existing contacts in the address book.

`search-contacts`: Search for contacts in the address book by specific criteria.

`birthdays`: Show all contacts with birthdays in a specified number of days (1 - 365).

#### Notes commands

`add-note`: Creates a new note.

`edit-note`: Edits an existing note.

`delete-note`: Deletes an existing note.

`all-notes`: Lists all of the notes.

`find-notes`: Searches for notes based on specific criteria, such as the note content or tags.

`add-note-tag`: Adds a tag to an existing note.

`remove-note-tag`: Removes a tag from an existing note.

`search-notes-by-tags`: Search notes by tags.

#### Common commands

`close`, `exit`: Close the bot.

`hello`: Show a greeting message.

## Examples:

To add a new contact to the address book:

`add -n "John Doe" -p 1234567890 -a "123 Main Street" -e john.doe@example.com -b 01.01.1980`

`add -n "Mr Smith"`

To change an existing contact in the address book:

`change -n "John Doe" -p 9876543210`

`change -n "Mr Smith" -p 1234567890 -e mr.smith@example.com`


To delete an existing contact from the address book or specific fields:

`delete -n "John Doe"`

`delete -n "Mr Smith" -f phone email`

To search for contacts in the address book by name:

`search-contacts -c email example`

To show all existing contacts in the address book:

`all`

To close the bot:

`close`

`exit`

To show a greeting message:

`hello`

To show all contacts with birthdays in the next 7 days:

`birthdays 7`

To create a new note:

`add-note "This is my first note."`

To search for notes based on the content:

`find-notes "first note"`

To list all of the notes:

`all-notes`

To edit an existing note:

`edit-note 1 "This is my updated note."`

To delete an existing note:

`delete-note 1`

To add a tag to an existing note:

`add-note-tag 1 important`

To remove a tag from an existing note:

`remove-note-tag 1 important`

To search notes by tags:

`search-notes-by-tags important`

