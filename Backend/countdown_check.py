class Countdown():

    def __init__(self, cost_list, countdown):
        self.cost_list = cost_list
        self.countdown = countdown
        self.valid_countdown = []

    def countdown_val(self):
        for i in self.cost_list:
            
            if i > self.countdown:
                pass
            else:
                self.valid_countdown.append(i)
                print("You have destroyed the Deathstar!")