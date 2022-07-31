class Countdown():

    def __init__(self, path, countdown):
        self.path = path
        self.countdown = countdown
        self.valid_countdown = []
        self.min_countdown = 0

    def countdown_val(self):
        for i in self.path:           
            
            if i[0] > self.countdown:
                pass
            else:
                self.valid_countdown.append(i[0])
                print("You have destroyed the Deathstar!")
                # self.min_countdown = min(self.valid_countdown)
        print(self.valid_countdown)