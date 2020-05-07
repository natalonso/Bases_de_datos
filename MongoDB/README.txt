
#################################################
PASOS A SEGUIR PARA LA EJECUCIÓN
#################################################

1. Conversión del fichero con la fuente de datos de xml a json: 
EJECUTAR FICHERO: 1.convertir_xml_json.py

2. División del fichero creado en la etapa anterior en tres ficheros: incollections.json, article.json, inproceedings.json: 
EJECUTAR FICHERO: 2.read_json.py

3. Procesamiento de los tres ficheros json anteriores y carga de datos en MongoDB:
EJECUTAR FICHERO: 3.crear_db_insertMany.py

4. Realizar las consultas:
EJECUTAR FICHERO: consultas.js