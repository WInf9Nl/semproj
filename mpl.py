from appJar import gui
from pogro import Dynamics
from scipy import integrate
from numpy import *
import sys
import os.path
import pylab as p

def lotvol(discrete):
    a = entrysofsub['growthofprey']
    b = entrysofsub['deathrateofprey']
    c = entrysofsub['deathrateofpredator']
    d = entrysofsub['growthofpredator']
    time = linspace(0, entrysofsub['timeoflotvol'], entrysofsub['stepsoflotvol'])
    X = array([entrysofsub['sizeprey'], entrysofsub['predatorsize']])

    if discrete == True:
        def eq(X, t=0):
            return array([(a*X[0]) - (b*X[0]*X[1]),
                  -c*X[1] + d*b*X[0]*X[1] ])
    else:
        def eq(X, t=0):
            return array([(a*X[0]) - (b*X[0]*X[1]),
                  (-c*X[1]) + (d*b*X[0]*X[1])])
        solution = integrate.odeint(eq, X, time)
        prey, predators = solution.T
        f1 = p.figure()
        ax = p.subplot('211')
        ax.plot(time, prey, 'r-', label='Prey')
        ax.plot(time, predators, 'b-', label='predators')
        ax.grid()
        ax.legend(loc='best')
        p.xlabel('time')
        p.ylabel('population')
        p.title('Evolution of prey and predator populations')
        f1.savefig('plot.png')
        app.stopSubWindow()
        app.destroySubWindow('lotvol')
        app.reloadImage('plot', './plot.png')

def calculatesub(btn):
    for i in entrysofsub.keys():
        try:
            entrysofsub[i] = float(app.getEntry(i))
        except:
            entrysofsub[i] = 0
    if app.getRadioButton('Calculationtypesub') == 'Discrete':
        for i in entrysofsub:
            if entrysofsub[i] == 0 and i != 'steps':
                app.setMessage('Error', 'Please provide all needed data')
                pass
        lotvol(True)
    else:
        for i in entrysofsub:
            if entrysofsub[i] == 0:
                app.setMessage('Error', 'Please provide all needed data')
                pass
        lotvol(False)

def calculate(btn):
    if os.path.isfile('plot.png'):
        os.remove('plot.png')
    dynamictype = app.getOptionBox('Dynamics')
    for i in entrys.keys():
        try:
            entrys[i] = float(app.getEntry(i))
        except:
            entrys[i] = 0
    if dynamictype == 'Lotka/Volterra':
            app.startSubWindow('lotvol', 'Lotka/Volterra', modal=True)
            app.addRadioButton('Calculationtypesub', 'Discrete')
            app.addRadioButton('Calculationtypesub', 'Continous')
            app.addEntry('growthofprey')
            app.setEntryDefault('growthofprey', 'Growthrate of prey')
            app.addEntry('deathrateofprey')
            app.setEntryDefault('deathrateofprey', 'Deathrate of prey per meet')
            app.addEntry('sizeprey')
            app.setEntryDefault('sizeprey', 'Populationsize of prey')
            app.addEntry('growthofpredator')
            app.setEntryDefault('growthofpredator', 'Growth of predator per meet')
            app.addEntry('deathrateofpredator')
            app.setEntryDefault('deathrateofpredator', 'Deathrate of predator')
            app.addEntry('predatorsize')
            app.setEntryDefault('predatorsize', 'Populationsize of predator')
            app.addEntry('timeoflotvol')
            app.setEntryDefault('timeoflotvol', 'time')
            app.addEntry('stepsoflotvol')
            app.setEntryDefault('stepsoflotvol', 'Steps')
            globals().update(entrysofsub = {'growthofprey': None, 'deathrateofprey': None, 'sizeprey': None, 'growthofpredator': None, 'deathrateofpredator': None, 'predatorsize': None, 'timeoflotvol': None, 'stepsoflotvol': None})
            app.addEmptyMessage('Error')
            app.addButton('subcalculate', calculatesub)
            app.showSubWindow('lotvol')
            pass
    growthfactor = entrys['growthfactor']
    startvalue = entrys['startvalue']
    time = entrys['time']
    steps = entrys['steps']
    capacity = entrys['capacity']
    for i in entrys.keys():
        if entrys[i] == 0 and i != 'capacity':
            app.setMessage('Solution', 'Please provide the {0}'.format(i))
            pass
    try:
        if dynamictype == 'Linear':
            if app.getRadioButton('Calculationtype') == 'Discrete':
                population = Dynamics(growthfactor, startvalue)
                solution = population.lin(time, steps, True)
                app.setMessage('Solution', str(solution))
            else:
                population = Dynamics(growthfactor, startvalue)
                population.lin(time, steps, False)
                app.reloadImage('plot', './plot.png')
        elif dynamictype == 'Exponential':
            if app.getRadioButton('Calculationtype') == 'Discrete':
                population = Dynamics(growthfactor, startvalue)
                solution = population.exp(time, steps, True)
                app.setMessage('Solution', str(solution))
            else:
                population = Dynamics(growthfactor, startvalue)
                population.exp(time, steps, False)
                app.reloadImage('plot', './plot.png')
        elif dynamictype == 'Logistic':
            if entrys['capacity'] == 0:
                app.setMessage('Solution', 'Please provide the capacity')
                pass
            if app.getRadioButton('Calculationtype') == 'Discrete':
                population = Dynamics(growthfactor, startvalue)
                app.setMessage('Solution', str(population.log(time, steps, True, capacity)))
            else:
                population = Dynamics(growthfactor, startvalue)
                population.log(time, steps, False, capacity)
                app.reloadImage('plot', './plot.png')
    except:
        app.setMessage('Solution', 'Sorry an error occured')

app = gui('PoDyCa', '600x600')
app.setBg('DarkKhaki')
app.addLabelOptionBox('Dynamics', ['Linear', 'Exponential', 'Logistic', 'Lotka/Volterra'], 0, 0, 2)
app.addRadioButton('Calculationtype', 'Discrete')
app.addRadioButton('Calculationtype', 'Continous')
app.addEntry('startvalue')
app.setEntryDefault('startvalue', 'Populationsize')
app.addEntry('growthfactor')
app.setEntryDefault('growthfactor', 'Growthrate')
app.addEntry('time')
app.setEntryDefault('time', 'Time')
app.addEntry('steps')
app.setEntryDefault('steps', 'Steps')
app.addEntry('capacity')
app.setEntryDefault('capacity', 'Kapazitaet')
app.addButton('Calculate', calculate)
app.addImage('plot', './default.png')
app.addEmptyMessage('Solution')
entrys = {'startvalue': None, 'growthfactor': None, 'time': None, 'steps': None, 'capacity': None}
for i in entrys.keys():
    app.setEntryBg(i, 'PaleGoldenRod')
app.go()
