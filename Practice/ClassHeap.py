class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def add(self, delx, dely):
        self.x += delx
        self.y += dely


p = Point(5, 6)
p.add(1,1)

print(str(p.x)+" , "+str(p.y))


