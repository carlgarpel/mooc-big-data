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
lo que genera un fichero json con 108.427 documentos (se suprime el registro de cabecera).

Importo el fichero a MongoDB
mongoimport --db convive --file avisos.json

Para prácticas se pide volver a generar los csv a partir de la base de datos MongoDB.
Los ficheros csv en al carpeta csv de este repositorio.

Mediante una utilidad de MongoDB:

mongoexport --db convive --collection resueltos2017 --type=csv --out resueltos2017.csv

Mediante Python
    En la carpeta python se encuentra el script exportcsv.py

Fase de análisis.

En el proyecto CONVIVE se realizarán dos acciones con los datos:
1. Se analizarán los datos existentes del sistema AVISA para obtener información sintetizada de
los incidentes reportados. Para ello debe tenerse en cuenta que el fichero con los datos puede
estar repartido entre varias máquinas y que se debe utilizar un modelo de programación que
facilite el acceso a todos esos datos sin cargar la máquina en la que se ejecute.
2. Se visualizarán los datos del sistema AVISA para que sean más fácilmente entendibles por los
destinatarios finales. Las decisiones finales sobre las acciones a tomar las llevarán a cabo
personas con distintas capacidades de abstracción y síntesis. Para facilitar esas decisiones se
mostrarán los datos mediante modelos visuales que permitan una mejor comprensión de
éstos.

Instalo hadoop mapreduce para realizar las prácticas de ejecución de las tareas de mapeo y
reducción de manera distruibuida. Los script están en este repositorio: en la carpeta python.
    mapper.Py --> Genera un fichero csv con estructura clave valor. En este caso: Distrito
    y TIPO_INCIDENCIA
    reducer.Py--> realiza un sumatorio de las claves agrupadas.
    En este ejercicio lo que se obtiene es información resumida d número de avisos por distrito 
    en la ciudad de Madrid.


Por último, se genera una representación gráfica de esta información con ayuda de Python y las librería
Bokeh.

El script se incluye en este repositorio, y su nombre es visualizador.Py.

El resultado final puede verse en el fichero visualizador.html (recordar que para ver este fichero hace
falta instalarlo en un servidor.)













