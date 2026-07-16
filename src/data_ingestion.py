import pandas as pd
import numpy as np
import os

try:
    df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')
except Exception as e :
    print(e.getMessage())
    
df = df.iloc[:, 3:]

df = df[df['Length of Membership'] > 1]

df.drop(columns=['Avg. Session Length'],inplace=True)
df.to_csv(os.path.join('data','customer.csv'))
# print(df)