import sqlite3 as sql

class database:
    def __init__(self, db_name= "db.db"):
        self.connection = sql.connect(db_name)
        self.cursor = self.connection.cursor()

    def get_notes(self):
        notes = self.cursor.execute('''SELECT * FROM notes''')
        return notes.fetchall()
    
    def update_note(self, id, text):
        self.cursor.execute('''UPDATE notes SET text=? WHERE id=?''', (text, id))
        self.connection.commit()

    def get_note(self, id):
        note = self.cursor.execute('''SELECT text FROM notes WHERE id=?''', (id, ))
        try:
            return note.fetchone()[0].strip()
        except:
            return ""
    
    def delete_note(self, id):
        self.cursor.execute('''DELETE FROM notes WHERE id=?''', (id, ))
        self.connection.commit()

    def create_note(self, title):
        self.cursor.execute('''INSERT INTO notes (title) VALUES (?)''', (title, ))
        self.connection.commit()