#evan
from cmu_graphics import *

Rect(190,0,10,400)
Rect(200,0,10,400,fill = 'tan')

def footprint(x,y,color):
    Oval(x,y,15,30,fill = color)
    Circle(x,y+15,7,fill = color)
    Rect(x-7.5,y+5,15,7,fill = 'white')
def onMousePress(x,y):
    if (x > 200):
        footprint(x,y,'tan')
    else:
        footprint(x,y,'black')
cmu_graphics.loop()