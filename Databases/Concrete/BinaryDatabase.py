from Concrete import BaseDatabase
import os
from interface import implements
import pickle

class BinaryDatabase(implements(BaseDatabase)):
    
    #IDB members
    def BinaryDatabase(self,filepath):
        self.filepath = filepath    
    def WriteFile(self):
        with open (self.filepath , 'wb') as f:
            pickle.dump(self.filepath,f)

    def ReadFile(self):
        entities = []
        if(os.path.exists(self.filepath)):
            with open(self.filepath , 'rb') as f:
                entities = pickle.load(f) 
        return entities               








