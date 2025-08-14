import pandas as pd
import numpy as np

data = pd.read_csv('D:/MachineLearning/music prediction/raw_data.csv', index_col = 0,header = 0)
y = data["song_hotttnesss"]