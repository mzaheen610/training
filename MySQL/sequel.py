import mysql.connector
from mysql.connector import pooling

"""Creating a connection object using mysql.connector
"""

# db_config = {  
#     'host':'localhost',
#     'user':'connector',
#     'password':'connector',
#     'database':'testdb'
#     }

# connectionPool = pooling.MySQLConnectionPool(pool_name="MySQLPool", pool_size= 15, pool_reset_session= True, **db_config)
# cnx = connectionPool.get_connection()
# print(connectionPool.pool_name)
# print(connectionPool._pool_size)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "connector",
    password = "connector",
    database = "testdb"
)

print("Connection Successful")

# mycursor = cnx.cursor()

mycursor = mydb.cursor()

## Inserting (CREATE) into a table using the connector

statement = "INSERT INTO employees (id, firstname, lastname, joinDate, district) VALUES (12, 'Rani', 'Mukherjee', '2023-10-01', 'Worli')"
mycursor.execute(statement)
mydb.commit()
print(mycursor.rowcount, "record is inserted")

#Deleting a record from a table

statement = "DELETE FROM employees WHERE id IN (11,12)"
mycursor.execute(statement)
mydb.commit()


#Update a table

statement = "UPDATE employees SET firstname='Tony' WHERE firstname='David'"
mycursor.execute(statement)
mydb.commit()
print(mycursor.rowcount)

#Reading from a table

mycursor.execute("SELECT * FROM employees")
result = mycursor.fetchall()
for row in result:
    print(row)

print("Done....")

mycursor.close()

# cnx.close()
mydb.close()
