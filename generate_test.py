import pandas as pd
import numpy as np

rows = 50_000_000
labels = ['A','B','C']

labels = np.random.choice(
    labels,
    size = rows,
)

data = np.random.normal(
    size=rows
)

df = pd.DataFrame(
    {
        'label' : labels,
        'data' : data,
    }
)

filename = './big_file_test.csv'
df.to_csv(filename,index=False)
