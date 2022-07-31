class Countdown():

    def __init__(self, cost_list, countdown):
        self.cost_list = cost_list
        self.countdown = countdown
        self.valid_countdown = []
        self.min_countdown = 0

    def countdown_val(self):
        for i in self.cost_list:
            
            if i > self.countdown:
                pass
            else:
                self.valid_countdown.append(i)
                print("You have destroyed the Deathstar!")
                self.min_countdown = min(self.valid_countdown)