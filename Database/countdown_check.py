class Countdown():

    def __init__(self, cost_list, countdown):
        self.cost_list = cost_list
        self.countdown = countdown

    def countdown_val(self):
        for i in self.cost_list:
            
            if i > self.countdown:
                pass
            else:
                print("You have destroyed the Deathstar!")