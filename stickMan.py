from cmu_graphics import *
#evan
app.background = gradient('yellow','orange','red')

Circle(200,135,25) # head
Line(200,160,200,240)#body
# arms
left = Line(200,185,150,175)
right = Line(200,185,250,175)
left.up = False
right.up = False
#legs
Line(200,240,230,300)
Line(200,240,170,300)

def onKeyPress(key):
    if key == 'right':
        right.up = not right.up
    elif key == 'left':
        left.up = not left.up
    else:
        right.up = not right.up
        left.up = not left.up
        
    if left.up:
        left.y2 = 125
    else:
        left.y2 = 175
        
    if right.up:
        right.y2 = 125
    else:
        right.y2 = 175

cmu_graphics.loop()