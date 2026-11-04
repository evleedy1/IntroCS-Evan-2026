from cmu_graphics import *

box = Rect(100,200,60,40,fill = 'yellow')

def onMousePress(mouseX,mouseY):
    if (box.width < 100):
        box.width += 10
    else:
        box.width -= 10
        
cmu_graphics.loop()