import utils, aggregations

if __name__ == "__main__":
    """
    In this main function, we need to uncomment the lines one by one in order to avoid errors
    and also see the code executions step by step. Follow the sequence provided in the comments. Make sure to
    comment the previous line before uncommenting and running the next line.
    """

    # Establish MongoDB connection. Make sure to replace localhost accordingly
    conn = utils.establishConnection('localhost') # Never comment this line as this establishes the connection to MongoDB
    
    # aggregations.tryMatch(conn)
    # aggregations.trySort(conn)
    # aggregations.tryGroup(conn)
    # aggregations.tryProject(conn)
    # aggregations.tryLimit(conn)
    # aggregations.tryOutSameDb(conn)
    # aggregations.tryOutDifferentDb(conn)
    # aggregations.tryUnwind(conn)
    aggregations.tryLookup(conn)

    utils.closeConnection(conn) # Never comment this line as this closes the connection to MongoDB