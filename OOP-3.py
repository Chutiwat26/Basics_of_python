#self

class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
    
    def total(self):  # instance method
        return self.gold + self.silver + self.bronze

    #def __str__(self):
    #    return "{:15} g:{:3} s:{:3} b:{:3} t:{:3}".format(self.country, self.gold, self.silver, self.bronze, self.total()) # :XX mean length of space

    def __repr__(self): # string representation
        return "{}{}".format(self.__class__.__name__, repr((self.country, self.gold, self.silver, self.bronze)))

if __name__ == '__main__':
    #th = Medal("Thailand", 1, 2, 3)
    #print(th)
    #print(th.country, "g", th.gold, "s", th.silver, "b", th.bronze, "t", th.total())
    m = [
        Medal("Japan", 5, 4, 3),
        Medal("Korea", 8, 4, 7),
        Medal("China", 7, 5, 7)
    ]

    for c in m:
        print(c)