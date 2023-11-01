def note_error(message=None):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValueError:
                return message
            except Exception as e:
                return e

        return inner

    return decorator
