import numpy as np
import matplotlib as mp


class Dynamics:                                 #dynamics are populations with different ways for growth

    def __init__(self, growthfactor, startvalue):
     self.gf = growthfactor
     self.sv = startvalue

    def exp(self, timeintervall, steps, disorcont):
        if disorcont == True:
            self.exptime = self.gf*timeintervall        #percentage of growth
            return self.sv*self.exptime               #population after timeintervall
        else:
            momentvalue = self.sv
            for i in range(0, timeintervall, steps):
                if momentvalue > 1:
                    break
                momentvalue = (self.sv*self.gf**i) // 1
            self.populationvalues.append(self.momentvalue)

    def log(self, timeintervall, capacity):
        self.
bacteria = Dynamics(1.4, 200)

print(bacteria.exp(5))
