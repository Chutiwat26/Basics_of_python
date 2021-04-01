def demo_tuple():
    p12 = "joe", "Gomez", 12
    print(p12)
    print(p12[1])

def demo_dict():
    p12 = {"first_name":"Joe", "last_name":"Gomez","number":12}
    print(p12)
    print(p12["last_name"])

#class like declare new data type
class Player:
    pass

class Player2:
    def __init__(self, first_name, last_name, number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number

def demo_simple_player_class():
    p12 = Player()
    p12.first_name = "Joe"
    p12.last_name = "Gomez"
    p12.number = 12
    print(p12.first_name)

def demo_simple_player2_class():
    p12 = Player2("Joe", "Gomez", 12)
    print(p12.first_name)

if __name__ == '__main__':
    #demo_tuple()
    #demo_dict()
    #demo_simple_player_class()
    demo_simple_player2_class()