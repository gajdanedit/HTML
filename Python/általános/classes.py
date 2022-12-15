class Teglalap:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b
    
    def setA(self, a):
        self.a = a
    def setB(self, b):
        self.b = b
    def setAB(self, a, b):
        self.a = a
        self.b = b
    
    def getA(self):
        return self.a
    def getB(self):
        return self.b
    def getKerulet(self):
        return 2 * (self.a + self.b)
    def getTerulet(self):
        return self.a * self.b

class Négyzet:
    def __init__(self, a = 0):
        self.a = a
    
    def setA(self, a):
        self.a = a
    
    def getA(self):
        return self.a
    def getKerulet(self):
        return 4 * self.a
    def getTerulet(self):
        return self.a ** 2

