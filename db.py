import sqlite3


connection = sqlite3.connect("mydatabase.db")

cursor = connection.cursor()
# session.execute(
#     """
# CREATE TABLE  users (
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# username TEXT,
# email TEXT NOT NULL UNIQUE
# );
# """
# )
# cursor.execute(
#     "INSERT INTO users (username, email) VALUES ('alice', 'alice@email.com')"
# )
# cursor.execute("DELETE FROM users WHERE id=2")
# connection.commit()
# cursor.close()
