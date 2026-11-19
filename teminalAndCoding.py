from cmu_graphics import *
app.background = 'black'

# a few constants for the terminal
textSize = 12
textWidth= 7.23
font = 'monospace'

# list of characters that when type don't return their chacrater
specialCharacters = ('enter','tab','escape','backspace','space','up','down','left','right')
# a list of the numbers as strings
numbers = ('0','1','2','3','4','5','6','7','8','9')
'''
line varibles
'''
lines = list()
currentLine= ''
currentLineLabel = Label(currentLine,0,0,fill = 'white',size = textSize, font = font)


'''
cursor variables
'''
cursor = Rect(15,378,5,textSize, fill = 'white')
cursorTimer = 0
cursorInterval = 15
cursorPosition = 0


'''
interpreter variables
'''

sentLine = ''

# program as list of strings, each string is a line
program = [None]
for i in range(500):
    program.append(None)
    
#init memory
memorySize = 32
memory = list()

for i in range(memorySize):
    memory.append(0)
    
# the program counter
pc = 0
# max steps before infinte loop is assumed
maxSteps = 30000

waitingForInput = False
userInput = None

'''
interpreter methods
'''

def readSent(sentLine):
    
    global program
    global waitingForInput
    global userInput
    global pc
    
    if (sentLine == ''): #if the sent line is blank just return
        return
    if (waitingForInput):
        userInput = sentLine
        pc -= 1
        error = runProgram()
        println('Enter a Value')
        
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
            pc = 0
            error = runProgram() #call runProgram and get the result
            println('exited with error ' + str(error)) # print to the console
            print(waitingForInput)
            return
            
        elif(command[0] == 'inspect'): # read code that has already been saved
            println('')
            for i in range(int(command[1]),int(command[2])+1,1): # for each line between operand 1 and 2
                if (program[i] != None):
                    println(str(i) + ' - ' + program[i]) # print that line of the program to the console
                elif (program[i + 1] != None):
                    println('~~~')
            println('~~~')
                
                
        elif(command[0] == 'clear'): # clears the console
            for i in range(25): # fill console with newlines
                newLine()
                
        elif(command[0] == 'clearPRG'): # clear the program
            for j in range(len(program)):
                program[j] = None
                
        elif(command[0] == 'help'):
            println('Error Codes :')
            
            println('')
            
            println('0 - Succesful Execution')
            println('1 - Raised Error')
            println('2 - End of Program')
            println("3 - Program Didn't Stop")
            println('4 - waiting for user input')
            
            println('')
            
            println('Commands :')
            
            println('')
            
            println('stop - Halts Execution')
            println('set a b - Sets the Value at a to b')
            println('ask a  - Sets the Value at 0 to whatever the use types')
            
        else:
            println("Unrecognized Command  -  Try 'help'")
            
            
                
        
        
        

def execute(line):
    global userInput
    global memory
    global pc
    global waitingForInput
    
    if (line == None): # if the line is None then do nothing
        return None

    else:
        
        instruction = line.split(' ') # split into tokens
        op = instruction[0] # opcode
        
        if(op == 'stop'): # stop the program
            return 0
        elif(op == 'raise'): # triggers an error
            return 1
        elif(op == 'set'): # set memory at arg1 to arg2
            memory[int(instruction[1])] = instruction[2]
        elif(op == 'prtMem'): # print the value at a memory address
            println(memory[int(instruction[1])])
        elif(op == 'print'):
            println(instruction[1])
        elif(op == 'jmp'):# jump to line
            pc = int(instruction[1])
        elif(op == 'jnz'):# jump if not Zero
            if (memory[int(instruction[1])] != 0):
                pc = int(instruction[2]) - 1
        elif(op == 'jiz'):# jump if Zero
            if (memory[int(instruction[1])] == 0):
                pc = int(instruction[2]) -1
        elif(op == 'add'): # add the values of 2 addresses and put it in a spot in memory
            memory[int(instruction[3])] = int(memory[int(instruction[2])]) + int(memory[int(instruction[1])])
        elif(op == 'sub'):# subtract the values of 2 addresses and put it in a spot in memory
            memory[int(instruction[3])] = int(memory[int(instruction[2])]) - int(memory[int(instruction[1])])
        elif(op == 'wait'): # wait for a set amount of time
            sleep(int(instruction[1]))
        elif(op == 'ask'):
            if (userInput == None):
                println(str(instruction[1]))
                waitingForInput = True
                return 4
            else:
                
                memory[0] = userInput
                userInput = None
                waitingForInput = False
                
        else:
            return 1
        
    

def runProgram():
    
    global pc
    
    #pc = 0 # reset program counter / relocated
    count = 0
    while True:
        if (pc >= len(program)): # if we finished the program, exit with a 'end of program' error
            return 2
        if (count > maxSteps): # id the program doesn't stop after a certain number of ticks (infinte loop) exit with a "didn't stop" error
            return 3
        
        error = execute(program[pc]) # execute the instruction
        
        if (error != None): # if the program return the error
            return error
        count += 1
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
    
    cursor.left = cursorPosition * textWidth + 11.4 # position based on characters typed
    
    
    
    
def onKeyPress(key):
    '''
    all the globals for the terminal
    '''
    global cursorPosition
    global currentLine
    global currentLineLabel
    global lines
    
    if (key in specialCharacters): # if  the key pressed is a special character do something special
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
    
    
    
    
    
   
