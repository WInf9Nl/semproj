from appJar import gui
from numpy import sin, pi, arange

x = arange(0.0, 3.0, 0.01)
y = sin(2*pi*x)

app = gui()
axes = app.addPlot("p1", x, y)
app.go()
