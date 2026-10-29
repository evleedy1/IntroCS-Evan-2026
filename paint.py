from cmu_graphics import *
#evan

#brushColor = 'black'

#pallet
Rect(0,0,400,30,fill='gainsboro',border = 'grey')
colorSelect =Label("pick a color", 300,15, size =12, align = 'left')
red = Circle(50,15,12.5,fill='red')
orange = Circle(75,15,12.5,fill='orange')
yellow = Circle(100,15,12.5,fill='yellow')
green = Circle(125,15,12.5,fill='green')
blue = Circle(150,15,12.5,fill='blue')
purple = Circle(175,15,12.5,fill='purple')

clear = Rect(200,2,50,26,fill='darkGrey')
Label('clear',225,15)
canvas= Rect(0,30,400,370,fill = 'white')
def onMousePress(mouseX,mouseY):
    brushColor='black'
    if (red.contains(mouseX,mouseY)):
        brushColor = red.fill
    elif (orange.contains(mouseX,mouseY)):
        brushColor = orange.fill
    elif (yellow.contains(mouseX,mouseY)):
        brushColor = yellow.fill
    elif (green.contains(mouseX,mouseY)):
        brushColor = green.fill
    elif (blue.contains(mouseX,mouseY)):
        brushColor = blue.fill
    elif (purple.contains(mouseX,mouseY)):
        brushColor = purple.fill
    elif (clear.contains(mouseX,mouseY)):
        canvas.toFront()
    else:
        brushColor = colorSelect.value
        
    colorSelect.value = brushColor
    print(colorSelect.value)
    if (mouseY>42.5):
      Circle(mouseX,mouseY,5,fill = colorSelect.value)
    
    

cmu_graphics.loop()
