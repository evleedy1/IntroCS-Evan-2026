from cmu_graphics import *
 
c = Circle(200,200,100)

def onKeyPress(key):
    if (key == 'left'):
        c.fill = 'red'
    elif (key == 'right'):
        c.fill = 'blue'
    else:
        c.fill = 'black'
cmu_graphics.loop()