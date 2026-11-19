from cmu_graphics import *
c = Circle(200,200,30,fill = 'green')

def onKeyHold(keys):
    if ('up' in keys):
        c.centerY -= 2
    if ('down' in keys):
        c.centerY += 2
    if ('left' in keys):
        c.centerX -= 2
    if ('right' in keys):
        c.centerX += 2
    if (c.centerY > 350 or c.centerY < 50):
        c.centerX = 200
        c.centerY = 200
    if (c.radius >= 5):
        if (c.centerX < 50):
            c.radius -= 2
    
    if (c.centerX > 350):
        c.radius += 2
    
def onKeyPress(key):
    if (key == 'space'):
        if(c.fill == 'blue'):
            c.fill = 'green'
        else:
            c.fill = 'blue'
    
cmu_graphics.loop()