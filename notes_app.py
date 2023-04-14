import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='notes',
                                         port='13306',
                                         user='root',
                                         password='notes')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        
# Insert
        
    mySql_insert_query = """INSERT INTO Anime (Id, Name, Episodes, Release_date) 
                           VALUES 
                           (1, 'Inuyasha', 167, '16-10-2000') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Anime table")
    cursor.close()
    
except mysql.connector.Error as error:
    print("Failed to insert record into Anime table {}".format(error))
    
# Read SQL database
    
    sql_select_Query = "select * from Anime"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Episodes  = ", row[2])
        print("Release date  = ", row[3], "\n")
        
# Update SQL Database
        
except mysql.connector.Error as e:
    print("Error reading data from Anime table", e)

    print("Before updating a record ")
    sql_select_query = """select * from Laptop where id = 1"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Update single record now
    sql_update_query = """Update Laptop set Price = 7000 where id = 1"""
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully ")

    print("After updating record ")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Failed to update table record: {}".format(error))
    
    print("Anime table before deleting a row")
    sql_select_query = """select * from Anime where id = 7"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Delete a record
    sql_Delete_query = """Delete from Anime where id = 7"""
    cursor.execute(sql_Delete_query)
    connection.commit()
    print('number of rows deleted', cursor.rowcount)

    # Verify using select query (optional)
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    if len(records) == 0:
        print("Record Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to delete record from table: {}".format(error))

except Error as e:
    print("Error while connecting to MySQL", e)
    

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")