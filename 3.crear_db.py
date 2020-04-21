import pymongo
from pymongo import MongoClient
import json

with open('./incollections.json', encoding='utf-8') as f:
    incollections = json.load(f)

with open('./inproceedings.json', encoding='utf-8') as f:
    inproceedings = json.load(f)

with open('./articles.json', encoding='utf-8') as f:
    articles = json.load(f)

publicaciones = [incollections, inproceedings, articles]

lista_autores = []

for tipo_publicacion in publicaciones:
    for publicacion in tipo_publicacion:
        try:
            autores = publicacion['author']
            if type(autores) != list:
                autores = []
                autores.append(publicacion['author'])

            for autor in autores:
                if '#text' in autor:
                    autor = autor['#text']

                lista_autores.append(autor)
        except KeyError:
            pass


lista_autores_set=list(set(lista_autores))
print(len(lista_autores_set))

conex = pymongo.MongoClient()
db = conex.prueba_dblp
col = db.prueba_collection_authors

lista_co_autores_incollections = []
lista_year_incollections = []
lista_publicaciones_incollections = []

lista_co_autores_inproceedings = []
lista_year_inproceedings = []
lista_publicaciones_inproceedings = []

lista_co_autores_articles = []
lista_year_articles = []
lista_publicaciones_articles = []

lista_autores_all = []

for autor_prueba in lista_autores_set[0:20]:

    print('Autor: ', autor_prueba)
    lista_autores_all.append(autor_prueba)

    ####################################################################################
    # INCOLLECTIONS:
    ####################################################################################

    for incollection in incollections:
        try:
            autores = incollection['author']
            if type(autores) != list:
                autores=[]
                autores.append(incollection['author'])

            for autor in autores:
                if '#text' in autor:
                    autor = autor['#text']
                if autor == autor_prueba:
                    publicacion = incollection['title']
                    year = incollection['year']
                    co_autores = incollection['author']
                    co_autores_limpios = []

                    if type(co_autores) == list:
                        for co_autor in co_autores:
                            if '#text' in co_autor:
                                co_autor = co_autor['#text']
                            co_autores_limpios.append(co_autor)
                        co_autores_limpios.remove(autor_prueba)

                    lista_co_autores_incollections.append(co_autores_limpios)
                    lista_year_incollections.append(year)
                    lista_publicaciones_incollections.append(publicacion)

        except KeyError:
            pass

    ####################################################################################
    # INPROCEEDINGS:
    ####################################################################################

    for inproceeding in inproceedings:
        try:
            autores = inproceeding['author']
            if type(autores) != list:
                autores = []
                autores.append(inproceeding['author'])

            for autor in autores:
                if '#text' in autor:
                    autor = autor['#text']
                if autor == autor_prueba:
                    publicacion = inproceeding['title']
                    year = inproceeding['year']
                    co_autores = inproceeding['author']
                    co_autores_limpios = []

                    if type(co_autores) == list:
                        for co_autor in co_autores:

                            if '#text' in co_autor:
                                co_autor = co_autor['#text']
                            co_autores_limpios.append(co_autor)

                        co_autores_limpios.remove(autor_prueba)

                    lista_co_autores_inproceedings.append(co_autores_limpios)
                    lista_year_inproceedings.append(year)
                    lista_publicaciones_inproceedings.append(publicacion)

        except KeyError:
            pass

    ####################################################################################
    # ARTICLES:
    ####################################################################################


    for article in articles:
        try:
            autores = article['author']
            if type(autores) != list:
                autores = []
                autores.append(article['author'])

            for autor in autores:
                if '#text' in autor:
                    autor = autor['#text']
                if autor == autor_prueba:
                    publicacion = article['title']
                    if '#text' in publicacion:
                        publicacion = publicacion['#text']
                    year = article['year']
                    co_autores = article['author']
                    co_autores_limpios = []

                    if type(co_autores) == list:
                        for co_autor in co_autores:
                            if '#text' in co_autor:
                                co_autor = co_autor['#text']
                            co_autores_limpios.append(co_autor)
                        co_autores_limpios.remove(autor_prueba)

                    lista_co_autores_articles.append(co_autores_limpios)
                    lista_year_articles.append(year)
                    lista_publicaciones_articles.append(publicacion)

        except KeyError:
            pass


clave=lista_autores_all

valor={'lista_autores': lista_autores,
       'co_autores_incollections':lista_co_autores_incollections,
       'publicaciones_incollections':lista_publicaciones_incollections,
       'years_incollections':lista_year_incollections}

db.prueba_collection_authors.insert({clave:valor})
conex.close()