import pymongo as db
from pymongo import MongoClient
import pandas as pd
import glob
client = MongoClient()
db = client.NSE_Database
collection_name = db.MultipleNSE_Data
extension ="csv"
all_filenames = [i for i in glob.glob('*.{}'.format(extension))] #The glob module finds all the pathnames matching a specified pattern
df = pd.concat([pd.read_csv(f) for f in all_filenames ])
records_ = df.to_dict(orient = 'records')
result = db.MultipleNSE_Data.insert_many(records_)

