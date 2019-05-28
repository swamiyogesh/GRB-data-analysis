import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  
from scipy import stats
import csv
import math
import numpy as np
# read flash.dat to a list of lists
datContent = [i.strip('|').split('|') for i in open("time.dat").readlines()]

# write it as a new CSV file
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(datContent)
def your_func(row):
    return row['Sentiments'] / row['Review']

data = pd.read_csv('output.csv')

t90 = pd.to_numeric(data['t90     '],errors='coerce')
t = t90.dropna()
tl = np.log(t)/np.log(10)

plt.hist(tl,bins=60)
plt.title('BATSE GRB EVENTS')
plt.xlabel('LOG(T90s)')

plt.show()
