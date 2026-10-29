from cmu_graphics import *
#evan
Rect(0,0,400,400,fill="lightSkyBlue")
Rect(200,330,10,400,fill="white")
Oval(200,185,300,340,fill=gradient("salmon","crimson",start="top-left"))

def onMousePress(mouseX,mouseY):
    Line(mouseX,mouseY,mouseX + 40,mouseY - 20,fill="lightGray")
    Circle(mouseX + 40,mouseY - 20,5,fill=gradient("lightCyan","skyBlue",start="top-left"))
def onMouseRelease(mouseX,mouseY):
    Star(200,200,210,9,fill="gray",roundness=10)
    Star(200,200,190,9,fill="lightSkyBlue",roundness=70)

cmu_graphics.loop()