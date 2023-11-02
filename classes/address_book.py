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
        if days < 1 or days > 180:
            raise ValueError("Days must be within 1 to 180.")

        birthday_dict = defaultdict(list)
        today = datetime.today().date()

        for record in self.data.values():
            name = record.name.value
            if record.birthday is None:
                continue
            birthday = record.birthday.value.date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= days:
                birthday_dict[birthday_this_year.strftime("%A")].append(name)

        result = ''
        for day, names in sorted(birthday_dict.items()):
            result += f"{day}: {', '.join(names)}\n"
        return result.strip()
