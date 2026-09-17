def tryMatch(conn):
    pipeline = [
        {
            '$match': {
                'age': { '$gte': 30, '$lte': 40 },
                'address.city': 'Taguig'
            }
        }
    ]

    db = conn['ruralSavingsPrime']
    
    results = db['customerAccounts'].aggregate(pipeline)

    for result in results:
        print(result)

def trySort(conn):
    pipeline = [
        {
            '$match': {
                'age': { '$gte': 30, '$lte': 40 },
                'address.city': 'Taguig'
            }
        },
        {
            '$sort': {
                'age': 1
            }
        }
    ]

    db = conn['ruralSavingsPrime']
    
    results = db['customerAccounts'].aggregate(pipeline)

    for result in results:
        print(result)

def tryGroup(conn):
    pipeline = [
        {
            '$match': {
                'type': 'debit'
            }
        },
        {
            '$group': {
                '_id': '$accountNumber',
                'totalSpending': {
                    '$sum': '$amount'
                }
            }
        }
    ]

    db = conn['ruralSavingsPrime']
    
    results = db['transactions'].aggregate(pipeline)

    for result in results:
        print(result)

def tryProject(conn):
    pipeline = [
        {
            '$match': {
                'type': 'debit'
            }
        },
        {
            '$group': {
                '_id': '$accountNumber',
                'totalSpending': {
                    '$sum': '$amount'
                }
            }
        },
        {
            '$project': {
                '_id': 0,
                'totalSpending': 1,
                'accountNumber': '$_id'
            }
        }
    ]

    db = conn['ruralSavingsPrime']
    
    results = db['transactions'].aggregate(pipeline)

    for result in results:
        print(result)

def tryLimit(conn):
    pipeline = [
        {
            '$match': {
                'type': 'debit'
            }
        },
        {
            '$group': {
                '_id': '$accountNumber',
                'totalSpending': {
                    '$sum': '$amount'
                }
            }
        },
        {
            '$project': {
                '_id': 0,
                'totalSpending': 1,
                'accountNumber': '$_id'
            }
        },
        {
            '$limit': 10
        }
    ]

    db = conn['ruralSavingsPrime']
    
    results = db['transactions'].aggregate(pipeline)

    for result in results:
        print(result)


def tryOutSameDb(conn):
    pipeline = [
        {
            '$match': {
                'type': 'debit'
            }
        },
        {
            '$group': {
                '_id': '$accountNumber',
                'totalSpending': {
                    '$sum': '$amount'
                }
            }
        },
        {
            '$project': {
                '_id': 0,
                'totalSpending': 1,
                'accountNumber': '$_id'
            }
        },
        {
            '$out': 'spenders'
        }
    ]

    db = conn['ruralSavingsPrime']
    
    results = db['transactions'].aggregate(pipeline)

    for result in results:
        print(result)

def tryOutDifferentDb(conn):
    pipeline = [
        {
            '$match': {
                'type': 'debit'
            }
        },
        {
            '$group': {
                '_id': '$accountNumber',
                'totalSpending': {
                    '$sum': '$amount'
                }
            }
        },
        {
            '$project': {
                '_id': 0,
                'totalSpending': 1,
                'accountNumber': '$_id'
            }
        },
        {
            '$out': {
                'db': 'ruralSavingsPrimeAnalytics',
                'coll': 'spenders'
            }
        }
    ]

    db = conn['ruralSavingsPrime']
    
    results = db['transactions'].aggregate(pipeline)

    for result in results:
        print(result)

def tryUnwind(conn):
    pipeline = [
        {
            '$unwind': '$accounts'
        }
    ]

    db = conn['ruralSavingsPrime']
    
    results = db['transactions'].aggregate(pipeline)

    for result in results:
        print(result)

def tryLookup(conn):
    pipeline = [
        {
            '$lookup': {
                'from': 'customerAccounts',
                'localField': 'customerNumber',
                'foreignField': 'customerNumber',
                'as': 'transactions'
            }
        }
    ]

    db = conn['ruralSavingsPrime']
    
    results = db['transactions'].aggregate(pipeline)

    for result in results:
        print(result)
