from cmu_graphics import *
app.background = 'lightGreen'
c = Circle(200,200,100,fill='red')
def fillCircle(color,x,y):
    c.fill = color
    star(x,y,10,4,fill=color)
    N
def onMousePress(mouseX,mouseY):
    if(mouseX <200):
       c.fill = 'blue'
    else:
        c.fill = 'green'

cmu_graphics.loop()