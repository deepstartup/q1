import pandas as pd
import multiprocessing as mp
from threading import Thread
import os
import json

configJson=json.load(CONFIG_FILE_PATH)
targetJson=json.load(TGT_FILE_PATH)
LARGE_FILE = configJson.LARGE_FILE_PATH
CHUNKSIZE = configJson.CHUNKSIZE

class kernel():
    def __init__(self,df):
        self.df=df
    def process_frame(self,df):
        reader = pd.read_table(LARGE_FILE, chunksize=CHUNKSIZE)
        pool = mp.Pool(configJson.pool_size)
        funclist = []
        for df in reader:
        # process each data frame
            if configJson.poolingtype='async':
                f = pool.apply_async(process_frame,[df])
                if configJson.multithreading:
                    
                    t1 = Thread(target = f) 
                    t2 = Thread(target = f) 
                    t1.start() 
                    t2.start() 
                    t1.join() 
                    t2.join() 
                    t1.end()
                    t2.end()
                    funclist.append(f)
            else:
                f = pool.apply(process_frame,[df])
                funclist.append(f)
        result = 0
        for datak in funclist:
            load_dataframe(datak)
            result += datak.get(timeout=configJson.timeout)
        pass
    def load_dataframe(self,df):
        pass
    
if __name__ == '__main__':
     kernel=kernel(LARGE_FILE)