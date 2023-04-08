Firstly install Mysql-connector python.

mysql-connector-python==8.0.32

pip install mysql-connector-python

Docker

To run a MYsql server inside a docker container using localhost run this command.

docker run -p 13306:3306 --name mysql-local -e MYSQL_ROOT_PASSWORD=notes -d mysql:latest

To install Mysql client 

for windows 

choco install mysql

For Ubuntu

sudo apt install mysql-client

once mysql client is installed , you can run the below command

mysql --host=127.0.0.1 --port=13306 -u root -p

To run this python script

python notesppp.py
