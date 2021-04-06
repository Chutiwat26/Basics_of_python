class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        #return "fname: {} lname: {} age: {}".format(self.fname, self.lname, self.age)
        
        #a = vars(self) # vars change value to dictionary format
        #s = ["{:10}: {}".format(k, v) for k, v in a.items()]
        #print(a)

        attrs = ("fname", "lname", "age")
        s = ["{:10}: {}".format(a, getattr(self, a)) for a in attrs] # getattr mean get attribute, for this method you can set position of attribute by switch attribute in tupble attrs
        return "\n".join(s)

if __name__ == "__main__":
    p = Person("chutiwat", "tanapibalwongsa", 27)
    print(p)