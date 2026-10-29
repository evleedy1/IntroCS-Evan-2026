from cmu_graphics import *
#evan
b1 = Rect(100,200,40,20, fill = 'blue')
b2 = Rect(300,300,30,40, fill = 'red')

def onMousePress(mouseX,mouseY):
    b1.visible = False
def onMouseRelease(mouseX,mouseY):
    b1.visible = True
    

cmu_graphics.loop()