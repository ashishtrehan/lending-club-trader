import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from connection import engine_db



class LCTrader(object):
    def __init__(self):
        self.loan_data = pd.read_sql_query('select * from lending_club.loans',con=engine_db)

        #top employ
        self.employment = self.loan_data['emp_title'].value_counts().head()

        self.employment_length = self.loan_data['emp_length'].value_counts().head()





print (LCTrader().employment_length)