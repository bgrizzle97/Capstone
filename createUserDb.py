import sqlite3
conn = sqlite3.connect('user.db')
conn.execute("CREATE TABLE user (id INTEGER PRIMARY KEY, username char(100) NOT NULL, email char(100) NOT NULL, password char(100) NOT NULL, verified INTEGER)")
conn.commit()
conn.close()