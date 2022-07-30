import sqlite3
conn = sqlite3.connect("Database/universe.db")
class Routes():

    def __init__(self, departure, destination, autonomy):
        self.departure = departure
        self.destination = destination
        self.autonomy = autonomy
        self.current_location = departure
        self.next_location = None
        self.path=[]
        self.cost = 0
        self.cost_list = []


    def check_routes(self):
    
        c = conn.cursor()
        c.execute(f"SELECT * FROM ROUTES WHERE ORIGIN == '{self.current_location}'")
       
        for i in c.fetchall():
            
            if i[1] == self.destination:
                # if (self.autonomy - i[2]) <= 0:
                #     self.cost += 1
                #     self.autonomy = 6
                print(i[1])
                print('FINISH')
                self.cost += i[2]
                self.cost_list.append(self.cost)
                self.path.append(i[1])
                
                self.cost = 0
                
            else:
                
                # if (self.autonomy - i[2]) <= 0:
                #     self.cost += 1
                #     self.autonomy = 6
                
                self.path.append(i[1])
                print(i[1])
                self.current_location = i[1]
                self.cost += i[2]
                self.check_routes()
                    
    
        conn.commit()
    
