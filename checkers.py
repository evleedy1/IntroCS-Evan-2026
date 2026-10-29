from cmu_graphics import *
places=8
placeSize=400/places
blackSquares= Group()
whiteSquares= Group()

for y in range(places):
    for x in range(places):
        if((x+y)%2==0):
            #newRect = Rect(x*placeSize,y*placeSize,placeSize,placeSize,fill='gray')
            blackSquares.add(Rect(x*placeSize,y*placeSize,placeSize,placeSize,fill='gray'))
        else:
            whiteSquares.add(Rect(x*placeSize,y*placeSize,placeSize,placeSize,fill='white'))
            
    

cmu_graphics.loop()