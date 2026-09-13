import pymongo
from datetime import datetime
from bson.int64 import Int64
from bson.decimal128 import Decimal128
from decimal import Decimal

if __name__ == "__main__":
    
    conn = pymongo.MongoClient("localhost", 27017) #connect to MongoDB
    db = conn["ruralSavingsPrime"] #use ruralSavingsPrime

    #create the query
    query1 = {
        "age": { "$gt": 30 }, # Notice how the $gt operator is also enclosed in quotes unlike in mongosh
        "address.city": { "$in": ["Pasig", "Taguig"] } # Same here. This is because we are creating a python dictionary.
    }

    #find_one
    results1 = db["customerAccounts"].find_one(query1) # The find_one function accepts a dictionary as its parameter

    #results1 now contains result of our query. We can use this variable to output the single result.
    # print(results1)

    #find_many
    results2 = db["customerAccounts"].find(query1)
    print(results2)

    #print cursor object contents
    for result in results2:
        print(result)

    conn.close()