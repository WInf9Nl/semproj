import numpy as np
from scipy import integrate
import math
import matplotlib as mpl
import matplotlib.pyplot as plt

class Dynamics:

    def __init__(self, growthfactor=0, startvalue=0, psv=0, gfofpy=0, gfofpr=0, dfofpy=0, dfofpr=0):
     self.gfofpy = gfofpy
     self.gfofpr =  gfofpr
     self.dfofpy = dfofpy
     self.dfofpr = dfofpr
     self.gf = growthfactor
     self.sv = startvalue
     self.psv = psv
     self.ordinates = []
     self.abscissa = []

    def lin(self, time, steps, discrete):
        if discrete == True:
            return self.gf*self.sv*(time//steps) + self.sv
        else:
            self.abscissa = np.arange(0, time, steps)
            for i in self.abscissa:
                self.ordinates.append(self.gf*self.sv*i + self.sv)
            fig = plt.figure()
            fig.figsize = (8, 8)
            ax = plt.subplot('211')
            ax.plot(self.abscissa, self.ordinates)
            fig.savefig('plot.png')


    def exp(self, time, steps, discrete):
        if discrete == True:
            return self.sv*math.exp(self.gf*(time//steps))
        else:
            self.abscissa = np.arange(0, time + steps, steps)
            for i in self.abscissa:
                self.ordinates.append(self.sv*math.exp(self.gf*i))
            fig = plt.figure()
            ax = plt.subplot('211')
            ax.plot(self.abscissa, self.ordinates)
            fig.savefig('plot.png')

    def log(self, time, steps, discrete, capacity):
        if discrete == True:
            return (capacity*self.sv*math.exp(self.gf*(time//steps))/(capacity + self.sv*(math.exp(self.gf*(time//steps))-1)))
        else:
            self.abscissa = np.arange(0, time, steps)
            for i in self.abscissa:
                self.ordinates.append((capacity*self.sv*math.exp(self.gf*i))/(capacity + self.sv*(math.exp(self.gf*i))-1))
            fig = plt.figure()
            ax = plt.subplot('211')
            ax.plot(self.abscissa, self.ordinates)
            fig.savefig('plot.png', frameon=None)

    def lotvol(self, time, steps, discrete):
            t = np.arange(0, time, steps)
            n = np.array([self.sv, self.psv])
            def alg(y, t, a, b, c, d):
                return np.array([y[0]*a - y[0]*y[1]*b, -y[1]*c + b*d*y[0]*y[1]])
            solution = integrate.odeint(alg, n, t, args=(self.gfofpy, self.dfofpy, self.gfofpr, self.dfofpr))
            prey, predator = solution.T
            if discrete == True:
                return [prey[len(prey) - 1], predator[len(predator) - 1]]
            else:
                fig = plt.figure()
                ax = plt.subplot('211')
                predatorlabel = mpl.patches.Patch(color='red', label='Predator')
                ax.legend(handles=[predatorlabel])
                preylabel = mpl.patches.Patch(color='blue', label='Prey')
                ax.legend(handles=[preylabel])
                ax.plot(t, prey, 'b')
                ax.plot(t, predator, 'r', label='predator')
                ax.grid()
                fig.savefig('plot.png')
