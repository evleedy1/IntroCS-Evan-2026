from cmu_graphics import *

app.background = 'lightGreen'
ticks = 0
# paths
Rect( 40,0,20,400, fill = 'grey')
Rect(60,350,340,20,fill = 'grey')
Rect(240,370,20,30,fill = 'grey')

# ferris Wheel

def cabin(x,y,col):
    cabin = Group(
    Rect(x,y,25,20,fill = col),
    Rect(x + 3,y + 4, 18,9,fill = 'lightBlue')
    )
    return cabin

Line(330,70,300,120,fill = gradient('red','red','darkRed',start = 'top'),lineWidth = 5)
Line(330,70,360,120,fill = gradient('red','red','darkRed',start = 'top'),lineWidth = 5)
Oval(330,70,25,20,fill = 'grey')

supports = Group()
supportNum = 8
angle = 360 / supportNum
for i in range(supportNum):
    x,y = getPointInDir(330,70,angle * i,45) # get the point at an angle and distance from a center point
    supports.add(Line(330,70,x,y,fill = 'grey',lineWidth = 3))
    
Oval(330,70,100,90,fill = None,border = 'red',borderWidth = 5)

cabins = [ cabin(0,0,'red'),cabin(0,0,'blue'),cabin(0,0,'green'),cabin(0,0,'pink') ] # create list of cabins

Rect(255,120,70,40,fill = 'grey')





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

def onMousePress(mouseX,mouseY):
    for foodCart in foodCarts:
        if (foodCart.contains(mouseX,mouseY)):
            print('food Cart clicked')
    
def onStep():
    supports.rotateAngle += 0.5
    
    global ticks
    ticks += 1
    
    # spin ferris wheel Cabins
    for i in range(len(cabins)):
        x,y = getPointInDir(330,70,(90 * i) + (ticks/2),45)
        cabins[i].centerX = x
        cabins[i].centerY = y
    
cmu_graphics.loop()