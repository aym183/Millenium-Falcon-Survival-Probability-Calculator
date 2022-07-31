import json
from Database.route_check import Routes
from Backend.countdown_check import Countdown
from Backend.probability_check import Probability

f = open('Backend/practice-millennium-falcon.json')
data = json.load(f)

g = open('Backend/practice-empire.json')
countdown_data = json.load(g)

new_route = Routes(data['departure'], data['arrival'], data['autonomy'])
new_route.check_routes()

countdown_check = Countdown(new_route.cost_list, countdown_data["countdown"])
countdown_check.countdown_val()

probability_check = Probability(countdown_data['bounty_hunters'], countdown_check.valid_countdown)
probability_check.probability_val()

final_value = int((1 - probability_check.final_probability)*100)

print(str(final_value)+'%')

# print(countdown_check.valid_countdown)
# print(probability_check.final_probability)

# print(countdown_data["bounty_hunters"])