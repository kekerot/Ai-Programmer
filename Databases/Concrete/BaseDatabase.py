from Interface import  IDatabase
from pathlib import Path
import os
from abc import abstractmethod
from interface import implements

class BaseDatabase(implements(IDatabase)):
    _filePath = ""

    def BaseDatabase(self,filepath):
        self._filePath = filepath
        FPath = self._filePath
        #get directory of Fpath 
        Lastslashindex = FPath.rfind("\\")
        directory = FPath[0,Lastslashindex]
        #create preference director if it doesnt exist
        fp = Path(directory)
        if(fp.is_dir()): pass
        else: os.mkdir(directory)


#Idatabase members
def WriteEntities():
    pass
def ReadEntities():
    pass           










