import sqlite3
conn = sqlite3.connect("Database/universe.db")
class Routes():

    def __init__(self, departure, destination, autonomy):
        self.departure = departure
        self.destination = destination
        self.prev_location = departure
        self.static_autonomy = autonomy
        self.var_autonomy = autonomy
        self.current_location = departure
        self.prev = None
        self.path=[]
        self.cost = 0
        self.cost_list = []
        self.string = [departure]

    # Method that checks all the possible routes to get to the desired destination from the origin
    def check_routes(self):

                # Querry to get all the possibe nodes from every possible location
                c = conn.cursor()
                c.execute(f"SELECT * FROM ROUTES WHERE ORIGIN == '{self.current_location}'")
            
                # Loop that recurses through the entire function for each possible location and seeing which gets you to destination
                for i in c.fetchall():

                    # Stopping the looop and adding path to list once destination reached
                    if i[1] == self.destination:
                       
                        self.prev_location = self.current_location
                        self.current_location = i[1]

                        if self.prev_location in self.string:
                            pass
                        else:
                            self.string.append(self.prev_location)
                            self.string.append(self.current_location)

                        if self.current_location in self.string:
                            pass
                        else:
                            self.string.append(self.current_location)

                        self.var_autonomy -= i[2]
                        self.cost += i[2]
                        self.cost_list.append(self.cost)
                        self.path.append(self.string)
                        self.string = []
                        self.cost = 0
                        
                    # Continuing loop when more leaf nodes found
                    else:

                        if self.prev_location in self.string:
                            pass
                        else:
                            self.string.append(self.prev_location)
                        
                        self.var_autonomy -= i[2]
                        self.prev_location = self.current_location
                        self.current_location = i[1]
                        self.cost += i[2]
                        
                        c.execute(f"SELECT * FROM ROUTES WHERE ORIGIN == '{i[1]}'")
                        if(len(c.fetchall())) == 0:
                            self.cost = 0
                            self.var_autonomy = self.static_autonomy

                        self.check_routes()
                conn.commit()

       
    
