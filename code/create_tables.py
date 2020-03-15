import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# 用全名才能啟用 auto increment
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

# real代表浮點數
create_table = (
    "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
)
cursor.execute(create_table)


connection.commit()

connection.close()
