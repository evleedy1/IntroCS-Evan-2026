from cmu_graphics import *
#evan

Rect(0,0,400,400,fill = 'black')
blueFlash =  Rect(0,0,400,400,fill = gradient('steelBlue','black'),visible = False)
button = Rect(90,135,40,15, fill = 'steelBlue')
Rect(50,150,300,200,fill = 'lightblue')
Circle(245,250,80,fill = 'white', border = 'steelblue', borderWidth = 10)
Circle(245,250,50,fill = 'black')
Rect(200,120,40,35,fill = 'white',border = 'lightBlue', borderWidth = 10)
flash = Star(220,130,200,12,fill =gradient('white','yellow','gold'),roundness = 30, visible =False)

def onMousePress(mouseX,mouseY):
    flash.visible = True
    blueFlash.visible = True
    button.centerY += 10
    
def onMouseRelease(mouseX,mouseY):
    flash.visible = False
    blueFlash.visible = False
    button.centerY -= 10

cmu_graphics.loop()