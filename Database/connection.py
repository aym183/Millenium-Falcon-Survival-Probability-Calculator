import sqlite3
conn = sqlite3.connect("Database/universe.db")

c = conn.cursor()

# Creation of the database

c.execute("""CREATE TABLE IF NOT EXISTS ROUTES (
    ORIGIN VARCHAR(150) NOT NULL,
    DESTINATION VARCHAR(150) NOT NULL,
    TRAVEL_TIME MEDIUMINT UNSIGNED
)""")

# DUMMY DATA IN THE TABLE

# c.execute("""INSERT into ROUTES VALUES
#     ('Tatooine', 'Dagobah', 6),
#     ('Dagobah', 'Endor', 4),
#     ('Dagobah', 'Hoth', 1),
#     ('Hoth', 'Endor', 1),
#     ('Tatooine', 'Hoth', 6)
# """)

conn.commit()


       