from decorators.input_error import input_error
from utils.representation import display_contacts


@input_error()
def show_all(book):
    return display_contacts(book.data.values())
