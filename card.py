class Card:
    def __init__(self, carddata):
        self.cardid = carddata[0]
        self.cost = carddata[1]
        self.name = carddata[2]
        if carddata[3] == '':
            self.ex = 0
        else:
            self.ex = 1
        self.type = carddata[4]  
        self.job = carddata[5]
        self.category = carddata[6]
        self.power = carddata[7]
        self.ability = carddata[8]


    def ToArray(self):
        ret = [self.cardid,self.name,self.ability,self.cost,self.power,self.job,self.category, self.type, self.ex]
        return ret