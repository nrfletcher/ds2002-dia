'''
Utility class responsible for persisting data to the SQLite3 database.
'''
import sqlite3

class DbUtil:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.db_created = False

    def connect(self):
        self.conn = sqlite3.connect('requests.db')
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.commit()
        self.conn.close()

    def persist(self, obj):
        if not self.db_created:
            self.create_table()
        factor = obj['factor']
        pi = obj['pi']
        time = obj['time']
        self.cursor.execute("INSERT INTO requests (factor, pi, time) VALUES (?, ?, ?)", (factor, pi, time))

    def create_table(self):
        if self.db_created:
            return
        else:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS requests (
                    request_id INTEGER PRIMARY KEY,
                    factor INTEGER,
                    pi REAL,
                    time TEXT
                )
            """)
            self.db_created = True