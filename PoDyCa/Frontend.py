from appJar import gui
from Backend import Dynamics
import numpy as np
import sys
import os.path
import pylab as p

def calculatesub(btn):
    for i in entrysofsub.keys():
        try:
            entrysofsub[i] = float(app.getEntry(i))
        except:
            entrysofsub[i] = 0
            app.setMessage('Solution', 'Please provide all needed data')
            return
    if app.getRadioButton('Calculationtypesub') == 'Discrete':
        preypredator = Dynamics(growthfactor=0, startvalue=entrysofsub['sizeprey'],gfofpr=entrysofsub['growthofpredator'], gfofpy=entrysofsub['growthofprey'], dfofpr=entrysofsub['deathrateofpredator'], dfofpy=entrysofsub['deathrateofprey'], psv=entrysofsub['predatorsize'])
        ansol = preypredator.lotvol(entrysofsub['timeoflotvol'], entrysofsub['stepsoflotvol'], True)
        app.setMessage('Solution', 'Prey: {0}\nPredator: {1}'.format(ansol[0], ansol[1]))
    else:
        for i in entrysofsub:
            if entrysofsub[i] == 0:
                app.setMessage('Solution', 'Please provide all needed data')
                return
        preypredator = Dynamics(growthfactor=0, startvalue=entrysofsub['sizeprey'], gfofpr=entrysofsub['growthofpredator'], gfofpy=entrysofsub['growthofprey'], dfofpr=entrysofsub['deathrateofpredator'], dfofpy=entrysofsub['deathrateofprey'], psv=entrysofsub['predatorsize'])
        preypredator.lotvol(entrysofsub['timeoflotvol'], entrysofsub['stepsoflotvol'], False)
        app.reloadImage('plot', './plot.png')
    app.hideSubWindow('lotvol')

def calculate(btn):
    if os.path.isfile('plot.png'):
        os.remove('plot.png')
    app.clearMessage('Solution')
    dynamictype = app.getOptionBox('Dynamics')
    for i in entrys.keys():
        try:
            entrys[i] = float(app.getEntry(i))
        except:
            entrys[i] = 0
    if dynamictype == 'Lotka/Volterra':
            app.showSubWindow('lotvol')
            return
    for i in entrys.keys():
        if entrys[i] == 0:
            if i != 'capacity':
                app.setMessage('Solution', 'Please provide the {0}\n'.format(i))
                return
            elif i == 'capacity' and dynamictype == 'Logistic':
                app.setMessage('Solution', 'Please provide the capacity\n')
                return

    if dynamictype == 'Linear':
        if app.getRadioButton('Calculationtype') == 'Discrete':
            population = Dynamics(entrys['growthfactor'], entrys['startvalue'])
            solution = population.lin(entrys['time'], entrys['steps'], True)
            app.setMessage('Solution', str(solution))
        else:
            population = Dynamics(entrys['growthfactor'], entrys['startvalue'])
            population.lin(entrys['time'], entrys['steps'], False)
            app.reloadImage('plot', './plot.png')
    elif dynamictype == 'Exponential':
        if app.getRadioButton('Calculationtype') == 'Discrete':
            population = Dynamics(entrys['growthfactor'], entrys['startvalue'])
            solution = population.exp(entrys['time'], entrys['steps'], True)
            app.setMessage('Solution', str(solution))
        else:
            population = Dynamics(entrys['growthfactor'], entrys['startvalue'])
            population.exp(entrys['time'], entrys['steps'], False)
            app.reloadImage('plot', './plot.png')
    elif dynamictype == 'Logistic':
        if app.getRadioButton('Calculationtype') == 'Discrete':
            population = Dynamics(entrys['growthfactor'], entrys['startvalue'])
            app.setMessage('Solution', str(population.log(entrys['time'], entrys['steps'], True, entrys['capacity'])))
        else:
            population = Dynamics(entrys['growthfactor'], entrys['startvalue'])
            population.log(entrys['time'], entrys['steps'], False, entrys['capacity'])
            app.reloadImage('plot', './plot.png')

app = gui('PoDyCa', '600x600')
app.setBg('Aqua')
app.addLabelOptionBox('Dynamics', ['Linear', 'Exponential', 'Logistic', 'Lotka/Volterra'])
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
app.setEntryDefault('capacity', 'Capacity')
app.addButton('Calculate', calculate)
app.addEmptyMessage('Solution')
app.addImage('plot', './default.png')
entrys = {'startvalue': None, 'growthfactor': None, 'time': None, 'steps': None, 'capacity': None}
for i in entrys.keys():
    app.setEntryBg(i, 'DarkOrange')
app.startSubWindow('lotvol', 'Lotka/Volterra', modal=True)
app.setBg('Tan')
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
app.setEntryDefault('timeoflotvol', 'Time')
app.addEntry('stepsoflotvol')
app.setEntryDefault('stepsoflotvol', 'Steps')
globals().update(entrysofsub = {'growthofprey': None, 'deathrateofprey': None, 'sizeprey': None, 'growthofpredator': None, 'deathrateofpredator': None, 'predatorsize': None, 'timeoflotvol': None, 'stepsoflotvol': None})
for y in entrysofsub.keys():
	app.setEntryBg(y, 'SaddleBrown')
app.addButton('Solve', calculatesub)
app.stopSubWindow()
app.go()
