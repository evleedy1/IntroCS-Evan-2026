from cmu_graphics import *

counter = 0

def makeStar(x,y,col):
    Star(x,y,15,5,fill = col)
    
def onMousePress(x,y):
    
    global counter
    
    if (counter < 5):
        makeStar(x,y,'green')
    else:
        makeStar(x,y,'red')
    counter += 1
cmu_graphics.loop()
    
    