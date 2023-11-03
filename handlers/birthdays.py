def birthdays(days, book):
    try:
        upcoming_birthdays = book.get_birthdays_in_next_days(days)
        return upcoming_birthdays if upcoming_birthdays else "No upcoming birthdays."
    except ValueError as e:
        return str(e)
