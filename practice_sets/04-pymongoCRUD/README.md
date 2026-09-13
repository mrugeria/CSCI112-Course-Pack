# [04] Pymongo CRUD

## Introduction

This repo will be used to setup the sample dataset that can be used to apply the lectures on basic Pymongo CRUD operations. You will need to run this first in order to migrate the dateset into your own instance of MongoDB.

## Deleting Existing Data

You may have created the same database in the previous activity that will conflict with this one. Thus, you need to drop that database first. Go to Mongo Shell and run the following commands:

```
use ruralSavingsPrime;
db.dropDatabase();
```

<h2 id=import> Importing Data to MongoDB </h2>

Once you are inside the repository, you can now run the import script which will import database objects into your MongoDB database. Follow these steps:

1. Go to `/home/ubuntu/CSCI112-Course-Pack/practice_sets/04-pymongoCRUD/`
2. Run the script: `python3 import.py`

## Reverting to the Original Database State

If you want to revert to the original database state, you can drop the database and execute [Importing Data to MongoDB](#import) from this manual again.

```
use ruralSavingsPrime;
db.dropDatabase();
```

## Code Structure

This specific repo contains 6 python files, each aiming to teach you the syntax of the CRUD operations in Pymongo. This tutorial will go through these files and run them one at a time.

---
---
<br/><br/>

## Pymongo CRUD Tutorial

### Introduction

Pymongo is a python library that simplifies the interaction of a Python code with a MongoDB Database. It has built in functions that would allow the code to connect to a MongoDB Database, query collections, create documents, update documents, and delete documents, among other things.

---

### `connect.py`

On `04-pymongoCRUD` repo, you will see a file called `connect.py`. Open it.

#### Connecting to a MongoDB Database

On line 9, you can see this line of code:

```
conn = pymongo.MongoClient('localhost', 27017)
```

This line of code calls the `MongoClient()` function from `pymongo` to create a connection to the MongoDB Database in localhost on port 27017. The response of this function is stored in the `conn` variable which is the connection object returned if the connection is successful.

>[!IMPORTANT]
> The parameters of the `MongoClient()` function from `pymongo` are the `host` (IP or hostname) and the `port` (usually 27017 depdending on the MongoDB setup)

On line 11, the response is printed.

>[!NOTE]
> **TO DO: Connect to your MongoDB Database and print the connection object returned.**
> 1. Copy and Paste lines 1-11 of `connect.py` to a blank python file in your EC2 server.
> 2. Run the python code by executing `python3 <your_code_filename.py>`
><br><br>
> Expected Output is similar to this screenshot:
> ![Expected Output is similar to this screenshot](../../assets/04-connect-success.png)

#### Disconnecting from a MongoDB Database

When you have completed all your operations with the MongoDB Database, it is important to always close the connection so that stale connections are avoided. Stale connections may prevent incoming critical operations from being executed due to connection limits.

On the same python file, go to line 13. The `.close()` function from a connection object closes the existing MongoDB connection.

>[!IMPORTANT]
> Always close any connection that you opened with the MongoClient() function.

---

### `insert.py`

On 04-pymongoCRUD repo, you will see a file called `insert.py`. Open it.

>[!IMPORTANT]
> Important terms to remember:
> dictionary - a python data structure used to hold a JSON-like object
> list - the same as array in other programming languages

If you take a look at lines 1-5, there are new imports added. These are used to import any libraries that are needed to create special numeric types in python before you can insert them in MongoDB.

```
import pymongo
from datetime import datetime
from bson.int64 import Int64
from bson.decimal128 import Decimal128
from decimal import Decimal
```

Before we can start with our operations, we first need to open a connection to our MongoDB databse. We do that online 10 as we learned in the previous section of this tutorial.

```
conn = pymongo.MongoClient("localhost",27017)
```

#### Creating a document before inserting to a MongoDB Collection

To insert a document in MongoDB using pymongo, it's best to create a dictionary first to store your document. See `document1` variable below as an example. This variable contains a sample data for our `ruralSavingsTest.customerAccounts` collection that we intend to insert. This can also be found on lines 13-30 of this script.

```
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
```

Below is another variable, `document2`, that contains sample data for our `ruralSavingsTest.transactions` collection that we intend to insert. This can be found on lines 34-42 of this script.

```
document2 = {
    "transactionNumber": "RSCNTXN00001",
    "customerNumber": "RSCN01",
    "accountNumber": "RSAN01",
    "type": "debit",
    "amount": 250,
    "vendor": "Potato Corner",
    "transactionDate": datetime(2025,8,31)
}
```

>[!IMPORTANT]
> Notice in `document2`, `transactionDate`'s value is datetime(2025,8,31).
> This is a conversion function from the `datetime` library in python.
> When inserting data with special datatypes like dates, decimal 128, long integers, etc., the standard python conversion functions must be used before inserting the data in MongoDB.
