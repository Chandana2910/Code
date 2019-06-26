import pymongo as db
from pymongo import MongoClient
import pandas as pd
import glob
client = MongoClient()
db = client.NSE_Database
collection2 = db.SpecificCols
extension ="csv"
all_filenames = [i for i in glob.glob('*.{}'.format(extension))] #The glob module finds all the pathnames matching a specified pattern
df = pd.concat([pd.read_csv(f) for f in all_filenames ])
df_temp = df.iloc[:, 2 : 14] #to select specific columns
records_ = df_temp.to_dict(orient = 'records')
result = db.SpecificCols.insert_many(records_)
