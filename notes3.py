import mysql.connector
from mysql.connector import Error

# CREATE TABLE anime_list (id int not null auto_increment primary key, name varchar(255), episode int, Release_Date date);

def connect():
    global connection, cursor
    connection = mysql.connector.connect(host='127.0.0.1', database='note', port='13306', user='root', password='notes')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

def showtable():
    connect()
    cursor.execute("SELECT * FROM anime_list;")
    rows = cursor.fetchall()
    return rows

# create function to create a note
def Create():
    connect()
    print(showtable()) 
    new_name = str(input("Please Enter the Name of the anime :- "))
    no_of_episodes = input("Please Enter the Number of Episodes :- ")
    release_date = input("Please Enter the Release date of the Anime in 'YYYY-MM-DD' format :- ")
    
    sql_create = """INSERT INTO anime_list (Name, No_of_episodes, Release_Date) values ('%s','%s','%s');"""
    data = (new_name, no_of_episodes, release_date)
    cursor.execute(sql_create % data)

    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Anime table")
  
# delete function to delete a note
def delete():
    connect()
    print(showtable()) 
    delete_req = int(input("Please insert the Id for the Anime which you want to delete :- "))
    delete_query = """Delete from anime_list where id = %s;""" % delete_req
    print(delete_query)
    cursor.execute(delete_query)
    connection.commit()
    print('number of rows deleted', cursor.rowcount)

# update function to update the note 
def update():
    connect()
    print(showtable()) 
    update_id = int(input("Please insert the ID for the Anime which you want to update :- "))
    update_name = input("Please insert the Name for the Anime which you want to update :- ")
    update_episodes = input("Please Enter the Number of Episodes :- ")
    release_date = input("Please Enter the Release date of the Anime in 'YYYY-MM-DD' format")
    sql_update_query = """Update anime_list set name = '%s', No_of_episodes = %s, Release_Date = '%s' where id = %s;""" % (update_name, update_episodes, release_date, update_id)
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully ")
    
def main():
    create_new = str(input("Would you like to Create, Update or delete note ? : - "))
    if create_new == 'create':
        Create()
    elif create_new == 'update':
        update()
    elif create_new == 'delete':
        delete()
    else:
        print("Choose the correct option")
    print(showtable())   
    connection.close()

# show table to view the table after the operation

if __name__ == "__main__":
   main()
   connection.close()
