import functools
from src.db.DataBase import DataBase
def entity(func):
    @functools.wraps(func)
    def wrapper(instance, *args, **kwargs):
        db = DataBase()
        result = func(instance, *args, **kwargs)
        db.db_disconnect()
        return result

    return wrapper