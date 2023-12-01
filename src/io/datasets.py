from config import *

import pandas as pd

def get_BWSAS():
    df = pd.read_csv(DATASET_BWSAS_FILE_ABS_PATH)
    df.rename(columns=lambda x: x.replace(' ', '_'), inplace=True) # Replace spaces with underscores in column names
    df = df.convert_dtypes()
    df.Measurement_Timestamp = pd.to_datetime(df.Measurement_Timestamp)
    df.dtypes
    
    return df
