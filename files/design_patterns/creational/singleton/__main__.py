from threading import Lock


class DatabaseConnectionSingleton:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        # Ensures thread-safe singleton creation
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(DatabaseConnectionSingleton, cls).__new__(
                        cls, *args, **kwargs
                    )
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self._connection = ""  # create connection
            self._cursor = self._connection.cursor()

    def get_connection(self):
        return self._connection

    def close_connection(self):
        if self._connection:
            self._connection.close()
            self._connection = None
            self._cursor = None


# Example usage
if __name__ == "__main__":
    db = DatabaseConnectionSingleton("example.db")

