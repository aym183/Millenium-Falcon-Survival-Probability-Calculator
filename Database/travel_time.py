import sqlite3
conn = sqlite3.connect("Database/universe.db")
class Travel():

    def __init__(self, path):
        self.path = path

    # Method that calculates travel time and accumulates it to each path
    def travel_time_check(self):

        total_sum = 0
        for i in self.path:
            for j in range(len(i)-1):
                
                # Query to get travel time for each node 
                c = conn.cursor()
                c.execute(f"SELECT TRAVEL_TIME FROM ROUTES WHERE ORIGIN = '{i[j]}' AND DESTINATION = '{i[j+1]}';")
                conn.commit()
                for k in c.fetchall():
                    total_sum+=k[0]
                
            i.insert(0, total_sum)
            total_sum = 0