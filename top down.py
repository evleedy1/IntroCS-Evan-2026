from cmu_graphics import *

# made by Evan
# wasd to move
# space to jump

'''
class NPC: # a class holds properties and methods
    def __init__(self,x,y,name,dialog): # constructor for the class to specify properties
        self.x = x
        self.y = y
        self.name = name
        self.dialog = dialog
        self.talkRange = Circle(x,y,100,fill = None,dashes = True,border = 'black')
        self.visual = Circle(x,y,25,fill = 'blue')
    def __setattr__(self):
        selfr
        
     
    def updateLocation():
        self.visual.centerX = self.x
        self.visual.centerY = self.y
        self.talkRange.centerX = self.x
        self.talkRange.centerY = self.y
   
   ''' 


speed = 4 # player move speed

def makeGround():# returns a group (combine multiple objects into one)
    return Group(Rect(-400,-400,1200,1200,fill = 'darkGreen'), Rect(0,0,50,50,fill ='gray'),Rect(300,200,50,50,fill ='gray'),Rect(30,200,50,50,fill ='gray'))

def makeGroundCollider():
    collider = Group(Rect(0,0,50,50,fill = 'gray'),Rect(300,200,50,50,fill = 'gray'),Rect(30,200,50,50,fill = 'gray'))
    collider.visible = True
    return collider

ground = makeGround() #initialize ground visual object
groundCollider = makeGroundCollider() # initialize ground collider

# player objects
shadow = Rect(175,200,50,30,opacity = 20)
player = Rect(175,175,50,50,fill = gradient('lightBlue','powderBlue'),border = 'cornflowerBlue',borderWidth = 2,dashes = True)

#if one of these objects collides with the ground collider stop moneement in that direction
top = Rect(180,170,40,10,visible = False)
bottom = Rect(180,220,40,10,visible = False)
left = Rect(170,180,10,40,visible = False)
right = Rect(220,180,10,40,visible = False)

walkCycleTime = 0

moveOffsetX = 0
moveOffsetY = 0

#firstNPC = NPC(350,200,'a','a')

def onKeyHold(key):
    global moveOffsetX
    global moveOffsetY
    
    global walkCycleTime
    
    walkCycleTime += 20 # a counter that increases when we walk
    player.centerY += dsin(walkCycleTime) # move the player up and down based on the timer
    
    if ('w' in key): # check if the w key is pressed
        if(not top.hitsShape(groundCollider)):# the .hitsShape method returns true if the object contains any part of the parameter object
            moveOffsetY += speed
            
    if ('a' in key):
        if(not left.hitsShape(groundCollider)):
            moveOffsetX += speed
            
    if ('s' in key):
        if(not bottom.hitsShape(groundCollider)):
            moveOffsetY -= speed
            
    if ('d' in key):
        if(not right.hitsShape(groundCollider)):
            moveOffsetX -= speed
            
    ground.centerX = moveOffsetX
    ground.centerY = moveOffsetY
    groundCollider.centerX = moveOffsetX-25
    groundCollider.centerY = moveOffsetY-75 # these offsets  need to be modifyed for any change :(
            
    
def onKeyPress(key):
    if('space' in key):# jump
        player.centerY -= 20
        
def onStep():
    #global player
    if (player.centerY < 200): #if the player jumped return it to the ground
        player.centerY += 2
    
    
        

cmu_graphics.loop()