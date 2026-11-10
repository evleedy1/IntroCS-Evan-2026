from cmu_graphics import *

app.background = 'skyBlue'
c = Circle(200,200,100)
def onKeyPress(key):
    if key == 'up':
        c.fill = 'red'
    elif key == 'down':
        c.fill = 'blue'

cmu_graphics.loop()