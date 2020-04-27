import pandas as pd
filepath = 'C:/Users/User/Downloads/full_dataset-clean.tsv'
df = pd.read_csv(filepath, delimiter='\t')

df['date'] = df['date'].astype('datetime64[ns]')
df['date'] = [time.date() for time in df['date']]

# q = df.groupby('date').agg('count')
# q.to_csv('test1.csv')

df_1 = df.iloc[:270873]
df_2 = df.iloc[270873:]

import numpy as np
size = 10**5        # sample size
replace = False  # with replacement
fn = lambda obj: obj.loc[np.random.choice(obj.index, size, replace),:]
df_2 = df_2.groupby('date', as_index=False).apply(fn)

df = pd.concat([df_1, df_2])
df.to_csv('covid-tweets-jan-mar.csv.gz', index=False, compression='gzip')
# df.groupby('date').agg('count')
