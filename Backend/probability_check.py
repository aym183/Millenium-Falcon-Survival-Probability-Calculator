class Probability():

    def __init__(self, bounty_hunters, valid_countdown):
        self.bounty_hunters = bounty_hunters
        self.valid_countdown = valid_countdown
        self.probability = []
        self.days = []
        self.trouble_days = 0
        self.final_probability = 0

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
                    
        print(str(self.trouble_days) + " Here you go")
        self.probability_answer()
        

    def probability_answer(self):
        
        if self.trouble_days == 0:
            self.final_probability = 0

        elif self.trouble_days == 1:

            self.final_probability = 0.1

        else:
            
            for i in range(1, self.trouble_days):
            
                self.final_probability += (9**(i))/(10**(i+1))
            
            self.final_probability += 0.1

