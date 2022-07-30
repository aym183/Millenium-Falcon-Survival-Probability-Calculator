import json
from Database.route_check import Routes

f = open('Back-end/practice-millennium-falcon.json')
data = json.load(f)
print(data['departure'])
new_route = Routes(data['departure'], data['arrival'])
new_route.check_routes()
