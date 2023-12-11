import pandas as pd
import numpy as np
import datetime as dt
from sodapy import Socrata

def load_data_from_API(source,key,limit):
    try:
        
        client = Socrata(source, None)

        results = client.get(key, limit = int(limit))

        data = pd.DataFrame.from_records(results)
        
        return data
    
    except Exception as err:
        
        print(f"Unexpected {err=}, {type(err)=}")
        raise


def link_to_data(link):
    try:
        
        data = pd.read_csv(link)
        
        return data
    
    except Exception as err:
        
        print(f"Unexpected {err=}, {type(err)=}")
        raise



def make_numeric(data,column):
    try:
        data[column] = pd.to_numeric(data[column])
        return data
    
    except ValueError:
        print('The data in this column is not numeric')
    
    except Exception as err:
        
        print(f"Unexpected {err=}, {type(err)=}")
        raise
    

def convert_to_datetime(data,column):
    try:
        data[column] = pd.to_datetime(data[column])
        return data
        
    except ValueError:
        print('The data in this column is not numeric')    
    
    except Exception as err:
        
        print(f"Unexpected {err=}, {type(err)=}")
        raise    