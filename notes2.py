import mysql.connector
from mysql.connector import Error

def connect():
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
                update()
                
    except Error as e:
            print("Error while connecting to MySQL", e)
        
        
    finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    
def update():
    connect()
    print("Before updating a record ")
    sql_select_query = """select * from anime_list where id = 1;"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)
    
    sql_update_query = """Update anime_list set Name = 'yu yu hakusho' where id = 1;"""
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully ")
    
    print("After updating record ")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)


            
        
        

        
        
        
        

    
