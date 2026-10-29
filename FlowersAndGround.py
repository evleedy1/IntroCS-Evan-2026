from cmu_graphics import *

# sky and ground
app.background = 'deepSkyBlue'
Rect(0,255,400,145,fill = 'oliveDrab')
Oval(200,255,400,20,fill = 'oliveDrab')
cloudCount = Label(0,370,20,size = 30)
flowerCount = Label(0,380,380,size = 30)

def drawCloud(x,y,col):
    Circle(x + 20, y, 40, fill = col)
    Circle(x - 20, y, 40, fill = col)
    Circle(x + 40, y, 30, fill = col)
    Circle(x - 40, y, 30, fill = col)
    cloudCount.value += 1
    
def drawFlower(x,y):
    Oval(x,y,10,30,fill = 'deepPink')
    Oval(x,y,10,30,fill = 'hotPink',rotateAngle = 60)
    Oval(x,y,10,30,fill = 'deepPink',rotateAngle = 120)
    Circle(x,y,4,fill = 'yellow')
    flowerCount.value += 1

def onMousePress(mouseX,mouseY):
    if (mouseY > 250):
        drawFlower(mouseX,mouseY)
    else:
        drawCloud(mouseX,mouseY,'gray')
cmu_graphics.loop()