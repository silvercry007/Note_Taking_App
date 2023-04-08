Agenda:

Create a Python Application For Connecting it with Database (MYSQL) to 
Do Create , Update , Read and Delete.

Example: python3 shubhnotes.py Create 1 “make me a sandwich by 4pm today”
Python3 shubnotes.py update 1 “sandwhich to be given now”
Python3 shubnotes.py read 2 
Python3 shubnotes.py read “all”



Python3 shubnotes.py Arg1 arg2 arg3 
Where arg1 would be the “function name“ “ID” “data”


#steps 
1. Python script for note taking.
2. Mysql.connector

Connect - mysql.connector.connectoion(host, port, user,pwd)


Import sysargv



Connectivity :

1. Check the connectivity with the database.
2. Able to ping the database.
3. Check if the database is present 
4. Check the table is present


Create : 
	0. Connectivity = true then 
	1. Take the data from Argv
	2. Send the data to Database.
	3. Output the data which we have sent.

Update: 
	0. Connectivity = true
Take the data from argv
Show the previous data.
Update the data from database
Save the data
Output the data.

Read : 
Connectivity = true,Check the db is present,Check table
Argv = specific or All.
Output the data in the db.

Delete:		
	
Connectivity = true,Check the db is present,Check table
Argv = specific or All.
Show the data.
Delete prompt.
Deleted successfully. impo










Sql -    Create database db_notes
	Use database db_notes.
Create table Note ([Sr no] as int primary key, date as datetime,Note as varchar(max))         
	
	To connect 
	mysql.connector.connect(host=”LOCALHOST”, port=, user=”ROOT”,pwd=””)

Def db_create_db(connect):
Query = “create database db_notes”
	
