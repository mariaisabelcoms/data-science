import pandas as pd

df = pd.read_csv("/workspaces/data-science/top10s.csv", encoding='ISO-8859-1')

dfs = pd.read_csv('/workspaces/data-science/SpotifyTopSongsByCountry - May 2020.csv', encoding='ISO-8859-1')

# cabeca1 = df.head()

# print(cabeca1)

# cabeca2 = dfs.head()

# print(cabeca2)

# rabo = df.tail(10)

# print(rabo)

# print(df.info)

# print(df.dtypes)

# print(df.select_dtypes(include='object'))

# print(df.describe)

# print(df.isna().sum())

# print(df['artist'].unique())

# print(df['artist'].nunique())

# print(df.shape)

# print(df.size)

# print(df.columns)

# print(df.nsmallest(3, 'bpm'))

# print(df.nlargest(3, 'bpm'))

df_ops=df.drop_duplicates(subset=['title'], keep='last')

# print(df_ops)

# print(df.query("artist == 'Ariana Grande'"))

# print(df.query('dur > 200'))

df_ops.drop(columns=['spch'], inplace=True)

print(df.groupby('artist').count())









