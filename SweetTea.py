from cmu_graphics import *
 
Rect(0,0,400,400, fill='paleTurquoise') #background
 
Rect(150,100,150,270,fill='azure')#cup

Rect(155, 160, 140, 205,fill = gradient("gold",'yellow',start ='bottom')) #tea

#straw
brown=rgb(92,68,39)
Rect(250,50,10,300,fill = gradient(brown,'gold',start= "top"))
Rect(250,50, 100,10, fill =brown )

#ice cubes
Rect(190,200,50,50, fill='moccasin')
Rect(170,280,50,50, fill='moccasin')
cmu_graphics.loop()