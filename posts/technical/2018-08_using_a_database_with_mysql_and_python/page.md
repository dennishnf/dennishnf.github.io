
## Using a Database with MySQL and Python ##

### 1. Make a Backup ###

Move to the Database location with cd command:

```
$ cd /home/<<x>location<x>>
```

Then, make the Backup into a .sql file:

```
$ mysqldump -u root -p mysql_database <x>> mysql_database_1.sql
```

### 2. Install MySQL dependencies and mysqlclient ###

Install the following dependencies:

```
$ sudo apt-get install mysql-server mysql-client mysql-common 
$ sudo apt-get install libmysqlclient-dev
```

Install "mysqlclient" (you can install into an environment):

```
$ pip install mysqlclient 
```

### 3. Using the backup Database ###

Move to the backup Database location with cd command:

```
$ cd /home/<<x>location<x>>
```

Create an empty database and use it:

```
$ mysql -u root -p
mysql<x>> SHOW DATABASES;
mysql<x>> CREATE DATABASE mysql_database_1;
mysql<x>> USE mysql_database_1;
mysql<x>> SHOW DATABASES;
mysql<x>> SELECT DATABASE(); #see the database that is being used
mysql<x>> EXIT
```

Fill the database created with the .sql file:

```
$ mysql -u root -p mysql_database_1 <<x> mysql_database_1.sql 
```

See the database filled with:

```
$ mysql -u root -p
mysql<x>> SHOW DATABASES;
mysql<x>> USE mysql_database_1;
mysql<x>> SHOW TABLES;
mysql<x>> SHOW COLUMNS FROM sample;
mysql<x>> SHOW COLUMNS FROM user;
mysql<x>> DESCRIBE sample;
mysql<x>> DESCRIBE user;
mysql<x>> EXIT
```

### 4. Using the backup Database with Python ###

Move to the backup Database location with cd command:

```
$ cd /home/<<x>location<x>>
```

Open Jupyter Notebook (or Spyder) and work with the backup Database:

```
$ jupyter notebook
```

```
In [ ]: import MySQLdb
In [ ]: db = MySQLdb.connect(host="localhost", user="root", passwd="<<x>my_root_password<x>>", db="mysql_database_1")
In [ ]: cur = db.cursor()
In [ ]: cur.execute("SELECT * FROM user")
        for row in cur.fetchall():
       		print(row[0])
In [ ]: db.close()
```

