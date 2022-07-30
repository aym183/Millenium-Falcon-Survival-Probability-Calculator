import sqlite3
conn = sqlite3.connect("Database/universe.db")
class Routes():

    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination
        self.current_location = departure

    def check_routes(self):
        c = conn.cursor()
        c.execute(f"SELECT * FROM ROUTES WHERE ORIGIN == '{self.departure}'")
       
        for i in c.fetchall():
            print("I am here")
            print(i)
        conn.commit()