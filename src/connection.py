from sqlalchemy import create_engine
import json
import pandas as pd
import psycopg2


with open('config.json') as f:
    conf = json.load(f)

conn_str = "host={} dbname={} user={} password={}".format(conf.get('host'), conf.get('database'), conf.get('user'), conf.get('passw'))
conn = psycopg2.connect(conn_str)
#
#
# df = pd.read_sql_query('select * from lending_club.loands limit 10',con=engine)
#
# print (df)
print (conn_str)