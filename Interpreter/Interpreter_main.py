#import types
class Interpreter():
    functioncallobject = self.FunctionCallObj()
    m_CallStack = []
    m_InstructionSet = dict()
    m_Input = bytes() #will be bytes
    m_Memory = bytearray()
    m_Output = bytes() #ouput function
    m_Source = str #program code
    m_DataPointer = int #data pointer
    m_InstructionPointer = int #instruction pointer
    m_ExitLoop = bool #flag to indicate to skip loop and continue at next valid instruction
    m_ExitLoopInstructionPointer = int #hold inspointer for start of loop
    m_functions  = dict() #will be used to hold list offunction and their starting indexes
    m_NextFunctionCharacter = 'a' #part of bfectended 3 ,identifier for next function,inst. to call this function
    m_FunctionCallStack = []
    m_CurrentCallStack = [] #pointer to current call stack
    m_FunctionInputPointer = int 
    _functionSize = 300
    m_MaxIterationCount = int
    m_Storage = bytes
    m_Options = None
    m_ReturnValue = bytes()
    ################some members to be declared......
    #complete
    m_Ticks = int
    m_TotalTicks = int
    m_Stop = bool
    def m_CurrentDataPointer(self):
        return self.m_DataPointer
    def m_CurrentInstructionPointer(self):
        return self.m_InstructionPointer
    m_ExecutedFunctions = dict()
    #IsInsideFunction defined below
    def IsInsideLoop(self):
        return len(self.m_CurrentCallStack) > 0
    def m_CurrentFunction(self):
        if self.isinsidefunction():
            return self.m_FunctionCallStack[Instruction]
        else:
            return None
    



    def plus(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer]+1

    def minus(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer]-1
    
    def rarrow(self):
        if not self.m_ExitLoop:
            self.m_DataPointer+1

    def larrow(self):
        if not self.m_ExitLoop:
            self.m_DataPointer-1

    def dot(self):
        if not self.m_ExitLoop:
            self.m_Output(self.m_Memory[self.m_DataPointer])

    def comma(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = self.m_Memory[self.m_FunctionInputPointer]+1 if self.isinsidefunction() else self.m_Input

    def LSqBracket(self):
        if not self.m_ExitLoop and self.m_Memory[self.m_DataPointer] == 0:
            self.m_ExitLoop = True
            self.m_ExitLoopInstructionPointer = self.m_InstructionPointer
        self.m_CurrentCallStack.append(self.m_InstructionPointer)

    def RSqBracket(self):
        temp = self.m_CurrentCallStack.pop()
        if not self.m_ExitLoop:
            self.m_InstructionPointer = temp - 1 if self.m_Memory[self.m_DataPointer] != 0 else self.m_InstructionPointer
        else:
            if(temp == self.m_ExitLoopInstructionPointer):
                self.m_ExitLoop = False
                self.m_ExitLoopInstructionPointer = 0
    
    def zero(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 0

    def one(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 16

    def two(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 32

    def three(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 48

    def four(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 64

    def five(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 80

    def six(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 96

    def seven(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 112

    def eight(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 128

    def nine(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 144

    def A(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 160

    def B(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 176

    def C(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 192

    def D(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 208

    def E(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 224

    def F(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = 240

    def star(self):
        if not self.m_ExitLoop:
            self.m_ReturnValue = self.m_Memory[self.m_DataPointer]

    def at(self):
        if self.isinsidefunction():
            temp = self.m_FunctionCallStack.pop()
            self.m_DataPointer = temp.DataPointer

            self.m_CurrentCallStack = temp.CallStack
            #Restore exit loop status.
            self.m_ExitLoop = temp.ExitLoop
            # Restore exit loop instruction pointer.
            self.m_ExitLoopInstructionPointer = temp.ExitLoopInstructionPointer
            # Restore ticks.
            self.m_Ticks = temp.Ticks
            # Restore global storage.
            self.m_Storage = self.m_ReturnValue.Value if self.m_ReturnValue.HasValue else temp.Storage
            # Restore parent return value.
            self.m_ReturnValue = temp.ReturnValue
            # Restore max iteraction count.           self.m_MaxIterationCount = temp.MaxIterationCount;
            # Restore the instruction pointer.           self.m_InstructionPointer = temp.InstructionPointer;
            # Restore function input pointer.
            self.m_FunctionInputPointer = temp.FunctionInputPointer       
        else:
            self.m_stop = True

    def dollar(self):
        if not self.m_ExitLoop:
            #If we're inside a function, use the function's own global storage (separate from the main program).
                    # However, if this is the last storage command in the function code, then use the main/calling-function storage, to allow returning a value.
                    if (self.isinsidefunction() & self.m_Source[self.m_InstructionPointer + 1] == '@'):
                       #Set function return value.
                        self.m_ReturnValue = self.m_Memory[self.m_DataPointer]
                    else:
                        #Set global storage for this main program or function.
                        self.m_Storage = self.m_Memory[self.m_DataPointer]


    def excla(self):
        if not self.m_ExitLoop:
            self.m_Memory[self.m_DataPointer] = self.m_Storage




    def __init__(self, programCode, Input, output, functions, options):
        self.m_Source = programCode
        self.m_Input = Input
        self.m_Output = output
        if(options != None):
            self.m_Options = options
        self.m_CurrentCallStack = self.m_CallStack
        
        #basic bf
        #this implementaton needs furthur testing
        '''self.m_InstructionSet.append('+',lambda Mdp:Mdp++ if(!self.m_ExitLoop))
        self.m_InstructionSet.append('-',lambda memory[self.m_DataPointer]:11self.m_Memory[self.m_DataPointer]-- if(!m_ExitLoop))
        self.m_InstructionSet.append('>',lambda self.m_DataPointer:self.m_DataPointer++ if(!m_ExitLoop))
        self.m_InstructionSet.append('<',lambda self.m_DataPointer:self.m_DataPointer-- if(!m_ExitLoop))
        self.m_InstructionSet.append('.',lambda self.m_Output(self.m_Memory[this.DataPointer]):self.m_Output(self.m_Memory[this.DataPointer]) if(!m_ExitLoop))'''
        #lambda func doesnt work as it can only execute one expression
        #maybe try everything in one if !exitloop
        #different approach put every instruction in a dict and at the value the action
        #and then use the keys to append to instruction set
        
        '''self.m_InstructionSet['+'] =  

        if not m_ExitLoop:
            self.m_InstructionSet['-'] = self.m_Memory[self.m_DataPointer]-1
            
        if not m_ExitLoop:
            self.m_InstructionSet['>'] = self.m_Memory[self.m_DataPointer]+1
        if not m_ExitLoop:
            self.m_InstructionSet['<'] = self.m_Memory[self.m_DataPointer]-1
        if not m_ExitLoop:'''    

        
        self.m_InstructionSet['+'] = self.plus
        self.m_InstructionSet['-'] = self.minus
        self.m_InstructionSet['>'] = self.rarrow
        self.m_InstructionSet['<'] = self.larrow
        self.m_InstructionSet['.'] = self.dot
        self.m_InstructionSet[','] = self.comma
        self.m_InstructionSet['['] = self.LSqBracket
        self.m_InstructionSet[']'] = self.RSqBracket
        self.m_InstructionSet['1'] = self.one
        self.m_InstructionSet['2'] = self.two
        self.m_InstructionSet['3'] = self.three
        self.m_InstructionSet['4'] = self.four
        self.m_InstructionSet['5'] = self.five
        self.m_InstructionSet['6'] = self.six
        self.m_InstructionSet['7'] = self.seven
        self.m_InstructionSet['8'] = self.eight
        self.m_InstructionSet['9'] = self.nine
        self.m_InstructionSet['A'] = self.A
        self.m_InstructionSet['B'] = self.B
        self.m_InstructionSet['C'] = self.C
        self.m_InstructionSet['D'] = self.D
        self.m_InstructionSet['E'] = self.E
        self.m_InstructionSet['F'] = self.F
        self.m_InstructionSet['*'] = self.star
        self.m_InstructionSet['@'] = self.at
        self.m_InstructionSet['$'] = self.dollar
        self.m_InstructionSet['!'] = self.excla

        self.ScanFunctions(programCode)
        inst = 'a'
        for inst in range(ord(inst),ord(m_NextFunctionCharacter)+1):
            instruction = inst
            self.m_InstructionSet[chr(instruction)] = self.funcinstructionset 


    def funcinstructionset(self,instruction,functions):
        if not self.m_ExitLoop:
            if not self.isinsidefunction():
                if self.m_ExecutedFunctions.keys(chr(instruction)):
                    self.m_ExecutedFunctions[instruction]+1
                else:
                    self.m_ExecutedFunctions[chr(instruction)] = 1

            if (functions != None):
                functions(chr(instruction))

            functionCallObj = FunctionCallObj
            functionCallObj.DataPointer = self.m_DataPointer
            functionCallObj.InstructionPointer = self.m_InstructionPointer 
            functionCallObj.FunctionInputPointer = self.m_FunctionInputPointer
            functionCallObj.CallStack = self.m_CurrentCallStack,
            functionCallObj.ExitLoop = self.m_ExitLoop,
            functionCallObj.ExitLoopInstructionPointer = this.m_ExitLoopInstructionPointer,
            functionCallObj.Ticks = self.m_Ticks, 
            functionCallObj.Instruction = instruction, 
            functionCallObj.Storage = self.m_Storage, 
            functionCallObj.ReturnValue = self.m_ReturnValue,
            functionCallObj.MaxIterationCount = self.m_MaxIterationCount

            self.m_CurrentCallStack = []
            self.m_ExitLoop = False
            self.m_ExitLoopInstructionPointer = 0

            #intialize func global storage
            self.m_Storage = 0
            self.m_ReturnValue = None

            functionOptions = m_Functions[chr(instruction)] #loaded into functioninstance may need furthur looking


            #Set the function input pointer to the parent's starting memory. 
            # Calls for input (,) from within the function will read from parent's memory, each call advances the parent memory cell that gets read from. 
            # This allows passing multiple values to a function.
            #Note, if we set the starting m_FunctionInputPointer to 0, 
            # functions will read from the first input position (0).
            #If we set it to m_DataPointer, functions will read input from the current position in the parent memory (n). 
            # This is trickier for the GA to figure out, because it may have to downshift the memory back to 0 before calling the function so that the function gets all input. Setting this to 0 makes it easier for the function to get the input.

            self.m_FunctionInputPointer = 0 if functionOptions.ReadInputAtMemoryStart else self.m_DataPointer
            self.m_DataPointer - self._functionSize * (ord(instruction) - 96)

            #clear memory
            self.m_Memory, self.m_DataPointer, self._functionSize = [],[],[]
            self.m_Ticks = 0
            #set maxiter for this func,if specified
            self.m_MaxIterationCount = functionOptions.MaxIterationCount if functionOptions.MaxIterationCount else self.m_MaxIterationCount
            # Set the instruction pointer to the beginning of the function.
            self.m_InstructionPointer = functionOptions.InstructionPointer

            #Runnnig the program
    
    def Run(self, maxInstructions = 0):
        self.m_Ticks = 0
        self.m_TotalTicks = 0
        self.m_Stop = False

        if (maxInstructions > 0):
            self.RunLimited(maxInstructions)
        else:
            self.RunUnlimited()
    
    def RunLimited(self, maxInstructions):
        self.m_MaxIterationCount = maxInstructions

        #Iterate through the whole program source
        while (self.m_InstructionPointer < len(self.m_Source) and not self.m_Stop):
            #Fetch the next instruction
            instruction = self.m_Source[self.m_InstructionPointer]

            #See if that IS an instruction and execute it if so
            #Action 
            if (self.m_InstructionSet.get(instruction)):
                #Yes, it was - execute
                action = self.m_InstructionSet[instruction]
                action()
            #Next instruction
            self.m_InstructionPointer+1

            #Have we exceeded the max instruction count?
            if (self.m_MaxIterationCount > 0 & self.m_Ticks >= self.m_MaxIterationCount):
                    if (self.isinsidefunction):
                        #We're inside a function, but ran out of instructions. Exit the function, but continue.
                        if (self.m_InstructionSet.get('@')):
                            action = self.m_InstructionSet['@']
                            action()
                            self.m_InstructionPointer+1
                    else:
                        break

            self.m_Ticks+1
            self.m_TotalTicks+1

    def RunUnlimited(self):
        #Iterate through the whole program source
        while (self.m_InstructionPointer < len(self.m_Source) and not self.m_Stop):
            #Fetch the next instruction
            instruction = self.m_Source[self.m_InstructionPointer]

            #See if that IS an instruction and execute it if so
            #Action action
            if (self.m_InstructionSet.get(instruction)):
                #Yes, it was - execute
                action = self.m_InstructionSet[chr(instruction)]
                action()

            #Next instruction
            self.m_InstructionPointer+1

            self.m_Ticks+1
            self.m_TotalTicks+1
    def ScanFunctions(self, source):
        self.m_InstructionPointer = source.index('@')
        while (self.m_InstructionPointer > -1 and self.m_InstructionPointer < len(source) - 1 and not self.m_Stop):
            #Retrieve any settings for this function.
            functionDetail = self.m_Options != None and self.m_Options[len(m_Functions)] if len(self.m_Options) > len(self.m_Functions) else None

            #Store the function.
            ##!!!!!!!!!1 this adding of function requires look into function instance also!!!!!!!!!
            self.m_Functions.append(m_NextFunctionCharacter++(self.m_InstructionPointer, functionDetail))

            self.m_InstructionPointer = source[self.m_InstructionPointer + 1:].index('@')

        self.m_InstructionPointer = 0




    def isinsidefunction(self):
        return len(self.m_CurrentCallStack)>0

    def NotExitLoop(self):
        return self.m_ExitLoop == True 

class FunctionCallObj:
    InstructionPointer = int
    DataPointer = int
    FunctionInputPointer = int
    CallStack = []
    ExitLoop = bool
    ExitLoopInstructionPointer = int
    Ticks = int
    Instruction = str
    Storage = bytes
    ReturnValue = bytes
    MaxIterationCount = int





