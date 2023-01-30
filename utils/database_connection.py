import sqlite3

class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        # host is the data base location passed in
        self.connection = sqlite3.connect(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        # if any errors happen do not commit and just close connection.
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()