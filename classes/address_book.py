from collections import UserDict, defaultdict
from datetime import datetime


weekday_names = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_in_next_days(self, days):
        if days < 1 or days > 365:
            raise ValueError("Days must be within 1 to 365.")

        birthday_dict = defaultdict(list)
        today = datetime.today().date()

        for record in self.data.values():
            name = record.name.value
            if record.birthday is None:
                continue
            birthday_date = record.birthday.value
            birthday_this_year = birthday_date.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_date.replace(year=today.year + 1)

            days_until_birthday = (birthday_this_year - today).days
            if 0 <= days_until_birthday <= days:
                birthday_dict[birthday_this_year].append(name)

        result = ''
        for birthday, names in sorted(birthday_dict.items()):
            day_string = birthday.strftime("%Y-%m-%d %A")
            result += f"{day_string}: {', '.join(names)}\n"

        return result.strip() if result else "No upcoming birthdays."
