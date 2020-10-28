"""Pcustom is the child module for custom 
   If any custom logic needs to be written
"""
from Pcluster import cluster
import json
configJson=json.load(CONFIG_FILE_PATH)
class custom(cluster):
    def __init__(self,df):
        self.df=df
    def process_frame(self,df):
        if not configJson.custom:
            return super().process_frame()
        else:
            """custom logic for ETL/ELT"""
            pass