def input_error(message=None):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                return e or message or "Unknown error occurred during data processing"

        return inner

    return decorator
