# mooc-big-data
Big Data para la Ciudad Inteligente Proyecto Convive - Curso MOOC Miriadax - Mayo-2017

Resumen del enunciado del ejercicio de prácticas.

Mejorar el conocimiento del estado de la ciudad de Madrid mediante la información aportada por los ciudadanos
y  la medición de diversos datos del entorno.

Las tareas objeto de este trabajo son:
1. Obtener los ficheros de datos del sistema AVISA del Ayuntamiento de Madrid.
2. Obtener los ficheros de ruido del Ayuntamiento de Madrid.
3. Crear el procedimiento de transformación de entradas de la base de datos en ficheros en
formato compatible con los del sistema AVISA.
4. Incluir todos los ficheros, los del sistema AVISA, los generados a partir de la base de datos y los
de ruido, en un sistema de ficheros distribuido. 

Desde una supusta aplicación web realiza el matenimiento de la base de datos Avisa, que se intengra dentro de 
un servidor de MongoDb.
- Crear base de datos, colección y documentos en MongoDB.
- Crear procedimiento para exportar de JSON a CVS:
    - Con herramiento Mongo.
    - Con Python.

Procedimiento:

Descargo los ficheros CSV de http://datos.madrid.es, en concreto:

Avisos ciudadanos recibidos en el Ayuntamiento año 2017, y
Avisos ciudadanos resueltos 2017.

Creo la base de datos avisos en MongoDB.
mongod # inicia el servidor MongoDB
mongo  # inicia el cliente.
use convive # crear la base de datos
db.avisos.insert() crea la colección avisos e inserta documentos.
db.avisosresueltos.insert() crea la colección avisosresueltos e inserta documentos.
Previamente he convertido los ficheros csv en json mediante la librería NPM csvtojson
https://www.npmjs.com/package/csvtojson
npm i --save csvtojson -g
csvtojson "avisa-avisos ciudadanos mensuales resueltos 201703.csv" 
--delimiter=; >resueltos2017.json
lo que genera un fichero json con 108.428 documentos.

Importo el fichero a MongoDB
mongoimport --db convive --file avisos.json



