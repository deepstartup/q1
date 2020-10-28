import json
import filewatcher
import Pkernel
import subprocess
import multiprocessing as mp
import pandas as pd
import dbwatcher
configJson=json.load(CONFIG_FILE_PATH)
class main():
    def __init__(self):
        pass
    def dfsplit(self):
        rule=rules()
        if configJson.filesplit and configJson.parallelprocess:
            """rule based file split and demon creation fro config"""
            os.fork()
            for i in range(configJson.subprocess):
                if filebased:
                    pool = mp.Pool()
                    df=pd.dataFrame(pool.map(filecount, [row for row in filedata]))
                subprocess.Popen(demons,Pkernel.kernel(df))

    def filewatcher(self):
        dfsplit(self)
        pass
    def dbwatcher(self):
        dfsplit(self)
        pass    
if __name__ == '__main__':
     if configJson.parallel:
         subprocess.Popen("python filewatcher.py & python dbwatcher.py", shell=True)
     elif configJson.filewatcher:
         main.filewatcher()
     elif configJson.dbwatcher:
         main.dbwatcher()
