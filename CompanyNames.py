import pymongo as db
from pymongo import MongoClient
import pandas as pd #Python library that provides highly optimized performance
client = MongoClient()
db = client.NSE_Database
collection1 = db.CompanyNames
df = pd.read_csv("sec_bhavdata_full.csv", usecols = [0, 1]) #pandas usecols when you want to load specific columns into dataframe.
records_ = df.to_dict(orient = 'records') #Convert DataFrame to dictionary.
result = db.CompanyNames.insert_many(records_)

