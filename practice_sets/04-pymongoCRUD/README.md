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

### `connect.py`

On `04-pymongoCRUD` repo, you will see a file called connect.py. Open it.

On line 9, you can see this line of code:

```
conn = pymongo.MongoClient('localhost', 27017)
```

This line of code calls the `MongoClient()` function from `pymongo` to create a connection to the MongoDB Database in localhost on port 27017. The response of this function is stored in the `conn` variable which is the connection object returned if the connection is successful.

>[!IMPORTANT]
> The parameters of the `MongoClient()` function from `pymongo` are the `host` (IP or hostname) and the `port` (usually 27017 depdending on the MongoDB setup)

On line 11, the response is printed.

>[!TODO]
> Try connecting to your MongoDB Database and print the connection object returned.
> Copy and Paste lines 1-11 of `connect.py` to a blank python file in your EC2 server.
> Run the python code by executing `python3 <your_code_filename.py>`