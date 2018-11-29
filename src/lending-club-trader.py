import pandas as pd


df = pd.read_csv('../dev-docker/SQL/loans_2.csv')
df.drop(df.columns[[0,1]], axis=1,inplace=True)
print (df.to_csv('../dev-docker/SQL/loans_clean.csv',index=False))