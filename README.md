# HUG
HUG (How U Going). It's the repository for the software engineering course project at EAFIT University. It consists of a dashboard for the university directors.
## Requirements
### Python
The version of python used is 3.11.
### PostgreSQL
Before running the application ensure you have PostgreSQL in your computer. The version of PostgreSQL used is 15.4.
### Create a virtual environment
```
python -m venv venv
```
### Activate the virtual environment
```
venv\Scripts\activate
```
### .env file
The .env file must be created in the root of the project.

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
DB_NAME=hug
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOST=localhost
DB_PORT=5432
```
### Install the libraries
```
pip install -r libraries.txt
```
## Database
### Create the database
```
CREATE DATABASE hug;
```
### Create tables
Para crear las tablas se debe ejecutar el siguiente script en la consola de PostgreSQL. El
acceso a los archivos csv se debe cambiar de acuerdo a la ubicación de los mismos en el equipo.
Dichos archivos se deben solicitar a los integrantes del grupo previamente.
```
-- Borra las tablas si existen
DROP TABLE IF EXISTS PUBLIC.sector CASCADE;
DROP TABLE IF EXISTS PUBLIC.egresado CASCADE;
DROP TABLE IF EXISTS PUBLIC.sectores_egresados CASCADE;
DROP TABLE IF EXISTS PUBLIC.experiencia CASCADE;
DROP TABLE IF EXISTS PUBLIC.estudio CASCADE;

-- Crea la tabla si no existe
CREATE TABLE IF NOT EXISTS PUBLIC.sector (
    id SERIAL PRIMARY KEY NOT NULL,
    nombre VARCHAR(350) NOT NULL
);

-- Inserta los datos del archivo CSV a la tabla
COPY sector (id, nombre)
FROM 'D:\ArchivosdeAplicaciones\PostgreSQL\EAFIT\INGENIERIA DE SOFTWARE\HUG\CSVs\sectores.csv'
WITH CSV HEADER NULL '' DELIMITER ';';

-- Crea la tabla si no existe
CREATE TABLE IF NOT EXISTS PUBLIC.egresado (
	id SERIAL PRIMARY KEY,
	fecha_nacimiento DATE,
    nivel_educativo VARCHAR(250),
    salario DOUBLE PRECISION,
    experiencia_meses INTEGER,
    ciudad VARCHAR(250)
);

-- Inserta los datos del archivo CSV a la tabla
COPY egresado (id, fecha_nacimiento, salario, nivel_educativo, experiencia_meses, ciudad)
FROM 'D:\ArchivosdeAplicaciones\PostgreSQL\EAFIT\INGENIERIA DE SOFTWARE\HUG\CSVs\procesado_v0.csv'
WITH CSV HEADER NULL '' DELIMITER ';';

-- Crea la tabla si no existe
CREATE TABLE IF NOT EXISTS PUBLIC.sectores_egresados (
    id SERIAL PRIMARY KEY NOT NULL,
    sector_id INTEGER,
    egresado_id INTEGER,
    FOREIGN KEY (sector_id) REFERENCES sector(id),
    FOREIGN KEY (egresado_id) REFERENCES egresado(id)
);

-- Inserta los datos del archivo CSV a la tabla
COPY sectores_egresados (id, egresado_id, sector_id)
FROM 'D:\ArchivosdeAplicaciones\PostgreSQL\EAFIT\INGENIERIA DE SOFTWARE\HUG\CSVs\sectores_egresados.csv'
WITH CSV HEADER NULL '' DELIMITER ';';

-- Crea la tabla si no existe
CREATE TABLE IF NOT EXISTS PUBLIC.experiencia (
	id SERIAL PRIMARY KEY,
	empresa TEXT,
    cargo TEXT,
    fecha_inicio DATE,
    fecha_fin DATE,
    egresado_id INTEGER,
    FOREIGN KEY (egresado_id) REFERENCES egresado(id)
);

-- Inserta los datos del archivo CSV a la tabla
COPY experiencia (id, empresa, cargo, fecha_inicio, fecha_fin, egresado_id)
FROM 'D:\ArchivosdeAplicaciones\PostgreSQL\EAFIT\INGENIERIA DE SOFTWARE\HUG\CSVs\experiencia_egresado.csv'
WITH CSV HEADER NULL '' DELIMITER ';';

-- Crea la tabla si no existe
CREATE TABLE IF NOT EXISTS PUBLIC.estudio (
	id SERIAL PRIMARY KEY,
	titulo TEXT,
    institucion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE,
    egresado_id INTEGER,
    FOREIGN KEY (egresado_id) REFERENCES egresado(id)
);

-- Inserta los datos del archivo CSV a la tabla
COPY estudio (id, egresado_id, titulo, institucion, fecha_inicio, fecha_fin)
FROM 'D:\ArchivosdeAplicaciones\PostgreSQL\EAFIT\INGENIERIA DE SOFTWARE\HUG\CSVs\estudio_egresados.csv'
WITH CSV HEADER NULL '' DELIMITER ';';
```

## Python Libraries
Each library is necessary to run the application, but the version is optional, we recommend using the version we used.
### Django
#### Version
4.2.6
```
pip install django==4.2.6
```
### Psycopg2 (PostgreSQL Adapter)
#### Version
2.9.9
```
pip install psycopg2==2.9.9
```
### Decouple
#### Version
3.8
```
pip install python-decouple==3.8
```
## Run the application
If is the first time you run the application, you must run the following commands:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
If you have already run the application, you must run the following commands:
```
python manage.py runserver
```
