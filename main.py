# importing sqlite
import sqlite3


# making a connection to the db
conn = sqlite3.connect('google.db')  # you can put any name || if you want to use memory use (":memory:")


# making a cursor
c = conn.cursor()


# First you need to create a table

# c.execute("""CREATE TABLE person(
#     first_name TEXT,
#     last_name TEXT,
#     email TEXT
# )""")

# if you are not using memory :
# You need to create a table a once not many times

# inserting into table
c.execute("""INSERT INTO person VALUES ('shajidur', 'rahman', 'shajidur rahman')""")

conn.commit()
conn.close()