class Probability():

    def __init__(self, bounty_hunters, valid_countdown):
        self.bounty_hunters = bounty_hunters
        self.valid_countdown = valid_countdown
        self.probability = []
        self.days = []
        self.trouble_days = 0
        self.final_probability = 0
        self.trouble_list = []

    # Method to get all the possible days that could be potentially dangerous
    def probability_val(self):
        for i in self.bounty_hunters:
            
            self.days.append(i['day'])
        self.probability_check()

    # Method to calculate all the days that overlap within the path cost and bounty hunters
    def probability_check(self):
        for i in self.valid_countdown:
            for j in range(1, i+1):
                if j in self.days:
                    self.trouble_days+=1

            self.trouble_list.append(self.trouble_days)
            self.trouble_days=0
 
        for i in range(len(self.trouble_list)):      
            self.probability_answer(self.trouble_list[i])
        
    # Method to calculate all the days that overlap within the path cost and bounty hunters
    def probability_answer(self, trouble_value):
   
        if trouble_value == 0:
            self.final_probability = 0
            self.probability.append(self.final_probability)

        elif trouble_value == 1:

            self.final_probability = 0.1
            self.probability.append(self.final_probability)

        else:
            
            for i in range(1, trouble_value):
            
                self.final_probability += (9**(i))/(10**(i+1))
            
            self.final_probability =round(self.final_probability, 2)
            self.final_probability += 0.1
            self.probability.append(self.final_probability)
            self.final_probability=0

