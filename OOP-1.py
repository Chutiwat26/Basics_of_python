# simple class

class Player:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.number = ""

class Player2:
    def __init__(self, first_name, last_name, number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number

if __name__ == '__main__':
    p1 = Player()
    p1.first_name = "chutiwat"
    p1.last_name = "tanapibalwongsa"
    p1.number = 26
    print(p1.first_name)

    p1a = Player2("chutiwat","Tanapibalwongsa",26)  
    print(p1a.last_name)

    p1b = ("chutiwat", "tanapibalwongsa", 1) #tuple
    print(p1b)
    print(p1b[0])

    p1c = {"first_name" : "chutiwat", "last_name" : "tanapibalwongsa", "number" : 26} # dictionary
    print(p1c)
    print(p1c["number"])

    