from cmu_graphics import *
app.background = 'black'

def drawStar(x,y):
    
    Star(x,y,100,12,fill = gradient('red','white'),roundness = 10)
    Star(x,y,100,12,fill = gradient('yellow','white'),roundness = 10,rotateAngle = 10)
    Star(x,y,100,12,rotateAngle = 5,roundness = 10)
def drawTrace(x,y):
    Line(x,y,x,400,fill = gradient('black','yellow','red','black',start = 'top'))
    
def onMousePress(mouseX,mouseY):
    if (mouseY < 150):
        drawStar(mouseX,mouseY)
    else:
        drawTrace(mouseX,mouseY)
    
cmu_graphics.loop()