import pymongo
from datetime import datetime
from bson.int64 import Int64
from bson.decimal128 import Decimal128
from decimal import Decimal

if __name__: "__main__":
    
    #open connection to MongoDB
    conn = pymongo.MongoClient("localhost", 27017)

    # first document that we intend to insert in ruralSavingsTest.customerAccounts collection
    document1 = {
        "customerNumber": "RSCN01",
        "customerFirstName": "Luka",
        "customerLastName": "Doncic",
        "age": 26,
        "address": {
            "city": "Los Angeles",
            "country": "USA"
        },
        "accounts": [
            {
                "accountNumber": "RSAN01",
                "cardNumber": "123456781234077",
                "creditLimit": 10000000,
                "branch": "Katipunan"
            }
        ]
    }

    # first document that we intend to insert in ruralSavingsTest.transactions colleciont

    document2 = {
        "transactionNumber": "RSCNTXN00001",
        "customerNumber": "RSCN01",
        "accountNumber": "RSAN01",
        "type": "debit",
        "amount": 250,
        "vendor": "Potato Corner",
        "transactionDate": datetime(2025,8,31)
    }



    conn.close()