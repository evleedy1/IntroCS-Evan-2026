from cmu_graphics import *
#Evan
def landscape():
    app.background = 'black'
    Rect(0,0,400,250, fill = 'darkBlue')
    Circle(200,90,60,fill = 'lemonChiffon')
    Circle(200,400,60, fill = 'lemonChiffon', opacity = 20)
    
def drawReflection(mouseX):
    Rect(mouseX,250,60,150,fill = 'grey')
    
def drawBuilding(mouseX,mouseY):
    Rect(mouseX,mouseY,60,250-mouseY,fill = 'black')
    drawReflection(mouseX)
    
    
landscape()

def onMousePress(mouseX,mouseY):
    drawBuilding(mouseX,mouseY)
cmu_graphics.loop()