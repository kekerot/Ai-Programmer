from .Databases.Interface.IDatabase import *
from .Databases.Concrete.BaseDatabase import *
import os

class GaRepository():
    _filepath = os.getcwd() + "\\"
    _items = []
    _database = IDatabase()
    def GARepository(self, filename):
        self._database = XmlDatabase(self._filepath + filename)
        LoadChanges()

#Irepository Members
    def GetAll(self):
        return enumerate(self._items)

    def Delete(self,GAParamsentity):
        index = FindIndexOfEntity(GAParamsentity)
        if (index != -1):
            self._items.RemoveAt(index)

    def Add(self,GAParamsentity):
        index = FindIndexOfEntity(GAParamsentity)
        if(index == -1):
            self._items.append(GAParamsentity)
        else:
            self._items.RemoveAt(index)
            self._items.insert(index, GAParamsentity)

    #Database Members
    def FindIndexOfEntity(ga):
        index = 0
        if (ga != null):
            for obj in self._items:
                if (obj.CrossoverRate == ga.CrossoverRate && obj.Elitism == ga.Elitism &&
                    obj.GenomeSize == ga.GenomeSize && obj.MutationRate == ga.MutationRate &&
                    obj.PopulationSize == ga.PopulationSize && obj.TargetFitness == ga.TargetFitness):
                        return index
                index++
        return -1   

    def LoadChanges():
        _items = _database.ReadEntities()
        

    def SaveChanges():
        _database.WriteEntities(_items)                


                




