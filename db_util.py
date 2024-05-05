'''
Utility class responsible for persisting and querying data from the SQLite3 database
'''
import sqlite3
import json

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

    def query(self):
        self.cursor.execute("SELECT * FROM requests")
        rows = self.cursor.fetchall()
        data = []
        columns = [desc[0] for desc in self.cursor.description]

        for row in rows:
            row_dict = dict(zip(columns, row))
            data.append(row_dict)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return data

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