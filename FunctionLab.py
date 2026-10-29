from cmu_graphics import *
#evan

def drawCircle(x,y,c):
    Circle(x,y,20,fill = c)
    
def drawStar(x,y,c):
    Star(x,y,20,5,fill = c)
    
drawCircle(100,100,'green')  
drawStar(100,300,'green')

drawCircle(150,100,'red')  
drawStar(150,300,'red')

drawCircle(200,100,'purple')  
drawStar(200,300,'purple')

drawCircle(250,100,'yellow')  
drawStar(250,300,'yellow')

drawCircle(300,100,'blue')  
drawStar(300,300,'blue')
cmu_graphics.loop()
