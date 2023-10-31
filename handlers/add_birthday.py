from datetime import datetime


def add_birthday(args, book):
    if len(args) != 2:
        return "Invalid number of arguments. Provide name and birthday."

    name, birthday = args
    try:
        datetime.strptime(birthday, "%d.%m.%Y")
    except ValueError:
        return "Incorrect date format. Should be 'DD.MM.YYYY'."

    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return f"Birthday added for {name}."
    else:
        return f"Contact {name} not found."
