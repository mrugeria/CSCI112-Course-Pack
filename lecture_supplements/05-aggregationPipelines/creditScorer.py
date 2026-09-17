import pymongo

if __name__ == "__main__":

    conn = pymongo.MongoClient('localhost', 27017)
    db = conn["ruralSavingsPrime"]
    collection = db["transactions"]

    pipeline = [
        {
            '$match': {
                'type': 'debit'
            }
        },
        {
            '$group': {
                '_id': '$customerNumber',
                'customerSpend': {
                    '$sum': '$amount'
                }
            }
        },
        {
            '$sort': {
                'customerSpend': -1
            }
        },
        {
            '$limit': 1
        },
        {
            '$lookup': {
                'from': 'customerAccounts',
                'localField': '_id',
                'foreignField': 'customerNumber',
                'as': 'customer'
            }
        },
        {
            '$unwind': '$customer'
        },
        # {
        #     '$limit': 1
        # },
        {
            '$project': {
                '_id': 0,
                'customerNumber': '$_id',
                'customerfirstName': '$customer.customerFirstName',
                'customerlastName': '$customer.customerLastName',
                'customerSpend': 1
            }
        },
        {
            '$out': 'creditScoreRawTop'
        }
    ]

    collection.aggregate(pipeline);

    results = db['creditScoreRawTop'].find();

    for result in results:
        print(result)

    conn.close()
