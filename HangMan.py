from cmu_graphics import *

'''
def binarySearch(array,target):
    lowerBound = 0
    upperBound = len(array)
    
    while(true
          checking = int(((upperBound - lowerBound) / 2) + lowerBound)
          if (upperBound-lowerBound == 1):
              raise execption('not in array')
          if array[checking
 '''           

Rect(0,370,400,30) # ground

Line(30,370,30,200,lineWidth = 5) 
Line(30,200,150,200,lineWidth = 5)
Line(150,200,150,220,lineWidth = 3)

man = [
    Circle(150,235,15,fill = None,border = 'black',borderWidth = 3), # head 
    Line(150,250,150,300,lineWidth = 3), # body
    Line(150,300,125,335,lineWidth = 3), #legs
    Line(150,300,175,335,lineWidth = 3),
    Line(150,250,125,285,lineWidth = 3), #arms
    Line(150,250,175,285,lineWidth = 3)
    ]

missedGuesses = 0
# I used AI to create the listo of words and letters to save some time
words = ["absolute", "actually", "addition", "although", "building", "business", "children", "complete", "computer", "consider", "continue", "decision", "directly", "district", "economic", "elephant", "evidence", "football", "hospital", "keyboard", "learning", "mountain", "notebook", "organize", "painting", "personal", "planning", "possible", "pressure", "probably", "property", "remember", "required", "schedule", "sentence", "southern"]

word = choice(words) # gives a random item in the list
print(word)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

x = 0
y = 0
letterDisplay = list()

for letter in letters:
    temp = Label(letter.upper(),0,0,size = 30,fill = 'grey')
    temp.left = x * 25 + 20 # set positions after the fact because it aligns them to the center for some reason
    temp.bottom = y * 30 + 40
    letterDisplay.append(temp)
    x += 1
    if (x > 12):
        y += 1
        x = 0
def onKeyPress(key):
    print('pressed')
    if (key in word):
        print('correct')
        temp[ indexOf ].        
cmu_graphics.loop()