"""felszin/ terfogata kiiratasa
magassag
sugar"""
import math
class Henger:
     def __init__(self, m, r):
          self.m = m
          self.r = r
     def Setmagassag(self, m):
          self.m = m
     def Setsugar(self, r):
           self.r = r
     def Getmagassag(self):
          return self.m
     def Getsugar(self):
          return self.r
     def Felszine(self):
          return 2*self.r**2*math.pi+2*self.r*math.pi*self.m
     def Terfogata(self):
          return self.r**2*math.pi*self.m

Henger = Henger(5,10)
print(Henger.Felszine())
print(Henger.Terfogata())
