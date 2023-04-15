import mysql.connector
from mysql.connector import Error

 
# CREATE TABLE anime_list (id int primary key, name varchar(255), episode int), Release_Date datetime);

def connect():
    global  connection, cursor
    connection = mysql.connector.connect(host='127.0.0.1', database='note',port='13306',user='root', password='notes')
    if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)      

# create function to create a note
def Create():
    connect()
    sql_create = """INSERT INTO anime_list values (1, 'Inuyasha' , 203 , 2024-12-19);"""
    cursor.execute(sql_create)

    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Anime table")
    connection.close()
  
# delete function to delete a note
def delete():
    connect()
    sql_Delete_query = """Delete from anime_list where id = 1;"""
    cursor.execute(sql_Delete_query)
    connection.commit()
    print('number of rows deleted', cursor.rowcount)
  
# update function to update the note 
def update():
    connect()
    sql_update_query = """Update anime_list set name = 'Yu Yu hakusho' where id = 2;"""
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully ")
    
    
# show table to view the table after the operation
def showtable():
    connect()
    cursor.execute("SELECT * FROM anime_list;")
    rows=cursor.fetchall()
    connection.close()
    return rows

        
        
Create()
delete()
update()
print(showtable())   