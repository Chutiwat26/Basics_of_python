def immutable_demo():  #int, str, float are imutable
    n = 5
    print("id(n) = {}, n = {}".format(id(n), n))
    n = n + 5
    print("id(n) = {}, n = {}".format(id(n), n))

def mutable_demo():
    p = ["rain"]
    print("id(p) = {}, p = {}".format(id(p), p))
    p[0] = p[0] + "bow"
    print("id(p) = {}, p = {}".format(id(p), p))
    q = p
    print("id(p) = {}, p = {}\nid(q) = {}, q = {}".format(id(p), p, id(q), q))
    q.append("sunshrine")
    print("id(p) = {}, p = {}\nid(q) = {}, q = {}".format(id(p), p, id(q), q))

if __name__ == "__main__":
    immutable_demo()
    mutable_demo()