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
            if app.getRadioButton('Calculationtype') == 'discrete':
                population = Dynamics(growthfactor, startvalue)
                solution = population.lin(time, steps, True)
                app.setMessage('Solution', str(solution))
            else:
                population = Dynamics(growthfactor, startvalue)
                population.lin(time, steps, False)
                app.reloadImage('plot', './plot.png')
        elif dynamictype == 'Exponential':
            if app.getRadioButton('Calculationtype') == 'discrete':
                population = Dynamics(growthfactor, startvalue)
                solution = population.exp(time, steps, True)
                app.setMessage('Solution', str(solution))
            else:
                population = Dynamics(growthfactor, startvalue)
                population.exp(time, steps, False)
                app.reloadImage('plot', './plot.png')
        elif dynamictype == 'Logistic':
            if app.getRadioButton('Calculationtype') == 'discrete':
                population = Dynamics(growthfactor, startvalue)
                app.setMessage('Solution', str(population.log(time, steps, True, capacity)))
            else:
                population = Dynamics(growthfactor, startvalue)
                population.log(time, steps, False, capacity)
                app.reloadImage('plot', './plot.png')
    except:
        app.setMessage('Solution', 'Sorry an error occured')

app = gui('PoDyCa')
app.setBg('white')
app.addLabelOptionBox('Dynamics', ['Linear', 'Exponential', 'Logistic', 'Lotka/Volterra'])
app.addRadioButton('Calculationtype', 'discrete')
app.addRadioButton('Calculationtype', 'continous')
app.addEntry('startvalue')
app.addEntry('growthfactor')
app.addEntry('time')
app.addEntry('steps')
app.addEntry('capacity')
app.addButton('Calculate', calculate)
app.addImage('plot', './default.png')
app.addEmptyMessage('Solution')
entrys = {'startvalue': None, 'growthfactor': None, 'time': None, 'steps': None, 'capacity': None}
app.go()
