import pymongo
from pymongo import MongoClient
import json

with open('./incollections.json', encoding='utf-8') as f:
    incollections = json.load(f)

print('NÚMERO DE INCOLLECTIONES AL INICIO: ', len(incollections))


conex = pymongo.MongoClient()
db = conex.prueba_dblp
col = db.incollections


####################################################################################
# INCOLLECTIONS:
####################################################################################

lista_autores_incollections = []
lista_publicaciones_incollections = []
lista_year_incollections = []
errors=[]

for incollection in incollections:
    try:
        lista_autores = []
        autores = incollection['author']
        if type(autores) != list:
            autores = []
            lista_autores.append(incollection['author'])

        for autor in autores:
            if '#text' in autor:
                autor = autor['#text']

            lista_autores.append(autor)

        lista_autores_incollections.append(lista_autores)

        publicacion = incollection['title']
        lista_publicaciones_incollections.append(publicacion)

        year = incollection['year']
        lista_year_incollections.append(year)
    except KeyError:
        errors.append(incollection)
        pass

print(errors[0])
clave='incollections'

valor={'autores_incollections':lista_autores_incollections,
       'publicaciones_incollections':lista_publicaciones_incollections,
       'years_incollections':lista_year_incollections}


insercion = {clave:valor}
print(type(insercion))

print('NÚMERO DE INCOLLECTIONES AL FINAL: ', len(lista_autores_incollections))
print('NÚMERO DE INCOLLECTIONES AL FINAL: ', len(lista_publicaciones_incollections))
print('NÚMERO DE INCOLLECTIONES AL FINAL: ', len(lista_year_incollections))


db.incollections.insert(insercion)


