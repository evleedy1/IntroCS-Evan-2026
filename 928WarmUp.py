from cmu_graphics import *
#evan
c = Circle(200,200,20,fill="red")

def onMousePress(mouseX,mouseY):
    c.fill = "blue"
    c.centerX = mouseX
    c.centerY = mouseY

cmu_graphics.loop()