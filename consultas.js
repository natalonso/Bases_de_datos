db.getCollection('collection_articles').find({})

db.collection_incollections.aggregate([
    {$count:"Total_Incollections"},
    {$project:{_id:"$Total_Incollections"}}
    ])
    
db.collection_inproceedings.aggregate([
    {$count:"Total_Inproceedings"},
    {$project:{_id:"$Total_Inproceedings"}}
    ])
    
db.collection_articles.aggregate([
    {$count:"Total_Artículos"},
    {$project:{_id:"$Total_Artículos"}}
    ])

/* 1. Listado de todas las publicaciones de un autor determinado. */

db.collection_incollections.aggregate([
    {$match:{authors:"Robert Demolombe"}},
    {$project:{_id:"$title"}}
    ])
    
db.collection_inproceedings.aggregate([
    {$match:{authors:"Robert Demolombe"}},
    {$project:{_id:"$title"}}
    ])
    
db.collection_articles.aggregate([
    {$match:{authors:"Robert Demolombe"}},
    {$project:{_id:"$title"}}
    ])


/* 2. Número de publicaciones de un autor determinado. */

db.collection_incollections.aggregate([
    {$match:{authors:"Robert Demolombe"}},
    {$count:"Numero_incollections"},
    {$project:{_id:"$Numero_incollections"}}
    ])
    
db.collection_inproceedings.aggregate([
    {$match:{authors:"Robert Demolombe"}},
    {$count:"Numero_inproceedings"},
    {$project:{_id:"$Numero_inproceedings"}}
    ])
    
db.collection_articles.aggregate([
    {$match:{authors:"Robert Demolombe"}},
    {$count:"Numero_articles"},
    {$project:{_id:"$Numero_articles"}}
    ])

/* 3. Número de artículos en revista para el año 2018. */

db.collection_articles.aggregate([
    {$match:{year:"2018"}},
    {$count:"Numero_articles_2018"},
    {$project:{_id:"$Numero_articles_2018"}}
    ])


/* 4. Número de autores ocasionales, es decir, que tengan menos de 5 publicaciones en total. */
    
db.collection_incollections.aggregate([
    {$unwind:"$authors"},
    {$sortByCount:"$authors"},
    {$match:{count: {$lt: 5}}},
    {$count:"Número_autores_con_menos_de_5_publicaciones"},
    {$project:{_id:"$Número_autores_con_menos_de_5_publicaciones"}}
    ])

    
/* 5. Número de artículos de revista (article) y número de artículos en congresos (inproceedings) de los diez autores con más publicaciones totales. */

/* 6. Número medio de autores de todas las publicaciones que tenga en su conjunto de datos. */

/* 7. Listado de coautores de un autor (Se denomina coautor a cualquier persona que haya firmado una publicación). */

/* 8. Edad de los 5 autores con un periodo de publicaciones más largo (Se considera la Edad de un autor al número de años transcurridos 
desde la fecha de su primera publicación hasta la última registrada). */

/* 9. Número de autores novatos, es decir, que tengan una Edad menor de 5 años. Se considera la Edad de un autor 
al número de años transcurridos desde la fecha de su primera publicación hasta la última registrada. */

/* 10. Porcentaje de publicaciones en revistas con respecto al total de publicaciones. */


