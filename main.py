import json
from Database.route_check import Routes
from Backend.countdown_check import Countdown

f = open('Backend/practice-millennium-falcon.json')
data = json.load(f)

g = open('Backend/practice-empire.json')
countdown_data = json.load(g)

new_route = Routes(data['departure'], data['arrival'], data['autonomy'])
new_route.check_routes()

countdown_check = Countdown(new_route.cost_list, countdown_data["countdown"])
countdown_check.countdown_val()

print(new_route.cost_list)

# print(countdown_data["bounty_hunters"])