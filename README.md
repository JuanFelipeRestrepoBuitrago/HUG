# HUG
HUG (How U Going). It's the repository for the software engineering course project at EAFIT University. It consists of a dashboard for the university directors.
## Requirements
### Python
The version of python used is 3.11.
### PostgreSQL
The version of PostgreSQL used is 15.4.
### Create a virtual environment
```
python -m venv venv
```
### Activate the virtual environment
```
venv\Scripts\activate
```
### .env file
Linux and Mac:
```
touch .env
```
Windows:
```
type nul > .env
```
The .env file is used to store the environment variables, in this case, the database credentials.
```
DB_NAME=database_name
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOST=database_host
DB_PORT=database_port
```
### Install the libraries
```
pip install -r libraries.txt
```
### Run the application
```
python manage.py runserver
```
## Database

## Python Libraries
Each library is necessary to run the application, but the version is optional, we recommend using the version we used.
## Django
### Version
4.2.6
```
pip install django==4.2.6
```
## Psycopg2 (PostgreSQL Adapter)
### Version
2.9.9
```
pip install psycopg2==2.9.9
```
## Decouple
### Version
3.8
```
pip install python-decouple==3.8
```