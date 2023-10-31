def birthdays(book):
    upcoming_birthdays = book.get_birthdays_per_week()
    if upcoming_birthdays:
        return upcoming_birthdays
    else:
        return "No upcoming birthdays in the next week."
