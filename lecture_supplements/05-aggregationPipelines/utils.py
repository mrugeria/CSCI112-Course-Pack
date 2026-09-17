import pymongo

def establishConnection(host='localhost'):
    conn = pymongo.MongoClient(host, 27017)
    return conn

def closeConnection(conn):
    conn.close()