import insertData
import pymongo
import exportData

def openConnection():
    host = '127.0.0.1'
    port = 27017

    conn = pymongo.MongoClient(host,port)

    return conn

def closeConnection(conn):
    conn.close()

if __name__ == "__main__":

    # fakeCustomers = insertData.generatefakeCustomers()
    # # print(fakeCustomers["accounts"])
    # fakeTransactions = insertData.generateFakeTransactions(fakeCustomers)
    # # print(fakeTransactions)

    # conn = openConnection()

    # db = conn["ruralSavingsPrime"]
    # db["customerAccounts"].insert_many(fakeCustomers)
    # db["transactions"].insert_many(fakeTransactions)

    # closeConnection(conn)

    exportData.exportData()
    

    