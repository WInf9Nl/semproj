import numpy as np
import matplotlib as mp


class Dynamics:

    def __init__(self, growthfactor, startvalue):
     self.gf = growthfactor
     self.sv = startvalue

     def exp(self, timeintervall):
         growth = self.gf*timeintervall
         return self.sv*growthfactor**growth

bacteria = Dynamics(1.4, 200)

print(bacteria.exp(5))
