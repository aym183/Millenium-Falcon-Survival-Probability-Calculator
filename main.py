import json
from Database.route_check import Routes
from Database.countdown_check import Countdown

f = open('Back-end/practice-millennium-falcon.json')
data = json.load(f)

g = open('Back-end/practice-empire.json')
countdown_data = json.load(g)

new_route = Routes(data['departure'], data['arrival'], data['autonomy'])
new_route.check_routes()

countdown_check = Countdown(new_route.cost_list, countdown_data["countdown"])
countdown_check.countdown_val()

print(new_route.cost_list)
