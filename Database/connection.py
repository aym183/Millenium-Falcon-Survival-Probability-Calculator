import sqlite3
conn = sqlite3.connect("universe.db")

c = conn.cursor()

# c.execute("""DROP TABLE IF EXISTS ROUTES""")

c.execute("""CREATE TABLE IF NOT EXISTS ROUTES (
    ORIGIN VARCHAR(150) NOT NULL,
    DESTINATION VARCHAR(150) NOT NULL,
    TRAVEL_TIME MEDIUMINT UNSIGNED
)""")


# c.execute("""INSERT into ROUTES VALUES
#     ('Tatooine', 'Dagobah', 6),
#     ('Dagobah', 'Endor', 4),
#     ('Dagobah', 'Hoth', 1),
#     ('Hoth', 'Endor', 1),
#     ('Tatooine', 'Hoth', 6)
# """)

# c.execute("""SELECT * FROM ROUTES""")
# for i in c.fetchall():
#     print(i)
    

conn.commit()


       