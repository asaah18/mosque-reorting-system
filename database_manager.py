import sqlite3


class Mosque:
    def __init__(self, database_path: str = "mosquedb.db"):
        self.connection = sqlite3.Connection(database_path)
        command = """CREATE TABLE IF NOT EXISTS "mosques" (
                "name"	TEXT,
                "address"	TEXT,
                "altitude"	FLOAT,
                "longitude"	FLOAT,
                "notes"	TEXT
            );"""
        self.connection.execute(command)

    def add_mosque(self, name: str, address: str, altitude: float, longitude: float):
        record = {"name": name, "address": address, "altitude": altitude, "longitude": longitude, "notes": None}
        command = "INSERT INTO mosques VALUES (?, ?, ?, ?, ?)"
        self.connection.execute(command, tuple(record.values()))
        self.connection.commit()

    def search(self, name: str):
        command = "SELECT * FROM mosques WHERE name=?"
        cursor = self.connection.execute(command, (name,))
        records = cursor.fetchall()
        return records

    def add_note(self, name: str, notes: str):
        data = {"notes": notes, "name": name}
        command = "UPDATE mosques SET notes=? WHERE name=?"
        self.connection.execute(command, tuple(data.values()))
        self.connection.commit()

    def delete_mosque(self, name: str):
        command = "DELETE FROM mosques WHERE name=?"
        self.connection.execute(command, (name,))
        self.connection.commit()
