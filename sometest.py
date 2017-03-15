from appJar import gui

def main():
    podycamain = gui('PoDyCa')
    podycamain.setBg('White')
    growthmenu = ['Exponential', 'Logistic', 'Prey/Predator']
    def expgui():
        podycamain.addEntry('growfactor')
        podycamain.setEntryDefault('growfactor', 'Growth Rate')
        def hello():
            a = podycamain.getEntry('growfactor')
            print(a)
        podycamain.addButton('Push Me', hello())
        a = podycamain.getEntry('growfactor')

    def loggui():
        pass

    def preypreda():
        pass

    def regressgui():
        pass
    funcmenu = [expgui(), loggui(), preypreda()]
    podycamain.addMenuList('Growthmodel', growthmenu, funcmenu)
    podycamain.addMenuList('Input', ['Regression'], regressgui())
    podycamain.go()


main()
