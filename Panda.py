from cmu_graphics import *
#evan
Circle(100,100,40)
Circle(300,100,40)
Circle(200, 400, 175)
Circle(200,200,130, fill = 'white')

Oval(250,170 ,60,80,rotateAngle = -30)
Oval(150, 170, 60, 80,rotateAngle = 30)
Circle(160, 160, 15, fill = 'white')
Circle(240, 160, 15, fill = 'white')
Circle(160, 160, 5)
Circle(240, 160, 5)

nose = Oval(200, 200, 50, 30)
mouth = Arc(200, 250, 50, 50, 90, 180, fill = 'lightCoral')

Label('Bamboo Eaten', 150, 15 , size = 20, bold = True)
counter = Label('0', 300, 15, size = 20, bold = True)   



cheek = Oval(275, 250, 60, 70,fill = 'white',border = 'black', borderWidth = 3,visible = False)
Rect(240, 212, 40, 70, fill = 'white')
bamboo = Rect(120, 265, 25, 410, fill = gradient('oliveDrab','darkOliveGreen','darkGreen'), rotateAngle = 20)

counter2 = 0

def onMousePress(mouseX, mouseY):
    global counter2
    counter2 += 1

    mouth.visible = False
    cheek.visible = True
    counter.value = counter2
    nose.centerX = 200
    nose.centerY = 190
def onMouseRelease(mouseX, mouseY):
    mouth.visible = True
    cheek.visible = False
    nose.centerX = 200
    nose.centerY = 200
    



cmu_graphics.loop()