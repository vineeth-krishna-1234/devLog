from threading import Lock


class Database:
    _instance = None
    _connection = None
    _lock = Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._connection:
            self._connection = "connected"


if __name__ == "__main__":
    instance_1 = Database()
    instance_2 = Database()
    print(instance_1 == instance_2)
    print(instance_1._connection == instance_2._connection)
