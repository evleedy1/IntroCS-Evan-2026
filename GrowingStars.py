from cmu_graphics import *

s1 = Star(200,200,175,8,fill = 'blue',opacity = 50,roundness = 40)
s2 = Star(200,200,175,8,fill = 'red',opacity = 50,roundness = 40)
def onKeyHold(keys):
    if ('up' in keys):
        if (s2.roundness == 0):
            s1.roundness = 0
            s2.roundness = 100
        else:
            s1.roundness += 2
            s2.roundness -= 2
    if ('down' in keys):
        if (s1.roundness == 0):
            s2.roundness = 0
            s1.roundness = 100
        else:
            s2.roundness += 2
            s1.roundness -= 2
        

cmu_graphics.loop()