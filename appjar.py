from appJar import gui
import random
def randomcolour():
    x = random.randint(0, 3)
    colours = ['blue', 'red', 'green', 'white']
    return colours[x]

app = gui('PodyCa')
pressedhowmanytimes = 5
app.addLabel('thereistrouble')
def press(name):
    global pressedhowmanytimes
    if pressedhowmanytimes == 0:
        app.stop()
    pressedhowmanytimes -= 1
    app.setLabel('thereistrouble', 'Now we working with some funny numbers like this' + str(pressedhowmanytimes))
    app.setBg(randomcolour())
app.addButton('Press me', press)
app.go()
