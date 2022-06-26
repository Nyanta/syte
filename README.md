# To Do List API

Used technologies:
  * PostreSQL for storing the To Do list
  * Python (Flask, Flask-SQLAlchemy) for API
  
# Setting up the environment

In a directory where the application is placed a virtual environment needs to be set up:

(bash)
```
python3 -m venv env
source env/bin/activate
```

The following Python libraries need to be installed within the activated environment:
* flask
* Flask-SQLAlchemy
* psycopg2
* requests

PostgreSQL needs to be installed (I used version 14.3)
User admin with password 'admin' with superuser privilieges needs to be created, as well as database 'crud':

(psql)
```
create role admin with encrypted password 'admin';
alter user admin with superuser;
create database crud;
grant all privileges on database crud to admin;
```

A todolist table needs to be created: 

(psql)
```
create table todolist (
id serial,
item_name varchar(100),
is_done boolean,
primary key(id)
);
```


# Running the application

The application can be run with flask:

```
export FLASK_APP=app
export FLASK_en=development
flask run
```
