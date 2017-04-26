from appJar import gui
from pogro import Dynamics
import sys
import os.path

def calculate(btn):
    if os.path.isfile('plot.png'):
        os.remove('plot.png')
    dynamictype = app.getOptionBox('Dynamics')
    for i in entrys.keys():
        try:
            entrys[i] = float(app.getEntry(i))
        except:
            entrys[i] = 0
    growthfactor = entrys['growthfactor']
    startvalue = entrys['startvalue']
    time = entrys['time']
    steps = entrys['steps']
    capacity = entrys['capacity']
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
