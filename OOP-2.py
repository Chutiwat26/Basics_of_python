class Person:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.country = "Thailand"

#create OOP with defualt value
class Person2:
    def __init__(self, fname = None, lname = None, country = "Thailand"):
        self.fname = fname
        self.lname = lname
        self.country = country
    
    def __str__(self):
        return "fname: {} lname: {} country: {}".format(self.fname, self.lname, self.country)

if __name__ == "__main__":
    p1 = Person2()
    print(p1.fname)
    print(p1.country)

    p2 = Person2(fname = 'Peter')
    print(p2.fname, p2.country)

    p3 = Person2('peter','parker')
    print(p3)

    p4 = Person2(lname='tanapibalwongsa', country='thailand', fname='chutiwat')
    print(p4)

