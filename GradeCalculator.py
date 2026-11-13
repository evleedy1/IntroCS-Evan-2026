#Evan
from cmu_graphics import *

grade = float(app.getTextInput('Enter % Grade'))

if(grade > 92):
    app.showMessage("A  -  Greate Job!")
elif(grade > 80):
    app.showMessage("B  -  Solid Effort!")
elif(grade > 65):
    app.showMessage("C  -  Passing!")
elif(grade > 50):
    app.showMessage("D  -  Time to Hit The Books!")
else:
    app.showMessage("F  -  Oh Dear!")