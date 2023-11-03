from classes.record import Record
from tabulate import tabulate

def display_contacts(contacts:list[Record]) -> str:
    headers = ["Name", "Email", "Phone", "Birthday", "Address"]
    rows = [[getattr(record, field, '') for field in [
        'name', 'email', 'phone', 'birthday', 'address']] for record in contacts]
    return tabulate(rows, headers=headers, tablefmt="grid")
