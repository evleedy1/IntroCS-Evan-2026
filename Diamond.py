from cmu_graphics import *
#Evan Leedy
Polygon(100,100,300,100,340,150,200,300,60,150,fill=gradient('white','lightBlue'),border='black')
Polygon(200,100,275,150,200,300,125,150,fill='azure',border='black')
Line(60,150,340,150)
Line(100,100,125,150)
Line(300,100,275,150)
Star(265,125,15,6,fill='white',roundness=15)




cmu_graphics.loop()