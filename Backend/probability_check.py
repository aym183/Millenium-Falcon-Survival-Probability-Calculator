class Probability():

    def __init__(self, bounty_hunters, valid_countdown):
        self.bounty_hunters = bounty_hunters
        self.valid_countdown = valid_countdown
        self.probability = []
        self.days = []
        self.trouble_days = 0

    def probability_val(self):
        for i in self.bounty_hunters:
            
            self.days.append(i['day'])
        print(self.days)
        self.probability_check()

    def probability_check(self):
        for i in self.valid_countdown:
            for j in range(1, i+1):
                if j in self.days:
                    self.trouble_days+=1
                    
        print(self.trouble_days)
        