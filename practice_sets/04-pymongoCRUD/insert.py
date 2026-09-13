import pymongo
from datetime import datetime
from bson.int64 import Int64
from bson.decimal128 import Decimal128
from decimal import Decimal

if __name__ == "__main__":
    #insert_one() tutorial
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

    #use the database first
    db = conn["ruralSavingsTest"] #use ruralSavingsTest in mongosh

    # output1 = db["customerAccounts"].insert_one(document1) #insert document1 to ruralSavingsTest.customerAccounts
    # output2 = db["transactions"].insert_one(document2) #insert document2 to ruralSavingsTest.transactions

    # print(output1)
    # print(output2)

    #insert_many() tutorial

    # customerAccountsDocuments variable contains more than 1 document (list of dictionaries in python)
    customerAccountsDocuments = [
        {
            "customerNumber": "RSCN02",
            "customerFirstName": "Jimmy",
            "customerLastName": "Alapag",
            "age": 49,
            "address": {
                "city": "Sacramento",
                "country": "USA"
            },
            "accounts": [
                {
                    "accountNumber": "RSAN02",
                    "cardNumber": "123456781234099",
                    "creditLimit": 10000000,
                    "branch": "Katipunan"
                },
                {
                    "accountNumber": "RSAN03",
                    "cardNumber": "123456781234088",
                    "creditLimit": 10000000,
                    "branch": "BGC"
                }
            ]
        },
        {
            "customerNumber": "RSCN03",
            "customerFirstName": "Izuku",
            "customerLastName": "Midoriya",
            "age": 18,
            "address": {
                "city": "Tokyo",
                "country": "Japan"
            },
            "accounts": [
                {
                    "accountNumber": "RSAN04",
                    "cardNumber": "123456781234011",
                    "creditLimit": 200000,
                    "branch": "Ortigas"
                }
            ]
        },
        {
            "customerNumber": "RSCN04",
            "customerFirstName": "Maelle",
            "customerLastName": "Dessandre",
            "age": 16,
            "address": {
                "city": "Paris",
                "country": "France"
            },
            "accounts": [
                {
                    "accountNumber": "RSAN05",
                    "cardNumber": "123456781234022",
                    "creditLimit": 500000,
                    "branch": "Ortigas"
                },
                {
                    "accountNumber": "RSAN06",
                    "cardNumber": "123456781234033",
                    "creditLimit": 700000,
                    "branch": "Ortigas"
                },
                {
                    "accountNumber": "RSAN07",
                    "cardNumber": "123456781234044",
                    "creditLimit": 1000000,
                    "branch": "Cubao"
                }
            ]
        }
    ]

    # output = db["customerAccounts"].insert_many(customerAccountsDocuments)
    # print(output)

    #Inserting special numeric characters
    db = conn["test2"]
    
    intValue = 100 # This is how to store a 32-bit int into a variable. We'll insert this later to mongodb.
    bigIntValue = Int64(9223372036854775807) # if you check the top part of this code, you'll see that we imported Int64 from bson.int64. This will allow us to cast the type of our 64-bit int
    doubleValue = 10000.50 # This is how to store a double into a variable
    decimal128Value = Decimal128(Decimal("123.431238971985")) # If you check the top part of this code, we imported Decimal128 from bson.decimal128. We also imported Decimal from decimal. We'll use these 2 functions to cast the type of our decimal 128 number

    db['numbers'].insert_one({ "value": intValue }) # insert 32-bit integer
    db['numbers'].insert_one({ "value": bigIntValue }) # insert 64-bit integer
    db['numbers'].insert_one({ "value": doubleValue }) # insert double
    db['numbers'].insert_one({ "value": decimal128Value }) # insert decimal128

    print("✅ Inserted Numbers!")

    conn.close()