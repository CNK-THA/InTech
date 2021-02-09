
import sqlite3
from sqlite3 import Error

conn = None
try:
    conn = sqlite3.connect("ShoppingDatabase.sqlite")
    cursorObject = conn.cursor()
    # dropTable = "DROP TABLE products"
    # cursorObject.execute(dropTable)

    # createTable = "CREATE TABLE products(name varchar(255), price int)"
    # cursorObject.execute(createTable)

    # insertInto = "INSERT INTO products VALUES('testing', 50)"
    # cursorObject.execute(insertInto)

    getAll = "SELECT * FROM products"
    queryResults = cursorObject.execute(getAll)
    for result in queryResults:
        print(result)
    # print(sqlite3.version)

    conn.commit()
except Error as e:
    print(e)
# finally:
#     if conn:
#         conn.close()



 
