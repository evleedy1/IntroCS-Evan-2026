from cmu_graphics import *
app.background = 'black'

# a few constants for the terminal
textSize = 12
textWidth= 7.25

# list of charcaters that when type don't return their chacrater
specialCharacters = ('enter','tab','escape','backspace','space','up','down','left','right')
# a list of the numbers as strings
numbers = ('0','1','2','3','4','5','6','7','8','9')
'''
line varibles
'''
lines = list()
currentLine= 'type'
currentLineLabel = Label(currentLine,0,0,fill = 'white',size = textSize, font = 'monospace')


'''
cursor variables
'''
cursor = Rect(15,378,5,textSize, fill = 'white')
cursorTimer = 0
cursorInterval = 15
cursorPosition = 4


'''
interpreter variables
'''

sentLine = ''

# program as list of strings, each string is a line
program = [None]
for i in range(500):
    program.append(None)

memory = list()
for i in range(32):
    memory.append(None)
pc = 0


'''
interpreter methods
'''

def readSent(sentLine):

    global program

    if (sentLine == ''): #if the sent line is blank just return
        return

    if (sentLine[0] in numbers): # if we are saving a line to the program

        i = 1
        # find line number
        for char in sentLine: #loop through characters until you find a non-number character and see how many characters that is then split the string at that index
            if (char not in numbers):
             break
            i += 1

        lineNumber = int(sentLine[:i]) # find the line we want to save to
        program[lineNumber] = sentLine[i:] # save the code to the index in program of the line number

    else:

        command = sentLine.split(' ') # split operation and operands for the command we want to execute

        if(command[0] == 'run'): # the run program command
            error = runProgram() #call runProgram and get the result
            println('exited with error ' + str(error)) # print to the console

        elif(command[0] == 'inspect'): # read code that has already been saved
            for i in range(int(command[1]),int(command[2])+1,1): # for each line between operand 1 and 2
                println(program[i]) # print that line of the program to the console

        elif(command[0] == 'clear'): # clears the console
            for i in range(25): # fill console with newlines
                newLine()




def execute(line):

    global memory
    global pc

    if (line == None): # if the line is None then do nothing
        return None

    else:

        instruction = line.split(' ') # split into tokens
        op = instruction[0] # opcode

        if(op == 'stop'):
            return 0
        elif(op == 'bug'):
            return 1
        elif(op == 'set'): # set memory at arg1 to arg2
            memory[int(instruction[1])] = instruction[2]
        elif(op == 'prtMem'):
            println(memory[int(instruction[1])])
        elif(op == 'print'):
            println(instruction[1])
        elif(op == 'jmp'):
            pc = instruction[1]
        elif(op == 'JmpIfZ'):
            if (memory[int(instruction[1])] == 0):
                pc = instruction[2]
        elif(op == 'add'):
            memory[int(instruction[3])] = int(memory[int(instruction[2])]) + int(memory[int(instruction[1])])
        elif(op == 'wait'):
            sleep(int(instruction[1]))

        return 1



def runProgram():

    global pc

    pc = 0 # reset program counter
    while True:
        if (pc >= len(program)): # if we finished the program, exit
            return 2

        error = execute(program[pc]) # execute the instruction
        if (error != None): # if the program return the error
            return error

        pc += 1 #increment the program counter




'''
terminal methods
'''

def labelAtTopLeft(label,x,y): # postion label independent of contents
    label.left = x
    label.top = y
    return label

currentLineLabel = labelAtTopLeft(currentLineLabel,15 ,380) # fix position of start text

# run when enter is pressed
def newLine():
    global lines
    global currentLine
    global cursorPosition
    lines.append(labelAtTopLeft(Label(currentLine,0,0,fill ='white',font = 'monospace'),15 ,380))
    for line in lines:
        line.centerY -= 15
        currentLine = ''
        cursorPosition = 0

def sendLine():
    global sentLine
    sentLine = currentLine

    # a few functions for the interpreter

def printChars(chars):
    global currentLine
    currentLine+=chars
    newLine()

def println(chars):
    global currentLine
    newLine()
    currentLine=chars



def onStep():

    #flashing cursor
    global cursor
    global cursorTimer

    #this code is haunted, do not touch
    cursorTimer += 0.5

    if ( cursorTimer % cursorInterval == 1): # flash cursor
        cursor.visible = False
    if( cursorTimer % cursorInterval == 10):
        cursor.visible = True

    cursor.left = cursorPosition * textWidth +12 # position based on characters typed




def onKeyPress(key):
    '''
    all the globals for the terminal
    '''
    global cursorPosition
    global currentLine
    global currentLineLabel
    global lines

    if (key in specialCharacters): # if the key pressed is a special character do something special
        #print(key+" sp")
        if(key == 'space'):
            currentLine += ' '
            cursorPosition += 1
        elif(key == 'backspace'):
            if (cursorPosition > 0):
                currentLine = currentLine[:-1]
                cursorPosition -= 1
        elif(key == 'tab'):
            currentLine += "\u0009"
            cursorPosition += 1
        elif(key == 'enter'):
            sendLine()

            readSent(sentLine)

            newLine()


    else:
        currentLine += key # if it's not special add to string and advance the cursor
        #print(key)
        cursorPosition += 1 # advance cursor


    currentLineLabel.value = currentLine #set the label value to string
    currentLineLabel = labelAtTopLeft(currentLineLabel,15 ,380)# fix the label position because cmu graphis is stupid
cmu_graphics.loop()
