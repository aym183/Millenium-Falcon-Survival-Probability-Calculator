import sqlite3
conn = sqlite3.connect("Database/universe.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS ROUTES (
    ORIGIN VARCHAR(150) NOT NULL,
    DESTINATION VARCHAR(150) NOT NULL,
    TRAVEL_TIME MEDIUMINT UNSIGNED
)""")

conn.commit()


       