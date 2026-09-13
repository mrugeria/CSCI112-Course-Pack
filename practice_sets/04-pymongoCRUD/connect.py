import pymongo

if __name__ == "__main__":

    """
    Line 9 calls the MongoClient() function from pymongo to create a connection
    to the MongoDB Database in localhost on port 27017.
    """
    conn = pymongo.MongoClient('localhost', 27017)

    print(conn) #print the connection object to see what it contains