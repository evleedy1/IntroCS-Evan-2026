from cmu_graphics import *

app.background = 'darkSeaGreen'
ticks = 0
# paths
Rect( 40,0,20,400, fill = 'grey')
Rect(60,350,340,20,fill = 'grey')
Rect(240,370,20,30,fill = 'grey')
Rect(60,140,340,20,fill = 'grey')
Rect(290,160,20,190,fill = 'grey')

# ferris Wheel

def cabin(x,y,col):
    cabin = Group(
    Rect(x,y,25,20,fill = col,border ='darkGrey',borderWidth = 1),
    Rect(x + 3,y + 4, 18,9,fill = 'lightBlue',border ='darkGrey',borderWidth = 2)
    )
    return cabin

Line(330,70,300,120,fill = gradient('red','red','darkRed',start = 'top'),lineWidth = 5)
Line(330,70,360,120,fill = gradient('red','red','darkRed',start = 'top'),lineWidth = 5)
Oval(330,70,25,20,fill = 'grey')
Rect(295,120,70,20,fill = 'darkGrey')

supports = Group()
supportNum = 8
angle = 360 / supportNum
for i in range(supportNum):
    x,y = getPointInDir(330,70,angle * i,45) # get the point at an angle and distance from a center point
    supports.add(Line(330,70,x,y,fill = 'grey',lineWidth = 3))
    
Oval(330,70,100,90,fill = None,border = 'red',borderWidth = 5)

cabins = [ cabin(0,0,'red'),cabin(0,0,'blue'),cabin(0,0,'green'),cabin(0,0,'pink') ] # create list of cabins


# Roller Coaster

#tracks
Line(130,300, 240,300, fill = 'steelBlue', lineWidth = 5)
Line(240,300,260,280, fill = 'steelBlue', lineWidth = 5)
Line(260,280, 260,200, fill = 'steelBlue', lineWidth = 5)
Line(260,200, 170,160, fill = 'steelBlue', lineWidth = 5)
Line(170,160, 140,200, fill = 'steelBlue', lineWidth = 5)
Line(140,200, 110,200, fill = 'steelBlue', lineWidth = 5)
Line(110,200, 110,280, fill = 'steelBlue', lineWidth = 5)
Line(110,280, 130,300, fill = 'steelBlue', lineWidth = 5)

# supports
Line(130,300, 130,320, fill = 'grey', lineWidth = 3)
Line(195,300, 195,320, fill = 'grey', lineWidth = 3)
Line(240,300, 240,320, fill = 'grey', lineWidth = 3)
Line(170,160, 170,220, fill = 'grey', lineWidth = 3)
Line(140,200, 140,220, fill = 'grey', lineWidth = 3)
Line(215,180, 215,220, fill = 'grey', lineWidth = 3)
Line(125,200, 125,220, fill = 'grey', lineWidth = 3)
Line(237.5,190, 237.5,220, fill = 'grey', lineWidth = 3)
Line(192.5,170, 192.5,220, fill = 'grey', lineWidth = 3)
Line(155,180, 155,220, fill = 'grey', lineWidth = 3)
Line(160,300, 160,320, fill = 'grey', lineWidth = 3)
Line(110,280, 110,300, fill = 'grey', lineWidth = 3)
Line(260,280, 260,300, fill = 'grey', lineWidth = 3)

#car

rollerCoasterCar = Rect(160,150,20,10,fill = 'darkRed',rotateAngle = 25)



# food Carts

def foodCart(x,y,col):
    foodCart = Group(
    Rect(x,y,30,20, fill = 'snow'),
    Rect(x,y+15,30,5,fill = col),
    Rect(x,y + 30,30,10,opacity = 20),
    Rect(x,y + 20,30,15,fill = 'ghostWhite'),
    Line(x,y+30,x+30,y+30,fill = col),
    Rect(x + 5,y + 20, 3, 8, fill = gradient('grey','darkGrey','grey',start = 'left')),
    Rect(x + 25,y + 20, 3, 8, fill = gradient('grey','darkGrey','grey',start = 'left'))
    )
    return foodCart

foodCarts = [
foodCart(110,358,'red'),
foodCart(150,355,'yellow'),
foodCart(200,355,'blue')
]

goingDown = False

def onMousePress(mouseX,mouseY):

    global goingDown

    for foodCart in foodCarts:
        if (foodCart.contains(mouseX,mouseY)):
            print('food Cart clicked')
    if (rollerCoasterCar.contains(mouseX,mouseY)):
        goingDown = True
    
def onStep():
    global goingDown

    supports.rotateAngle += 0.5
    
    global ticks
    ticks += 1
    
    # spin ferris wheel Cabins
    for i in range(len(cabins)):
        x,y = getPointInDir(330,70,(90 * i) + (ticks/2),45)
        cabins[i].centerX = x
        cabins[i].centerY = y
    if goingDown:
        rollerCoasterCar.centerX += 2
        rollerCoasterCar.centerY += 0.88888 # 2x the slope of the line from (170,160) to (260,280)
        if rollerCoasterCar.centerX > 260:
            goingDown = False
            rollerCoasterCar.centerX = 170
            rollerCoasterCar.centerY = 155
    
cmu_graphics.loop()