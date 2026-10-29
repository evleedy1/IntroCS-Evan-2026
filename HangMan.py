from cmu_graphics import *


gameOver = False
           

Rect(0,370,400,30) # ground

Line(30,370,30,200,lineWidth = 5) 
Line(30,200,150,200,lineWidth = 5)
Line(150,200,150,220,lineWidth = 3)

man = [
    Circle(150,235,15,fill = None,border = 'black',borderWidth = 3,visible = False), # head 
    Line(150,250,150,300,lineWidth = 3,visible = False), # body
    Line(150,300,125,335,lineWidth = 3,visible = False), #legs
    Line(150,300,175,335,lineWidth = 3,visible = False),
    Line(150,250,125,285,lineWidth = 3,visible = False), #arms
    Line(150,250,175,285,lineWidth = 3,visible = False)
    ]

missedGuesses = -1 # the number of failed guesses
# I used AI to create the list of of words and letters to save some time
# A list of words for the game
words = ["absolute", "actually", "addition", "although", "building", "business", "children", "complete", "computer", "consider", "continue", "decision", "directly", "district", "economic", "elephant", "evidence", "football", "hospital", "keyboard", "learning", "mountain", "notebook", "organize", "painting", "personal", "planning", "possible", "pressure", "probably", "property", "remember", "required", "schedule", "sentence", "southern"]

word = choice(words) # gives a random item in the list
print(word)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # a list of the 26 letters

i = 0
j = 0

letterDisplay = list() # will be a list containing lables with thw values in letters

for letter in letters: # for each letter in letters
    temp = Label(letter.upper(),0,0,size = 30,fill = 'grey') # create a label with the value of the letter we are on
    temp.left = i * 25 + 20 # set positions after the fact because it aligns them to the center for some reason
    temp.bottom = j * 30 + 40
    letterDisplay.append(temp) # add it to the list of labels
    i += 1 # increase the counter
    if (i > 12): # if the counter gets big enough reset it and increment another counter
        j += 1
        i = 0
def onKeyPress(key):
    global missedGuesses
    if (not gameOver):
    
        if (key in letters): # if the key pressedis a valid letter
            if (key in word): # is it in the word?
                letterDisplay[letters.index(key)].fill = 'green' # if so set the letter to green
            elif (not key in word):# is it not in the word?
                letterDisplay[letters.index(key)].fill = 'red' # set it to red, increment the counter and show another part of the man
            
                man[missedGuesses].visible = True
                missedGuesses += 1
            
        print(missedGuesses)
    
        if (missedGuesses == 5):
            Rect(50,150,300,100,fill = 'darkGrey')
            Label('Game Over',200,200,size = 50)
            gameOver = True

cmu_graphics.loop()
