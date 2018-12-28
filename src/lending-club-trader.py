import pandas as pd
from connection import engine_db
import requests

#
# df = pd.read_csv('../dev-docker/SQL/loans_2.csv')
# df.drop(df.columns[[0,1]], axis=1,inplace=True)
# print (df.to_csv('../dev-docker/SQL/loans_clean.csv',index=False))

df = pd.read_sql_query('select * from lending_club.loans',con=engine_db)

print (df.head(5))