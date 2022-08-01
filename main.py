import json
from Database.route_check import Routes
from Backend.countdown_check import Countdown
from Backend.probability_check import Probability
from Database.travel_time import Travel

f = open('Backend/practice-millennium-falcon.json')
data = json.load(f)

g = open('Backend/practice-empire.json')
countdown_data = json.load(g)

class Main():

    def __init__(self, departure, arrival, autonomy, bounty_hunters, countdown):
        self.departure = departure
        self.arrival = arrival
        self.autonomy = autonomy
        self.bounty_hunters = bounty_hunters
        self.countdown = countdown


    def run_method(self):

            new_route = Routes(self.departure, self.arrival, self.autonomy)
            new_route.check_routes()

            for i in range(len(new_route.path)):
                if self.departure not in new_route.path[i]:
                    new_route.path[i].insert(0, self.departure)

            print(new_route.path)

            travel_check = Travel(new_route.path)
            travel_check.travel_time_check()

            print(travel_check.path)

            countdown_check = Countdown(travel_check.path, self.countdown)
            countdown_check.countdown_val()

            probability_check = Probability(self.bounty_hunters, countdown_check.valid_countdown)
            probability_check.probability_val()

            # print(countdown_check.valid_countdown

            if max(probability_check.probability) == 0:
                print('0% chance of survival')
                return 0

            else:
                final_value = int((1 - max(probability_check.probability))*100)
                print(str(final_value)+ '% chance of survival')
                return final_value


if __name__ == '__main__':
    new_method = Main(data['departure'], data['arrival'], data['autonomy'], countdown_data['bounty_hunters'], countdown_data['countdown'])
    new_method.run_method()
