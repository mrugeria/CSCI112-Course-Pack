# [03] MongoDB Data Structures and MongoSH CRUD

## Introduction

This repo will be used to setup the sample dataset that can be used to apply the lectures on basic MongoSH CRUD operations. You will need to run this first in order to migrate the dateset into your own instance of MongoDB.

<h2 id=import> Importing Data to MongoDB </h2>

Once you are inside the repository, you can now run the import script which will import database objects into your MongoDB database. Follow these steps:

1. Go to `/home/ubuntu/CSCI112-Course-Pack/practice_sets/03-mongodbDS/`
2. Run the script: `python3 import.py`

## Reverting to the Original Database State

If you want to revert to the original database state, you can drop the database and execute [Importing Data to MongoDB](#import) from this manual again.

```
use ruralSavingsPrime;
db.dropDatabase();
```


---
---
<br/><br/>

## mongosh CRUD Tutorial

In this section, we will go through the different commands in mongosh discussed in class. 

>[!WARNING]
>Make sure you are logged into Mongo Shell before running these commands.

### CREATE - `insertOne()` and `insertMany()`

When inserting documents into your MongoDB collection, you need to select your target database first. You can run `use ruralSavingsTest;` inside mongosh to select the ruralSavingsTest database.

#### Insert Basic Syntax

Now to insert your first document, you must first build your document. A document is always in a valid JSON format. Although in mongosh, you are allowed to omit the quotations for keys.

Which means if your document is:

```
{
    "customerName": "Luka Doncic",
    "customerNumber": "C00077",
    "age": 26,
    "address": {
        "city": "Quezon City",
        "country": "Philippines"
    },
    "accounts": [
        {
            "accountNumber": "C090289",
            "cardNumber" "0000 0000 0000 0077
            "creditLimit": 500000,
            "activeIndicator": true
        },
        {
            "accountNumber": "C090280",
            "cardNumber" "0000 0000 0000 1177
            "creditLimit": 50000,
            "activeIndicator": false
        }
    ]
}
```

You can either declare age as `{ age: 26 }` or `{ "age": 26}` in mongosh.

Now, let's try to insert the document above. You can insert one document at a time using `db.customerAccounts.insertOne({})` like the example below:

```
db.customerAccounts.insertOne({
    "customerName": "Luka Doncic",
    "customerNumber": "C00077",
    "age": 26,
    "address": {
        "city": "Quezon City",
        "country": "Philippines"
    },
    "accounts": [
        {
            "accountNumber": "C090289",
            "cardNumber": "0000 0000 0000 0077",
            "creditLimit": 500000,
            "activeIndicator": true
        },
        {
            "accountNumber": "C090280",
            "cardNumber": "0000 0000 0000 1177",
            "creditLimit": 50000,
            "activeIndicator": false
        }
    ]
});
```

Alternatively, you can insert multiple documents at a time using `db.customerAccounts.insertMany([])`. Note that this function accepts an array of JSON objects, thus the parameter being enclosed in `[]`. The example below shows how this can be done:

```
db.customerAccounts.insertMany([
    {
        "customerName": "Luka Doncic",
        "customerNumber": "C00077",
        "age": 26,
        "address": {
            "city": "Quezon City",
            "country": "Philippines"
        },
        "accounts": [
            {
                "accountNumber": "C090289",
                "cardNumber": "0000 0000 0000 0077",
                "creditLimit": 500000,
                "activeIndicator": true
            },
            {
                "accountNumber": "C090280",
                "cardNumber": "0000 0000 0000 1177",
                "creditLimit": 50000,
                "activeIndicator": false
            }
        ]
    },
    {
        "customerName": "Kobe Bryant",
        "customerNumber": "C00024",
        "age": 42,
        "address": {
            "city": "Pasig",
            "country": "Philippines"
        },
        "accounts": [
            {
                "accountNumber": "C090265",
                "cardNumber": "0000 0000 0000 0824",
                "creditLimit": 5000000,
                "activeIndicator": true
            },
            {
                "accountNumber": "C090280",
                "cardNumber": "0000 0000 0000 1824",
                "creditLimit": 10000000,
                "activeIndicator": true
            }
        ]
    }
]);
```

#### Inserting Date Values

You can also insert datetime objects in MongoDB. To do that you can use the `ISODate()` function to convert a date string to datetime in MongoDB. Example: `ISODate('2024-01-01')`.

Thus, if you want to insert a transaction in the ruralSavingsTest.transaction collection, you can use the following script:

```
db.transactions.insertOne(
    {
        "transactionNumber": "TX00001",
        "customerNumber": "C00001",
        "accountNumber": "A00001",
        "type": "debit",
        "amount": 100000,
        "vendor": "Kahit Saan",
        "transactionDate": ISODate("2025-09-08")
    }
);
```

If you run `db.transactions.find()`, you will see that this document was inserted:

```
{
  _id: ObjectId('68bef4b501db05a15b55deea'),
  transactionNumber: 'TX00001',
  customerNumber: 'C00001',
  accountNumber: 'A00001',
  type: 'debit',
  amount: 100000,
  vendor: 'Kahit Saan',
  transactionDate: 2025-09-08T00:00:00.000Z
}
```

Notice how the `transactionDate` attribute is now formatted as a timestamp. In MongoDB, there are no date values. They are always turned into timestamps.

#### Inserting Special Numeric Values

We mentioned in class that there are different types of numeric attributes that we can store in MongoDB:

- int: 32-bit integer  
- long: 64-bit integer  
- double: 64-bit floating-point number  
- decimal128: 128-bit decimal-based floating-point (for high-precision calculations like money)

For this demo, let's use the test database. Run `use test;`

To insert a 32-bit integer, you just need to specify a regular integer. Example:

```
db.numbers.insertOne({ "value": 10000});
```

To insert a 64-bit integer, You can use the function `NumberLong()` to explicitly tell MongoDB that this value is a 64-bit integer.

```
db.numbers.insertOne({ "value": NumberLong(9223372036854775807) });
```

The value above is the max value for a 64-bit integer. For larger numbers, you may use double or decimal128.

To insert a double, just add decimal numbers to the value. Example:

```
db.numbers.insertOne({ "value": 1000.50 });
```

Finally, to insert Decimal128 numbers which is the best data type for representing financials, we can use the `NumberDecimal()` function:

```
db.numbers.insertOne({ "value": NumberDecimal(1000000.502189732189732198) });
```

That's it for creating documents in MongoDB! The key here is to master how to create JSON objects. My tip is to master how nested objects and array objects are built.

### READ - find()

The `find()` function is the most essential part of mongosh operations. This allows you to query your mongoDB collections.

The `find()` function accepts a parameter in the JSON format. So the rule of thumb here is if a JSON validator says that your query is not a valid JSON, then your query will most probably not work. But, the thing with mongosh is that it accepts JSON keys that are not enclosed in `""` as mentioned in the create lecture above.

This means that `{ "age": 30 }` and `{ age: 30 }` are both accepted queries in JSON format.

#### Basic Query

Let's dive in to the basic format of queries:

```
db.<collectionName>.find({<JSON query object here>})
```

The structure of the JSON query object looks like this:

```
{
    <field>: <value>,
    <field>: <value> #Optional
}
```

There can be one or more query conditions inside the JSON object. They should be separated by a comma and that comma indicates an `AND` logical operator.

In the example below, we will be using the ruralSavingsPrime database so switch to that once you have imported the data in this git repo. Type `use ruralSavingsPrime;`.

Example, if you want to run the query `SELECT * FROM ruralSavings.customerAccounts WHERE age = 30;`, this is the mongoDB equivalent:

```
db.customerAccounts.find(
    { "age": 30 }
)
```

The query will return all documents with age = 30.

#### Querying Nested Objects

Our document in the `customerAccounts` collection is in the following format:

```
{
    "customerName": "Luka Doncic",
    "customerNumber": "C00077",
    "age": 26,
    "address": {
        "city": "Pasay",
        "country": "Philippines"
    },
    "accounts": [
        {
            "accountNumber": "C090289",
            "cardNumber": "0000 0000 0000 0077",
            "creditLimit": 500000,
            "activeIndicator": true
        },
        {
            "accountNumber": "C090280",
            "cardNumber": "0000 0000 0000 1177",
            "creditLimit": 50000,
            "activeIndicator": false
        }
    ]
}
```

What if we want to query all customers who live in 'Pasay' from our customerAccounts colelction? Or in SQL terms, `SELECT * FROM ruralSavings.customerAccounts WHERE age = 30 AND cityAddress = “Pasay”;`?

When querying nested objects, we can use the dot notation where in we access nested keys by separating the parent key and the child key with a dot. Example: `address.city`.

So if we want to implement that in our query, this is how it will look like:

```
db.customerAccounts.find(
    {
        "age": 30,
        "address.city": "Pasay"
    }
)
```

**Take note: when accessing nested objects using dot notation, mongosh requires the key to be enclosed in quotations. Otherwise, the query will not work**

#### Querying Nested Objects with Multiple Levels

What if our address field looks like this:

```
{
    "address": {
        "cityAddress": {
            "city": "Pasig",
            "barangay": {
                "name": "Ugong"
            }
        }
        "country": "Philippines"
    }
}
```

Can we still query customers who live in Pasig even if it's nested multiple times?

Yes. Try to insert the following documents in `ruralSavingsTest.customerAccounts`:

```
db.customerAccounts.insertMany([
    {
        "customerName": "Luka Doncic",
        "customerNumber": "C00077",
        "age": 26,
        "address": {
            "cityAddress": {
                "city": "Pasig",
                "barangay": {
                    "name": "Ugong"
                }
            },
            "country": "Philippines"
        },
        "accounts": [
            {
                "accountNumber": "C090289",
                "cardNumber": "0000 0000 0000 0077",
                "creditLimit": 500000,
                "activeIndicator": true
            },
            {
                "accountNumber": "C090280",
                "cardNumber": "0000 0000 0000 1177",
                "creditLimit": 50000,
                "activeIndicator": false
            }
        ]
    },
    {
        "customerName": "Kobe Bryan",
        "customerNumber": "C00024",
        "age": 42,
        "address": {
            "cityAddress": {
                "city": "Pasig",
                "barangay": {
                    "name": "Sta. Lucia"
                }
            },
            "country": "Philippines"
        },
        "accounts": [
            {
                "accountNumber": "C090123",
                "cardNumber": "0000 0000 0000 0824",
                "creditLimit": 500000,
                "activeIndicator": true
            },
            {
                "accountNumber": "C0902111",
                "cardNumber": "0000 0000 0000 1824",
                "creditLimit": 50000,
                "activeIndicator": false
            }
        ]
    }
]);
```

You can run the following query to get only the customers who live in Pasig:

```
db.customerAccounts.find(
    {
        "address.cityAddress.city": "Pasig",
    }
)
```

If you want to query customers who live in Ugong, Pasig only, you may use the following query:

```
db.customerAccounts.find(
    {
        "address.cityAddress.city": "Pasig",
        "address.cityAddress.barangay.name": "Ugong"
    }
)
```

>[!NOTE]
>The MongoDB BSON format supports nesting up to 100 levels. Beyond this, you will hit an error. This means that accessing nested objects using dot notation can only be done up to 100 levels. The 16MB document limit must also be considered when dealing with multi-level documents.See https://www.mongodb.com/docs/manual/reference/limits/

#### Querying Arrays

The difference with arrays is that objects, even when nested, refer to a single thing only. Like the address example above, even if we nest it further, it still describes a single thing which is the address of the customer. On the other hand, arrays contain multiple values like the accounts array in our document. Each element of the array describes an account of a customer, and a customer can have multiple accounts.

Therefore, when querying arrays, once a condition is met for a single element in the array, all elements will be returned together with the document. This behavior is what I was erroneously referring to in the objects topic during class.

Now, querying arrays is similar to querying objects. In this example, let us use the `ruralSavingsPrime` database.

This is the query for all customers with an active account in at least 1 branch:

```
db.customerAccounts.find(
    {
        "accounts.activeIndicator": true
    }
)
```

If you browse your results, you can see this document which shows you a customer with accounts that are all active:

```
{
  _id: '68b349aa9044de7e12f74e23',
  customerNumber: 'RSCN126979',
  customerFirstName: 'Tonya',
  customerLastName: 'Cook',
  age: 21,
  address: {
    city: 'Quezon City',
    country: 'Philippines'
  },
  accounts: [
    {
      accountNumber: 'RSAN546022',
      cardNumber: '589279097887',
      creditLimit: 674393,
      activeIndicator: true,
      branch: 'Megamall'
    },
    {
      accountNumber: 'RSAN932769',
      cardNumber: '2700142072320327',
      creditLimit: 4344059,
      activeIndicator: true,
      branch: 'Cembo'
    },
    {
      accountNumber: 'RSAN599659',
      cardNumber: '372826567028004',
      creditLimit: 2893560,
      activeIndicator: true,
      branch: 'Ortigas Center'
    },
    {
      accountNumber: 'RSAN150571',
      cardNumber: '4498967175676262',
      creditLimit: 2050771,
      activeIndicator: true,
      branch: 'BGC'
    },
    {
      accountNumber: 'RSAN198438',
      cardNumber: '5565051565183141',
      creditLimit: 3825281,
      activeIndicator: true,
      branch: 'Manila'
    }
  ]
}
```

However, you can also see this document where there are some accounts that are inactive:

```
{
  _id: '68b349aa9044de7e12f74e24',
  customerNumber: 'RSCN947615',
  customerFirstName: 'John',
  customerLastName: 'Chase',
  age: 25,
  address: {
    city: 'Pasig',
    country: 'Philippines'
  },
  accounts: [
    {
      accountNumber: 'RSAN464032',
      cardNumber: '4608948555103785',
      creditLimit: 658930,
      activeIndicator: true,
      branch: 'Diliman'
    },
    {
      accountNumber: 'RSAN727033',
      cardNumber: '4693337669565368',
      creditLimit: 4933061,
      activeIndicator: false,
      branch: 'Ortigas Center'
    },
    {
      accountNumber: 'RSAN620411',
      cardNumber: '30584372412632',
      creditLimit: 865367,
      activeIndicator: true,
      branch: 'Pioneer'
    },
    {
      accountNumber: 'RSAN316479',
      cardNumber: '4103876348270852',
      creditLimit: 2526361,
      activeIndicator: true,
      branch: 'Diliman'
    },
    {
      accountNumber: 'RSAN910797',
      cardNumber: '3557813690768236',
      creditLimit: 3580231,
      activeIndicator: false,
      branch: 'Manila'
    },
    {
      accountNumber: 'RSAN851851',
      cardNumber: '6011481604384376',
      creditLimit: 1820997,
      activeIndicator: false,
      branch: 'Cubao'
    },
    {
      accountNumber: 'RSAN901895',
      cardNumber: '676116498319',
      creditLimit: 3483601,
      activeIndicator: true,
      branch: 'Manila'
    },
    {
      accountNumber: 'RSAN219919',
      cardNumber: '4266142156118493230',
      creditLimit: 2833673,
      activeIndicator: true,
      branch: 'Legarda'
    },
    {
      accountNumber: 'RSAN743996',
      cardNumber: '3512654111477559',
      creditLimit: 4762773,
      activeIndicator: true,
      branch: 'Megamall'
    },
    {
      accountNumber: 'RSAN688192',
      cardNumber: '372458025119660',
      creditLimit: 1795159,
      activeIndicator: false,
      branch: 'MOA Complex'
    },
    {
      accountNumber: 'RSAN248288',
      cardNumber: '4251307149862515',
      creditLimit: 469137,
      activeIndicator: true,
      branch: 'Shaw Boulevard'
    }
  ]
}
```

This is what this statement means:

> Therefore, when querying arrays, once a condition is met for a single element in the array, all elements will be returned together with the document. This behavior is what I was erroneously referring to in the objects topic during class.

If you want to achieve a query that strictly filters the accounts embedded inside a customer, you will need to implement an **aggregation pipeline** instead of a query. This will be discussed in another module.

#### Basic Query Operators

Sometimes, parameters need operators for more complex querying. Here are query operators that can be used for non-array and non-nested object attributes:

- $eq – get documents with value equal to the specified value based on a specified key
- $ne – get documents with value not equal to the specified value based on a specified key
- $in – get documents with value equal to any item in a list of values based on a specified key
- $nin – get documents with value not equal to any item in a list of values based on a specified key
- $elemMatch – get documents that match a criteria set to arrays

Example, you want to show your customers in ruralSavingsPrime.customerAccounts whose age is NOT equal to 30 and lives in Pasig or Taguig. (Or in SQL terms: `SELECT * FROM ruralSavingsPrime.customerAccounts WHERE age <> 30 AND cityAddress in ("Pasig", "Taguig");`):

```
db.customerAccounts.find(
    {
        "age": { $ne: 30 },
        "address.city": { $in: ["Pasig", "Taguig"] }
    }
)
```

You can also do the opposite (`SELECT * FROM ruralSavingsPrime.customerAccounts WHERE age = 30 AND cityAddress not in ("Pasig", "Taguig");`) using the query below:

```
db.customerAccounts.find(
    {
        "age": { $eq: 30 },
        "address.city": { $nin: ["Pasig", "Taguig"] }
    }
)
```

For arrays, you can also use `$elemMatch` to check for matches within queries. However, it behaves similar to using equals or `:` so it's recommended to make your query simpler and use `:` instead of `$elemMatch`. This means that

```
db.customerAccounts.find(
    {
        "accounts.activeIndicator": true
    }
)
```

is the same as

```
db.customerAccounts.find(
    {
        "accounts": {
            $elemMatch: { activeIndicator: true }
        }
    }
)
```

You can instantly see which query is simpler. I recommend you use that format.

#### Numeric and Timestamp Query Operators

For numeric and timestamp attributes, you can use the following operators to query documents with attribute values less than or greater than the specified value in the query.

- $lt – get documents with values less than the specified value base on a specified key
- $lte – get documents with value less than or equal to the value based on a specified key 
- $gt – get documents with value greater than the specified value based on a specified key 
- $gte – get documents with value greater than or equal to the specified value based on a specified key

Example, if you want to show your customers in ruralSavingsPrime.customerAccounts whose age is less than or equal to 30 and lives in Pasig and Taguig. (Or in SQL terms: `SELECT * FROM ruralSavingsPrime.customerAccounts WHERE age <= 30 AND cityAddress in ("Pasig", "Taguig");`)

```
db.customerAccounts.find(
    {
        "age": { $lte: 30 },
        "address.city": { $in: ["Pasig", "Taguig"] }
    }
);
```

You can also get the opposite by using `$gte` and `$nin` (`SELECT * FROM ruralSavingsPrime.customerAccounts WHERE age >= 30 AND cityAddress not in ("Pasig", "Taguig");`):

```
db.customerAccounts.find(
    {
        "age": { $gte: 30 },
        "address.city": { $nin: ["Pasig", "Taguig"] }
    }
);
```

You can also use this with dates. Let's say you want to query all transactions greater than 2020-01-01. You can run this script:

```
db.transactions.find(
    {
        "transactionDate": { $gte: ISODate("2020-01-01") }
    }
);
```

#### Query to get documents where a specified field exists/does not exist

Since MongoDB can have flexible schemas, you cannot avoid documents having fields that others don't. This is evident in data models that follow the inheritance and schema versioning patterns.

This is where the `$exists` operator is useful. For example, you want to see documents that don't have the age field in ruralSavingsPrime.customerAccounts, you can run the following query:

```
db.customerAccounts.find(
    {
        "age": { $exists: true }
    }
)
```

You can also query the opposite, where documents without the age field are returned:


```
db.customerAccounts.find(
    {
        "age": { $exists: false }
    }
)
```

#### Logical Operators

Logical operators are used to add logic to your parameters for more complex querying. By default, using comma to separate conditions in a query implements the `$and` logical operator. Which means that this query:

```
db.transactions.find(
    {
        "transactionDate": { $gte: ISODate("2020-01-01") },
        "type": "debit"
    }
);
```

means you want to retrieve documents where `transactionDate` is greater than or equal to 2020-01-01 **AND** `type` is "debit".

To replace this behavior, you may use the following operators:

- $or – return documents if at least 1 criterion is met
- $not – return documents if the criteria is not met
- $nor – return documents if neither criterion is met
- $and – return documents if both criteria are met

However, the syntax for advanced logical operators is quite different. When using `$or`, `$nor`, or `$not`, you need to enclose the conditions within `[]`.

For instance, if you want to query all transactions later than 2020 or all debit transactions regardless of transactionDate, you may use the following query:

```
db.transactions.find(
    {
        $or: [
            {
                "transactionDate": { $gte: ISODate("2020-01-01") }
            },
            {
                "type": "debit"
            }
        ]
    }
);
```

You can also use `$and` as an alternative to the comma separator:

```
db.transactions.find(
    {
        $and: [
            { "transactionDate": { $gte: ISODate("2020-01-01") } },
            { "type": "debit" }
        ]
    }
);
```

But I suggest you stick to the simpler query format. But if you do that, when do you use `$and`?

As we've said earlier in this tutorial, you cannot specify the same attribute twice in a single query if you will use the comma separation format. For example, if you want to query all transactions in 2020, you might think that this query will work:

```
db.transactions.find(
    {
        "transactionDate": { $gte: ISODate("2020-01-01") },
        "transactionDate": { $lt: ISODate("2021-01-01") }
    }
);
```

If you think about it, the logic is correct. But since JSON does not accept duplicate keys, the second `transactionDate` query will overwrite the first. Thus, instead of querying all transactions in 2020, this will return all transactions earlier than 2021.

This is where `$and` comes in. We can achieve our original goal of getting all transactions in 2020 through the following query:

```
db.transactions.find(
    {
        $and: [
            { "transactionDate": { $gte: ISODate("2020-01-01") } },
            { "transactionDate": { $lt: ISODate("2021-01-01") } }
        ]
    }
);
```

If you browse through the results, you should now only see transactions in 2020.

There is also a third alternative to the `$and` operator. Following the date filter above, you can also use this format:

```
db.transactions.find(
    {
        "transactionDate": {
            $gte: ISODate("2020-01-01"),
            $lt: ISODate("2021-01-01")
        }
    }
);
```

In this format, the key (transactionDate) gets an object as its value which contains the 2 date operators. Again, this is an alternative to `$and` so you choose which format you are most comfortable with, as long as you can achieve your intended logic.

#### Nesting Logical Operators

Logical Operators can also be nested to perform more complex queries. For example, you want to get all transactions in 2020 that are debit transactions, or all transactions in 2021 that are credit transactions, you can use the following query:

```
db.transactions.find(
    {
        $or: [
            {
                $and: [
                    { "transactionDate": { $gte: ISODate("2020-01-01") } },
                    { "transactionDate": { $lt: ISODate("2021-01-01") } },
                    { "type": "debit" }
                ],
            },
            {
                $and: [
                    { "transactionDate": { $gte: ISODate("2021-01-01") } },
                    { "transactionDate": { $lt: ISODate("2022-01-01") } },
                    { "type": "credit" }
                ]
            }
        ]
    }
);
```

#### Final thoughts on querying

In builing MongoDB queries, just remember the basic format. Also remember that you can have as many as conditions as you can. You can definitely build complex queries using the `find()` function, but the limit is if you are working with arrays. That's where **Aggregation Pipelines** will be useful.

### UPDATE - updateOne() and updateMany()

The thing with updates in MongoDB is it's the same with any database. You just need to provide a query first, and then the thing to be updated on the results of your query. The query limits the records that will be updated in your operation. If a query is not provided, all the records in your database will be updated.

#### Basic Syntax of updateOne() and updateMany()

Like the create operation, update also has an `updateOne()` and `updateMany()` function. `updateOne()` will update only the first document found, while `updateMany()` will update all matched documents from the query.

The syntax looks like this:

```
db.<collectionName>.updateMany(
    { <parameters> },
    { $set : { <update objects>},
    $rename: { <oldField>, <newField> } }, #this is optional
    { <options> }
)
```
The `updateMany()` function accepts a parameter still in JSON format, a set of objects to be updated within the `$set` operator, and an optional `$rename` operator to rename attributes in your documents. You can also include options that are available to the updateMany function.

Scenario: In 2019, Rural Savings was targeted by a massive cybersecurity attack. All of their 2019 data in ruralSavingsPrime.transactions, unfortunately, were tampered with. Particularly, 2019 debit transaction vendors were replaced with incorrect values.
Since the data is now fraudulent, the leadership decided to let it go since they didn’t have any backups.
Task: For all debit transactions in 2019, replace the value of “type” to “Fraud”, add a field “isFraud” with a value of True, and rename the “vendor” field to “fraudVendor”.

How do we execute this update and make sure we only target relevant data?

```
db.transactions.updateMany(
    {
        $and: [
            { "type": "debit" },
            { "transactionDate": { $gte: ISODate("2019-01-01") } },
            { "transactionDate": { $lt: ISODate("2020-01-01") } },
        ]
    },
    {
        $set: { "type": "Fraud", "isFraud": true },
        $rename: { "vendor": "fraudVendor" }
    }
);
```

We also have other update operators aside from `$set` and `$rename`.

- $unset – removes the specified key from the document
- $inc – increment the value of the specified key, by the specified amount 
- $mul – multiply the value of the specified key, by the specified amount
- $rename – rename the specified field
- $push – add a value/key-value to an array inside a document
- $addToSet – add a value/key-value to an array with deduplication (NOTE: If you are adding an object to an array instead of a single value, only values that exactly match the incoming key-value pair will be treated as duplicates.)

#### Inserting Key-Value Pairs to Arrays

`$inc` and `$mul` are self explanatory, so we won't dive deep into them anymore. In this part, let's try to insert values into an array. We have 2 options: $push - disregards duplicate key-value pairs and $addToSet which does not insert a new entry if the same key-value pair or object is already in the array.

Let's use our ruralSavingsTest database for this one. `use ruralSavingsTest`. Drop the customerAccounts collection using `db.customerAccounts.drop()`.

Let's insert our test data:

```
db.customerAccounts.insertMany([
    {
        "customerName": "Luka Doncic",
        "customerNumber": "C00077",
        "age": 26,
        "address": {
            "city": "Quezon City",
            "country": "Philippines"
        },
        "accounts": [
            {
                "accountNumber": "C090289",
                "cardNumber": "0000 0000 0000 0077",
                "creditLimit": 500000,
                "activeIndicator": true
            },
            {
                "accountNumber": "C090280",
                "cardNumber": "0000 0000 0000 1177",
                "creditLimit": 50000,
                "activeIndicator": false
            }
        ]
    },
    {
        "customerName": "Kobe Bryant",
        "customerNumber": "C00024",
        "age": 42,
        "address": {
            "city": "Pasig",
            "country": "Philippines"
        },
        "accounts": [
            {
                "accountNumber": "C090265",
                "cardNumber": "0000 0000 0000 0824",
                "creditLimit": 5000000,
                "activeIndicator": true
            },
            {
                "accountNumber": "C090280",
                "cardNumber": "0000 0000 0000 1824",
                "creditLimit": 10000000,
                "activeIndicator": true
            }
        ]
    }
]);
```

We should now have 2 documents in our collection. What if we want to add a new account to Kobe Bryant? We can run the following script:

```
db.customerAccounts.updateMany(
    { "customerName": "Kobe Bryant" },
    {
        $push: {
            "accounts": {
                "accountNumber": "NEW ACCOUNT",
                "cardNumber": "0000 0000 0000 1111",
                "creditLimit": 100,
                "activeIndicator": true
            }
        }
    }
);
```

If we run `db.customerAccounts.find({ "customerName": "Kobe Bryant" });`, we should now be able to see the new account:

```
{
  _id: ObjectId('68bf0f4301db05a15b55deee'),
  customerName: 'Kobe Bryant',
  customerNumber: 'C00024',
  age: 42,
  address: {
    city: 'Pasig',
    country: 'Philippines'
  },
  accounts: [
    {
      accountNumber: 'C090265',
      cardNumber: '0000 0000 0000 0824',
      creditLimit: 5000000,
      activeIndicator: true
    },
    {
      accountNumber: 'C090280',
      cardNumber: '0000 0000 0000 1824',
      creditLimit: 10000000,
      activeIndicator: true
    },
    {
      accountNumber: 'NEW ACCOUNT',
      cardNumber: '0000 0000 0000 1111',
      creditLimit: 100,
      activeIndicator: true
    }
  ]
}
```

We can also use $addToSet to insert into an array:

```
db.customerAccounts.updateMany(
    { "customerName": "Kobe Bryant" },
    {
        $addToSet: {
            "accounts": {
                "accountNumber": "NEW ACCOUNT",
                "cardNumber": "0000 0000 0000 1111",
                "creditLimit": 100,
                "activeIndicator": true
            }
        }
    }
);
```

Notice that the query above did not do anything. This is because `$addToSet` ignores duplicate entries. Try to modify the `activeIndicator` to `false` and see what happens. A new account should be added. In using `$addToSet`, there is no concept of keys. Thus, duplication checking is done by matching all the key-value pairs inside. If at least 1 key-value pair does not match any of the existing documents, a new object will be inserted into the array. You saw this behavior when you replaced the activeIndicator with `false`.

Try to use `$push` again using the same exact document and see if a new account will be added. A new document is added because `$push` ignores duplicates and inserts regardless if an identical object is already inside the array.

>[!NOTE]
>Always keep in mind that updates have optional queries that will allow you to limit the documents to be edited. Otherwise, all documents will be edited. You also cannot `$set` the value of an attribute and `$rename` it at the same time in one update operation. You need to do this separately.

### DELETE - deleteOne() and deleteMany()

The delete functionality is very similar to the update functionality. It also has deleteOne() and deleteMany() functions which deletes the first matched document, and deletes all matched documents respectively.

Unlike the `updateOne()` and `updateMany()` functions, the `deleteOne()` and `deleteMany()` functions only accept a query to filter the documents to be deleted. No need for other options. Here is the basic syntax of the deleteOne() and deleteMany() functions:

```
db.<collectionName>.deleteMany(
    { <parameters> }
)
```

In our previous scenario, the fraud data do not make sense anymore. We may now delete them from the database. To do that, we can use this script:

```
db.transactions.deleteMany(
    {
        "fraudTransactions": true,
    }
)
```

This `deleteMany()` function looks for documents that has `fraudTransactions` set to true. Since we only added this field to the fraudulent transactions of 2019, documents outside of this filter will remain untouched. You may try querying the collection to see that is still has the non fraudulent transactions.

>[!NOTE]
>Always keep in mind that deletes have optional queries that will allow you to limit the documents to be deleted. Otherwise, all documents will be deleted.




