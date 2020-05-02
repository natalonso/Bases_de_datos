
import pymongo
from pymongo import MongoClient
import json


def load_publication(lista, type_publication):
    lista_documentos_dict = []
    for publicacion in lista:
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

            documento_dict['type'] = type_publication
            documento_dict['authors'] = autores_insert
            documento_dict['title'] = publicacion['title']
            documento_dict['year'] = publicacion['year']

            lista_documentos_dict.append(documento_dict)

        except KeyError:
            pass
    return lista_documentos_dict

if __name__ == "__main__":
    with open('./incollections.json', encoding='utf-8') as f:
        incollections = json.load(f)

    with open('./inproceedings.json', encoding='utf-8') as f:
        inproceedings = json.load(f)

    with open('./articles.json', encoding='utf-8') as f:
        articles = json.load(f)

    type_p="incollection"
    lista_incollections = load_publication(incollections, type_p)
    print('Número total de publicaciones: ', len(lista_incollections))

    type_p = "inproceeding"
    lista_inproceedings = load_publication(inproceedings, type_p)
    print('Número total de publicaciones: ', len(lista_inproceedings))

    type_p="article"
    lista_articles = load_publication(articles, type_p)
    print('Número total de publicaciones: ', len(lista_articles))

    conection = pymongo.MongoClient()
    db = conection.prueba_dblp
    collection = db.collection_publication
    collection.insert_many(lista_incollections)
    collection.insert_many(lista_inproceedings)
    collection.insert_many(lista_articles)
    conection.close()

    print('terminado')