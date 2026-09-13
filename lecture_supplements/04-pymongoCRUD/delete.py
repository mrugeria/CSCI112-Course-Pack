import pymongo
from datetime import datetime
from bson.int64 import Int64
from bson.decimal128 import Decimal128
from decimal import Decimal

if __name__: "__main__":

    conn = pymongo.MongoClient("localhost", 27017) #connect to MongoDB
    db = conn["ruralSavingsPrime"] #use ruralSavingsPrime

    # Let's declare our query
    query1 = {
        'fraudTransactions': True
    }

    # You may also use different variations of this query, as long as the logic is correct
    query2 = {
        'fraudVendor': { '$exists': True }
    }

    # Or use the same query for updating the records, this will also work
    query3 = {
        "transactionDate": { '$gte': datetime(2019,1,1) },
        "transactionDate": { '$lt': datetime(2020,1,1) }
    }

    # run the delete function after this comment

    conn.close()