
def add_2(x):
    return x+2

class Maths(object):
    def __init__(self, x):
        self.x = x
    def add_2(self):
        return self.x+2
    def __add__(self, other):
        return self.x + other.x
    def __eq__(self, other):
        return self.x == other.x

print(add_2(5))

Obj = Maths(5)
Obj2 = Maths(5)
print(Obj==Obj2)

