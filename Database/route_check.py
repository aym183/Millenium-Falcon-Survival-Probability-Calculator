import sqlite3
conn = sqlite3.connect("Database/universe.db")
class Routes():

    def __init__(self, departure, destination):
        self.departure = departure
        self.destination = destination
        self.current_location = departure
        self.next_location = None
        self.path=[]
        self.cost = 0
        self.cost_list = []
        

    visited = set() # Set to keep track of visited nodes of graph.

    def dfs(self, visited, node):  #function for dfs 

        c = conn.cursor()
        c.execute(f"SELECT * FROM ROUTES WHERE ORIGIN == '{self.current_location}'")
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


    def check_routes(self):
    
        c = conn.cursor()
        c.execute(f"SELECT * FROM ROUTES WHERE ORIGIN == '{self.current_location}'")
       
        for i in c.fetchall():
            if i[1] == self.destination:
                print(i[1])
                print('FINISH')
                self.cost += i[2]
                self.cost_list.append(self.cost)
                print(self.cost)
                self.cost = 0

                
            else:
                self.path.append(i[1])
                print(i[1])
                self.current_location = i[1]
                self.cost += i[2]
                self.check_routes()
                
    
        conn.commit()
    