#ppr.py: Preprocessing Calulations Based on Config.json/Config.yml and validation on configuration
import os
import json

configJson=json.load(CONFIG_FILE_PATH)

class pprcalc():
    def __init__(self):
        self.mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
        self.mem_gib = mem_bytes/(1024.**3)

class filesize(pprcalc):
    def __init__(self,filesizeval):
        self.filesizeval=filesizeval
    def validation(self):
        """
        Memory validation on file size and if works fine would return to kernel package
        """
        pass
    def fileoperation(self):
        """
        Read the config JSON to identify file split TRUE/FALSE, 
        if True then calculate number of splits,size of each split file and 
        number of parallel processes 
        """
        setFileProcess=True
        setSplitSize=round(self.fileoperation/os.cpu_count())
        setParallelProcess=os.cpu_count()+1
        pass
class chunksize(pprcalc):
    def __init__(self,dbrows):
        self.dbrows=dbrows
    def clcchunk(self):
        pass