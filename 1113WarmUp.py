from cmu_graphics import*

app.background = 'skyBlue'
username = app.getTextInput('enter your name')

someText = Label('hello' + username,100,200,size = 16)

cmu_graphics.loop()