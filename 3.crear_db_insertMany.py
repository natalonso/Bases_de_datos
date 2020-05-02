
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

        documento_dict['type'] = 'incollection'
        documento_dict['authors'] = autores_insert
        documento_dict['title'] = publicacion['title']
        documento_dict['year'] = publicacion['year']

        lista_documentos_dict.append(documento_dict)

    except KeyError:
        pass


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

        documento_dict['type'] = 'inproceeding'
        documento_dict['authors'] = autores_insert
        documento_dict['title'] = publicacion['title']
        documento_dict['year'] = publicacion['year']

        lista_documentos_dict.append(documento_dict)

    except KeyError:
        pass


##########################################################
# ARTICLES:
##########################################################

with open('./articles.json', encoding='utf-8') as f:
    articles = json.load(f)


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

        documento_dict['type'] = 'article'
        documento_dict['authors'] = autores_insert
        documento_dict['title'] = publicacion['title']
        documento_dict['year'] = publicacion['year']

        lista_documentos_dict.append(documento_dict)

    except KeyError:
        pass

conection = pymongo.MongoClient()
db = conection.prueba_dblp
collection = db.collection_publication
collection.insert_many(lista_documentos_dict)
conection.close()

print('Número total de publicaciones: ', len(lista_documentos_dict))
print('terminado')