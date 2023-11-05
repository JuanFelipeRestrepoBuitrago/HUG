# HUG
HUG (How U Going). Este repositorio corresponde a un proyecto para la materia Ingeniría de Software de lo universidad EAFIT. El cual trata de un dashboard para directivos de universidades.
## Requerimientos
### Python
La versión usada de Python es 3.11.
### PostgreSQL
Antes de correr el proyecto necesitas haber instalado PostgresQL. La versión usada fue 15.4.
### Crea el entorno virtual
```
python -m venv venv
```
### Activa el entorno virtual
```
venv\Scripts\activate
```
### Archivo .env
El archivo .env debe ser creado en la raíz del proyecto.

Linux and Mac:
```
touch .env
```
Windows:
```
type nul > .env
```
El archivo .env contiene las variables de entorno, en este caso, las credenciales de la base de datos.
```
DB_NAME=hug
DB_USER=database_user
DB_PASSWORD=database_password
DB_HOST=localhost
DB_PORT=5432
```
### Instala las librerias
```
pip install -r libraries.txt
```
## Base De Datos
### Crea la base de datos
```
CREATE DATABASE hug;
```
### Crea las tablas
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
Cada libreria es necesaria, aunque la versión es opcional, se recomienda usar las mismas versiones para evitar errores.
### Django
#### Versión
4.2.6
```
pip install django==4.2.6
```
### Psycopg2 (Adaptador PostgreSQL)
#### Versión
2.9.9
```
pip install psycopg2==2.9.9
```
### Decouple
#### Versión
3.8
```
pip install python-decouple==3.8
```
## Corre la aplicación
La primera vez que se corra la aplicación se necesitaran ejecutar los siguientes comandos:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Posteriormente se puede correr la aplicación con el siguiente comando:
```
python manage.py runserver
```
