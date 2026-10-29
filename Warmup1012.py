from cmu_graphics import *


app.background = 'lightGreen'
c1 = Circle(200,200,40,fill='red')
count = Label(0,200,25,size = 24)

def changeCircleColor(col):
    c1.fill = col
    count.value += 1
def onMousePress(mouseX,mouseY):
    if (mouseX > 200 and mouseY > 200):
        changeCircleColor('blue')
    if (mouseX < 200 and mouseY > 200):
        changeCircleColor('yellow')
    if (mouseX < 200 and mouseY < 200):
        changeCircleColor('red')
    if (mouseX > 200 and mouseY < 200):
        changeCircleColor('green')

cmu_graphics.loop()