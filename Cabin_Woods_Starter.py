#Evan

from cmu_graphics import *

time = 0


#sky = Rect(0, 0, 400, 275, fill='skyBlue')
app.background = 'skyBlue'

# Mountains
Polygon(0, 275, 95, 105, 205, 275, fill='slateBlue')
Polygon(40, 205, 95, 105, 150, 205, 110, 190, 95, 201, 78, 189, fill='white')
Polygon(145, 275, 285, 125, 400, 275, fill='mediumPurple')
Polygon(230, 184, 285, 125, 338, 184, 306, 175, 286, 188, 267, 175, fill='white')

# Ground and lake
Rect(0, 275, 400, 125, fill='forestGreen')
pond = Oval(40, 385, 240, 135, fill='dodgerBlue', border='navy', borderWidth=2)

# Pine trees
Rect(35, 240, 16, 65, fill='saddleBrown')
Polygon(43, 140, 8, 245, 78, 245, fill='darkGreen', border='black')
Rect(102, 250, 14, 48, fill='saddleBrown')
Polygon(109, 165, 75, 265, 144, 265, fill='darkGreen', border='black')
Rect(363, 245, 14, 62, fill='saddleBrown')
Polygon(370, 145, 330, 255, 399, 255, fill='darkGreen', border='black')

# Cabin body, roof, and chimney are already drawn.
Rect(165, 224, 160, 105, fill='peru', border='black', borderWidth=2)
Line(165, 246, 325, 246, fill='saddleBrown', lineWidth=2)
Line(165, 269, 325, 269, fill='saddleBrown', lineWidth=2)
Line(165, 292, 325, 292, fill='saddleBrown', lineWidth=2)
Line(165, 315, 325, 315, fill='saddleBrown', lineWidth=2)
Polygon(150, 226, 194, 181, 297, 181, 340, 226,fill='maroon', border='black', borderWidth=2)

# Draw chimney AFTER the roof so it appears on top.
chimney = Rect(280, 175, 27, 57, fill='fireBrick', border='black', borderWidth=2)
Line(280, 195, 307, 195, fill='black')
Line(280, 214, 307, 214, fill='black')

#windows
windows = Group(
Rect(270,240,35,30,border = 'black'),
Rect(180,240,35,30,border = 'black')
)

#smoke
smoke = Group(
    Circle(293,160,15,fill = 'grey'), 
    Circle(300,140,10,fill = 'grey'),
    Circle(290,125,13,fill = 'grey'), 
)
smoke.visible = False

# door
door = Rect(225,265,35,65,fill = 'maroon',border = 'black')
doorKnob = Circle(255,300,3,fill = 'gold')
# Example helper: draw a fish at the mouse position.
def makeFish(mouseX, mouseY):
    return Group(
    Oval(mouseX, mouseY, 20, 10, fill='orange', border='darkOrange'),
    Polygon(mouseX - 9, mouseY, mouseX - 19, mouseY - 8,
            mouseX - 19, mouseY + 8, fill='orange'),
    Circle(mouseX + 6, mouseY - 2, 1.5, fill='black')
    )
    
def makeCloud(x,y):
    return Group(
    Circle(x,y,10,fill = 'white'),
    Circle(x - 9,y,7,fill = 'white'),
    Oval(x - 7, y + 6,30,10,fill = 'white')
    )


skyCircle = Circle(350,30,25,fill = 'yellow')

isDayTime = False

stars = Group()



def onMousePress(mouseX,mouseY):
    
    global isDayTime
    global skyCircle
    global stars
    '''
    # control day/night
    if (mouseX >= 350 and mouseY >= 350):
        if (isDayTime):
            isDayTime = False
        else:
            app.background = 'skyBlue'
            skyCircle.fill = 'Yellow'
            stars.visible = False
            isDayTime = True
    '''
            
    #clouds/stars
    if (mouseY < 275 and mouseX < 300):
        if (not isDayTime):
            cloud = makeCloud(mouseX,mouseY)
            cloud.toBack() # send to back so it can be behind mountains
        else:
            star = Star(mouseX,mouseY,10,5,fill = 'lightYellow')
            stars.add(star)
            stars.toBack()
    if(pond.hits(mouseX,mouseY)):
        makeFish(mouseX,mouseY)
    
    #Windows day/night
    if(isDayTime): # is it night?
        if (windows.contains(mouseX,mouseY)): # did the user click on the windows?
            windows.toFront()
            if (windows.fill == 'black'): # if the lights are off turn them on
                windows.fill = 'yellow'
            else: # otherwise turn them off
                windows.fill = 'black'
    else: # turn lights off if its day
        windows.fill = 'black'
        
    #chimney/smoke
    if(chimney.contains(mouseX,mouseY)):
        if(not windows.fill == 'black'):
            if (smoke.visible):
                smoke.visible = False
            else:
                smoke.visible = True
                
    # door open/close
    if(door.contains(mouseX,mouseY)):
        if (door.fill == 'black'):
            door.fill = 'maroon'
            doorKnob.visible = True
        else:
            door.fill = 'black'
            doorKnob.visible = False
    
    
def onStep():
    global time
    global isDayTime
    
    time += 1
    
    skyCircle.centerX,skyCircle.centerY = getPointInDir(200,600,(-time/12) + 23,550)
    
    if(skyCircle.centerX <= 0):
        time = 0
        if (isDayTime):
            isDayTime = False
        else:
            isDayTime = True
            
    if (isDayTime):
        app.background = 'black'
        skyCircle.fill = 'lightCyan'
        stars.visible = True
    else:
        app.background = 'skyBlue'
        skyCircle.fill = 'Yellow'
        stars.visible = False
    
cmu_graphics.loop()
