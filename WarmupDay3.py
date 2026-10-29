from cmu_graphics import *
#evan

Oval(200,200,200,100,fill='green')
Circle(200,150,50,opacity= 75,fill='skyBlue')
Rect(0,0,200,200,fill="blue",opacity=50)
Rect(200,200,200,200,fill='red',opacity=50)
Circle(200,200,20,fill='green',border='blue',borderWidth=5)
Line(0,0,200,200,fill='blue',lineWidth=5,arrowEnd=True,dashes=True)
Label('Here',230,200,size= 20,font='orbitron')

cmu_graphics.loop()