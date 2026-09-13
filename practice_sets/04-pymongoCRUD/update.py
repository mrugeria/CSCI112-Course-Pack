import pymongo
from datetime import datetime
from bson.int64 import Int64
from bson.decimal128 import Decimal128
from decimal import Decimal

if __name__ == "__main__":

    conn = pymongo.MongoClient('localhost', 27017) #connect to MongoDB
    db = conn["ruralSavingsPrime"] #use ruralSavingsPrime

    # create the query and store it in the query1 variable
    query1 = {
        "transactionDate": { '$gte': datetime(2019,1,1) },
        "transactionDate": { '$lt': datetime(2020,1,1) }
    }

    # create the update commands and store them in the updates1 variable
    updates1 = {
        '$set': { 'fraudTransactions': True }, # Notice that the value True starts with a capital letter as compared to the value true in mongoDB which starts with a lowercase letter
        '$rename': { 'vendor': 'fraudVendor' }
    }
    
    # execute the update
    db['transactions'].update_one(query1, updates1) # We are only passing 2 parameters since we don't want to specify any options

    # execute update_many instead of update_one
    db['transactions'].update_many(query1, updates1)

    conn.close()