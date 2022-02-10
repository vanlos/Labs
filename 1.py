import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/Yorko/mlcourse.ai/master/data/cars.csv"
pd.set_option('display.max_rows', 428)
data = pd.read_csv(url, delimiter=';')
data
data.head()
data.sample(3)
