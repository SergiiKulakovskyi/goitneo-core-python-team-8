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

    def get_birthdays_per_week(self):
        birthday_dict = defaultdict(list)
        today = datetime.today().date()
        current_weekday = today.weekday()

        for record in self.data.values():
            name = record.name.value
            if record.birthday.value is None:
                continue
            birthday = record.birthday.value.date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            delta_days = (birthday_this_year - today).days
            birthday_weekday = birthday_this_year.weekday()
            if birthday_weekday in [5, 6]:
                delta_days += 7 - birthday_weekday

            if delta_days < 7:
                greeting_weekday = (current_weekday + delta_days) % 7
                birthday_dict[weekday_names[greeting_weekday]].append(name)

        result = ''
        for day, names in birthday_dict.items():
            result += f"{day}: {', '.join(names)}\n"
        return result
