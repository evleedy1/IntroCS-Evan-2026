from cmu_graphics import *

Circle(200,200,200,fill=gradient("red","darkRed",start="left"))
Circle(200,200,160,fill=gradient("white","grey",start="left"))
Circle(200,200,120,fill=gradient("red","darkRed",start="left"))
Circle(200,200,80,fill=gradient("blue","darkBlue",start="left"))
Star(200,200,75,5,fill=gradient("white","grey",start="left"))

cmu_graphics.loop()