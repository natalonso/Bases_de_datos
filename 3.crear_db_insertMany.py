
import pymongo
from pymongo import MongoClient
import json


##########################################################
# INCOLLECTIONS
##########################################################

with open('./incollections.json', encoding='utf-8') as f:
    incollections = json.load(f)

lista_documentos_dict = []
for publicacion in incollections:
    documento_dict = {}
    autores_insert = []
    try:
        autores = publicacion['author']
        if type(autores) != list:
            autores = []
            autores.append(publicacion['author'])

        for autor in autores:
            if '#text' in autor:
                autor = autor['#text']
            autores_insert.append(autor)

        documento_dict['authors'] = autores_insert
        documento_dict['title'] = publicacion['title']
        documento_dict['year'] = publicacion['year']

        lista_documentos_dict.append(documento_dict)

    except KeyError:
        pass

conection = pymongo.MongoClient()
db = conection.prueba_dblp
collection = db.collection_incollections
collection.insert_many(lista_documentos_dict)
conection.close()
print('Número total de incollections: ', len(lista_documentos_dict))

##########################################################
# INPROCEEDINGS:
##########################################################

with open('./inproceedings.json', encoding='utf-8') as f:
    inproceedings = json.load(f)

lista_documentos_dict = []
for publicacion in inproceedings:
    documento_dict = {}
    autores_insert = []
    try:
        autores = publicacion['author']
        if type(autores) != list:
            autores = []
            autores.append(publicacion['author'])

        for autor in autores:
            if '#text' in autor:
                autor = autor['#text']
            autores_insert.append(autor)

        documento_dict['authors'] = autores_insert
        documento_dict['title'] = publicacion['title']
        documento_dict['year'] = publicacion['year']

        lista_documentos_dict.append(documento_dict)

    except KeyError:
        pass

conection = pymongo.MongoClient()
db = conection.prueba_dblp
collection = db.collection_inproceedings
collection.insert_many(lista_documentos_dict)
conection.close()
print('Número total de inproceedings: ', len(lista_documentos_dict))


##########################################################
# ARTICLES:
##########################################################

with open('./articles.json', encoding='utf-8') as f:
    articles = json.load(f)

lista_documentos_dict = []
for publicacion in articles:
    documento_dict = {}
    autores_insert = []
    try:
        autores = publicacion['author']
        if type(autores) != list:
            autores = []
            autores.append(publicacion['author'])

        for autor in autores:
            if '#text' in autor:
                autor = autor['#text']
            autores_insert.append(autor)

        documento_dict['authors'] = autores_insert
        documento_dict['title'] = publicacion['title']
        documento_dict['year'] = publicacion['year']

        lista_documentos_dict.append(documento_dict)

    except KeyError:
        pass

conection = pymongo.MongoClient()
db = conection.prueba_dblp
collection = db.collection_articles
collection.insert_many(lista_documentos_dict)
conection.close()
print('Número total de articles: ', len(lista_documentos_dict))



print('terminado')