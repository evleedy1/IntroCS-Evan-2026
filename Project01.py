#Evan Leedy
from cmu_graphics import *
Rect(0,0,400,100,fill=gradient('deepSkyBlue','lightSkyBlue',start='top')) # sky

Rect(0,200,400,200,fill=gradient('bisque','tan',start='top'))# sand
Oval(0,200,50,20,fill='paleTurquoise',border='white',borderWidth=5) # waves
Oval(60,200,80,40,fill='paleTurquoise',border='white',borderWidth=5)
Oval(120,200,40,30,fill='paleTurquoise',border='white',borderWidth=5)
Oval(180,200,100,30,fill='paleTurquoise',border='white',borderWidth=5)
Oval(220,200,40,15,fill='paleTurquoise',border='white',borderWidth=5)
Oval(280,200,80,30,fill='paleTurquoise',border='white',borderWidth=5)
Oval(400,200,80,40,fill='paleTurquoise',border='white',borderWidth=5)
Oval(320,200,30,20,fill='paleTurquoise',border='white',borderWidth=5)
Oval(335,200,50,20,fill='paleTurquoise',border='white',borderWidth=5)

Rect(0,100,400,100,fill=gradient('royalBlue','paleTurquoise',start='top')) #sea

#umbrela
Oval(300,300,180,80,opacity=20)#shadow
Rect(300,180,8,140,fill=gradient('lightgrey','grey','lightgrey',start='left'),rotateAngle=10)#pole
Arc(315,185,200,120,275,200,fill='red',border='black')#base
#Arc(315,185,200,120,275,50,fill='red')
Arc(315,185,200,120,325,50,fill='white',border='black')#stripes
Arc(315,185,200,120,430,50,fill='white',border='black')
Circle(346,124,5,fill='red',border='black')#top

Star(50,50,30,200,fill=gradient('gold','lightYellow')) #sun

Circle(320,50,25,fill='white')
Circle(300,60,25,fill='white')
Circle(350,60,20,fill='white')
Circle(330,70,15,fill='white')

Polygon(120,380,200,380,190,240,130,240,120,380,fill=gradient('darkOrange','violet','lightgreen'),border='black',borderWidth=2) # bugged will not render border correctly

cmu_graphics.loop()