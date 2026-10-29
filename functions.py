from cmu_graphics import *
#evan
def drawHexagon(x,y,size,borderSize,fillColor):
    RegularPolygon(x,y,size,6,fill = fillColor, border = 'green', borderWidth = borderSize)

drawHexagon(200,100,100,0,'Green')
drawHexagon(200,300,100,5,None)


cmu_graphics.loop()