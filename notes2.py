import mysql.connector
from mysql.connector import Error

def insert():
    # Insert   
    
    mySql_insert_query = """INSERT INTO anime_list VALUES (2, 'Dragon ball Z', 291, '1989-04-26'); """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Anime table")
    cursor.close()


try:
    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='Anime',
                                         port='13306',
                                         user='root',
                                         password='notes')
    if connection.is_connected():
        
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        insert()
        
except Error as e:
    print("Error while connecting to MySQL", e)
    
    
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
        
        
        
        

    
