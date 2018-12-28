import pandas as pd
from connection import engine_db



class LCTrader(object):
    def __init__(self):
        None
        self.loan_data = pd.read_sql_query('select * from lending_club.loans',con=engine_db)



print (LCTrader().loan_data)