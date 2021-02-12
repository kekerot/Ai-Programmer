#import AIProgrammer.Fitness.Base;
#import AIProgrammer.GeneticAlgorithm;
#Displays a string in the console.
class StringFitness(FitnessBase):#will inherit fitness base
    _targetString = str

    def StringFitness(self,GA, maxIterationCount, targetString):#base(ga, maxIterationCount)
        self._targetString = targetString;
        if (_targetFitness == 0):
            _targetFitness = len(self._targetString) * 256;

        #FitnessBase Members

    def GetFitnessMethod(self,program):
            #Run the source code.
            self.Output = self.RunProgram(program);

            #Order bonus.
            for i in range(0,len(self._targetString)):
                if (len(self._console) > i):
                    Fitness += 256 - abs(ord(self._console[i]) - ord(self._targetString[i]))

            self._fitness += Fitness

            #Check for solution.
            self.IsFitnessAchieved()

            self.Ticks = _bf.m_Ticks#_bf will be a instance object of th interpreter

            return self._fitness

    def GetConstructorParameters(self):
        return self._maxIterationCount + ", \"" + self._targetString + "\""

    def RunProgramMethod(self, program):
        try()
        #define run method
