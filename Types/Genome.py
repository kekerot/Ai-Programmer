import numpy as np
import copy
import random 
class Genome:
    #only mutation rate is static so its valus would be changes using class
    m_mutationRate=0
    #constructor for various functions
    def __init__(self,length,createGenes=True,genes=[]):
        if len(genes)==0:
            self.age=0
            self.m_fitness=0

            self.m_length=length
            self.m_genes=np.empty(length,dtype=float)
            if createGenes==True:
                self.CreateGenes()
        else:
             self.age=0
            self.m_fitness=0
            self.m_genes = genes
            self.m_length=len(self.m_genes)
    
    def DeepCopy(self):
        g=Genome(self.m_length,False)
        g.m_genes=copy.deepcopy(self.m_genes)
        return g
        
    def CreateGenes(self):
        for i in range(self.m_length):
            self.m_genes[i]=random.random()
    
    
    #creates two children with random and parent genes combined 
    def CrossOver(self,genome2):
        pos=int(random.random()*self.m_length)
        child1=Genome(self.m_length,False)
        child2 = Genome(self.m_length,False)

        for i in range(self.m_length):
            if i<pos:
                child1.m_genes[i]=self.m_genes[i]
                child2.m_genes[i]=genome2.m_genes[i]
            else:
                child2.m_genes[i]=self.m_genes[i]
                child1.m_genes[i]=genome2.m_genes[i]
        return child1, child2

    #Function to mutate the genomes by inserting/shifting/deleting or replacing some bits    
    def Mutate(self):
        for pos in range(self.m_length):
            if random.random()<self.m_mutationRate:
                r=random.random()
                if r<0.25:
                    #insertation mutation
                    mutationIndex=pos
                    shiftbit=self.m_genes[mutationIndex]
                    self.m_genes[mutationIndex]=random.random()
                    
                    if random.random()>0.5:
                        #deleting one element from last
                        for i in range(mutationIndex+1,self.m_length):
                            nextshiftbit=self.m_genes[i]
                            self.m_genes[i]=shiftbit
                            shiftbit=nextshiftbit
                    else:
                        #deleting element from start
                        for i in range(mutationIndex-1,-1,-1):
                            nextshiftbit=self.m_genes[i]
                            self.m_genes[i]=shiftbit
                            shiftbit=nextshiftbit
                elif r<=0.5:
                    #deleting muttion
                    mutationIndex = pos
                    if random.random()>0.5:
                        for i in range(mutationIndex,0,-1):
                            self.m_genes[i]=self.m_genes[i-1]
                        self.m_genes[0]=random.random()
                    else:
                        for i in range(mutationIndex,self.m_length):
                            self.m_genes[i]=self.m_genes[i+1]
                        self.m_genes[self.m_length-1]=random.random()
                elif r<=0.75:
                    #shift mutation
                    if random.random()>0.5:
                        shiftbit=self.m_genes[0]
                        for i in range(self.m_length):
                            if i>0:
                                temp=self.m_genes[i]
                                self.m_genes[i]=shiftbit
                                shiftbit=temp
                            else:
                                self.m_genes[i]=self.m_genes[self.m_length-1]
                    else:
                        shiftbit = self.m_genes[self.m_length-1]
                        for i in range(self.m_length-1,-1,-1):
                            if i<self.m_length-1:
                                temp=self.m_genes[i]
                                self.m_genes[i]=shiftbit
                                shiftbit=temp
                            else:
                                self.m_genes[i]=self.m_genes[0]
                else:
                    #replacement mutation
                    self.m_genes[pos]=random.random()

    def Expand(self,size):
        originalSize=len(self.m_genes)
        difference=size-originalSize
        newGenes=np.empty(size)
        if difference>0:
            if random.random()<0.5:
                #extend from front
                for i in range(0,difference):
                    newGenes[i]=random.random()
                for i in range(difference,size):
                    newGenes[i]=self.m_genes[i]
            else:
                #extend from end
                for i in range(0,originalSize):
                    newGenes[i]=self.m_genes[i]
                for i in range(originalSize,size):
                    newGenes[i]=random.random()
            self.m_genes=newGenes
        else:
            for i in range(size):
                newGenes[i]=self.m_genes[i]
            self.m_genes=newGenes
        self.m_length=size
        
    def Genes(self):
        return self.m_genes

    def Output(self):
        #will be defined later 
        #this function displays the value in m_genes 
        pass
    
    def GetValues(self,values):
        for i in range(self.m_length):
            values[i]=self.m_genes[i]

    
    def SetFitness(self,value):
        self.m_fitness=value
    
    def GetFitness(self):
        return self.m_fitness
    
    def GetLength(self):
        return self.m_length
    
        
                

                        



