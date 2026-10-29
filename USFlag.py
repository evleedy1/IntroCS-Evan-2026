from cmu_graphics import *
flagHeight=200
stripeHeight =flagheight/13
flagWidth = 400
for i in range(13):
    if(i%2 == 1):
        Rect(0,stripeHeight*i,flagWidth,stripeHeight, fill ='snow')
    else:
        Rect(0,stripeHeight*i,flagWidth,stripeHeight, fill ='red')
Rect(0,0, flagWidth/3,flagHeight/2)
    
cmu_graphics.loop()