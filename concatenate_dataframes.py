import numpy as np
import pickle
import pandas as pd
import glob

DATA_DIR = 'data/twitter_data_clean_*'
files = (glob.glob(DATA_DIR))
frames = []

for _file in files:
    print(_file)
    df = pickle.load( open( _file, "rb" ) )
    frames.append(df)

clean_data = pd.concat(frames)
pickle.dump(clean_data, open("data/twitter_data_clean.p", "wb" ) )

# number of tweets per canton in Switzerland
#clean_data[clean_data.country=="ch"].state.value_counts()




