import numpy as np
import math
import matplotlib.pyplot as plt

class Dynamics:

    def __init__(self, growthfactor, startvalue):
     self.gf = growthfactor
     self.sv = startvalue
     self.ordinates = []
     self.abscissa = []

    def lin(self, time, steps, discrete):
        if discrete == True:
            return self.gf*time + self.sv
        else:
            x = 0
            while x < time:
                momentvalue = self.gf*x + self.sv
                if momentvalue < 1:
                    break
                else:
                    self.ordinates.append(momentvalue)
                    self.abscissa.append(x)
                    x += steps
            fig = plt.figure()
            ax = plt.subplot('211')
            ax.plot(self.abscissa, self.ordinates)
            fig.savefig('plot.png', frameon=None)


    def exp(self, time, steps, discrete):
        if discrete == True:
            return self.sv*math.exp(self.gf*time)
        else:
            x = 0
            while x < time:
                momentvalue = self.sv*math.exp(self.gf*x)
                if momentvalue < 1:
                    break
                else:
                    self.ordinates.append(momentvalue)
                    self.abscissa.append(x)
                    x += steps
            fig = plt.figure()
            ax = plt.subplot('211')
            ax.plot(self.abscissa, self.ordinates)
            print(self.ordinates)
            fig.savefig('plot.png')

    def log(self, time, steps, discrete, capacity):
        if discrete == True:
            return (capacity*self.sv*math.exp(self.gf*time))/(capacity + self.sv*(math.exp(self.gf*time)-1))
        else:
            x = 0
            while x < time:
                momentvalue = (capacity*self.sv*math.exp(self.gf*x))/(capacity + self.sv*(math.exp(self.gf*x)-1))
                if momentvalue < 1:
                    break
                else:
                    self.ordinates.append(momentvalue)
                    self.abscissa.append(x)
                    x += steps
            fig = plt.figure()
            ax = plt.subplot('211')
            ax.plot(self.abscissa, self.ordinates)
            fig.savefig('plot.png', frameon=None)
	def lotvol(self, time, steps, discrete)