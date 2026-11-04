from cmu_graphics import *


# CABIN IN THE WOODS - STARTER CODE
# Canvas coordinates run from 0 to 400 in both directions.
app.width = 400
app.height = 400

# The background objects are named so you can change them later.

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
Rect(280, 175, 27, 57, fill='fireBrick', border='black', borderWidth=2)
Line(280, 195, 307, 195, fill='black')
Line(280, 214, 307, 214, fill='black')

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

# YOUR CODE STARTS HERE.
# 1. Create the windows and door as named objects.
# 2. Create a sun, moon, and smoke (use .visible to show/hide).
# 3. Create state variables to remember day/night, lights, door, fire.
# 4. Write onMousePress(mouseX, mouseY) using coordinate ranges.
#    Call makeFish(mouseX, mouseY) when the lake is clicked.
#    Important: check the corner controls BEFORE the general sky area.

skyCircle = Circle(350,30,25,fill = 'yellow')

isDayTime = True

stars = Group()



def onMousePress(mouseX,mouseY):
    
    global isDayTime
    global skyCircle
    global stars
    
    # day/night
    if (mouseX >= 350 and mouseY >= 350):
        if (isDayTime):
            app.background = 'black'
            skyCircle.fill = 'lightCyan'
            stars.visible = True
            isDayTime = False
        else:
            app.background = 'skyBlue'
            skyCircle.fill = 'Yellow'
            stars.visible = False
            isDayTime = True
    #clouds/stars
    if (mouseY < 275 and mouseX < 300):
        if (isDayTime):
            cloud = makeCloud(mouseX,mouseY)
            cloud.toBack() # send to back so it can be behind mountains
        else:
            star = Star(mouseX,mouseY,10,5,fill = 'lightYellow')
            star.toBack()
            stars.add(star)
    if(pond.hits(mouseX,mouseY)):
        makeFish(mouseX,mouseY)
        

cmu_graphics.loop()
