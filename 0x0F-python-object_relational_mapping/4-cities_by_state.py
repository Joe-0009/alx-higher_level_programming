#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select cities from the cities table and join with the states table to get state names
    query = "SELECT cities.id, cities.name, states.name " \
            "FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "ORDER BY cities.id ASC"

    cursor.execute(query)

    # Fetch all the rows in a list of tuples
    cities = cursor.fetchall()

    # Print the cities
    for city in cities:
        print(city)

    # Close the cursor and database connection
    cursor.close()
    db.close()

