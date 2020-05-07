
db.collection_publication.createIndex({authors:1})

/* 1. Listado de todas las publicaciones de un autor determinado. */
    
db.collection_publication.aggregate([
    {$match:{authors:"Robert Demolombe"}},
    {$project:{_id:"$title"}}
    ])

/* 2. Número de publicaciones de un autor determinado. */

db.collection_publication.aggregate([
    {$match:{authors:"Robert Demolombe"}},
    {$count:"Numero_publicaciones"},
    {$project:{_id:"$Numero_publicaciones"}}
    ])

/* 3. Número de artículos en revista para el año 2018. */

db.collection_publication.aggregate([
    {$match:{type:"article"}},
    {$match:{year:2018}},
    {$count:"Numero_articles_2018"},
    {$project:{_id:"$Numero_articles_2018"}}
    ])

/* 4. Número de autores ocasionales, es decir, que tengan menos de 5 publicaciones en total. */

db.collection_publication.aggregate([
    {$unwind:"$authors"},
    {$sortByCount:"$authors"},
    {$match:{count: {$lt: 5}}},
    {$count:"Número_autores_con_menos_de_5_publicaciones"},
    {$project:{_id:"$Número_autores_con_menos_de_5_publicaciones"}}
    ],{allowDiskUse:true})
    
/* 5. Número de artículos de revista (article) de los diez autores con más publicaciones totales. */
/* Cambiar el nombre de los counts, ver si se puede optimmizar el número de pasos o de tablas */
    
db.collection_publication.aggregate([
    {$unwind:"$authors"},
    {$sortByCount:"$authors"},
    {$limit:10},
    {$out:"Top10_autores"}
    ],{allowDiskUse:true})

db.collection_publication.aggregate([
    {$match:{type:"article"}},
    {$unwind:"$authors"},
    {$sortByCount:"$authors"},
    {$out:"Autores_articles"}
    ],{allowDiskUse:true})
    
db.Top10_autores.aggregate([
    {$lookup:{
        from : "Autores_articles",
        localField : "_id",
        foreignField : "_id",
        as : "Número_artículos"}},
    {$unwind:"$Número_artículos"}
    ],{allowDiskUse:true})
    
/* y número de artículos en congresos (inproceedings) de los diez autores con más publicaciones totales. */
    
db.collection_publication.aggregate([
    {$match:{type:"inproceeding"}},
    {$unwind:"$authors"},
    {$sortByCount:"$authors"},
    {$out:"Autores_inproceeding"}
    ],{allowDiskUse:true})
    
db.Top10_autores.aggregate([
    {$lookup:{
        from : "Autores_inproceeding",
        localField : "_id",
        foreignField : "_id",
        as : "Número_inproceeding"}},
    {$unwind:"$Número_inproceeding"}
    ],{allowDiskUse:true})
    
/* 6. Número medio de autores de todas las publicaciones que tenga en su conjunto de datos. */

db.collection_publication.aggregate([
    {$unwind:"$authors"},
    {$sortByCount:"$_id"},
    {$group:{
        _id: null,
        Media: {$avg: "$count"}}},
    {$project: {_id : "$Media"}}
    ],{allowDiskUse:true})

/* 7. Listado de coautores de un autor (Se denomina coautor a cualquier persona que haya firmado una publicación). */

db.collection_publication.aggregate([
    {$match:{authors:"Robert Demolombe"}},
    {$project: {"Co-autores" : "$authors"}},
    {$unwind:"$Co-autores"},
    {$sortByCount:"$Co-autores"},
    {$match:{_id : {$ne : "Robert Demolombe"}}},
    ])
    
/* 8. Edad de los 5 autores con un periodo de publicaciones más largo (Se considera la Edad de un autor al número de años transcurridos 
desde la fecha de su primera publicación hasta la última registrada). */

db.collection_publication.aggregate([
    {$unwind:"$authors"},
    {$group: {
        _id: "$authors",
        Minimo: { $min: "$year" },  
        Maximo: { $max: "$year" }}},
     {$addFields:{Edad: { $subtract: ["$Maximo", "$Minimo"] }}},
     {$sort: {"Edad" : -1}},
     {$limit: 5}
     ],{allowDiskUse:true})
    
/* 9. Número de autores novatos, es decir, que tengan una Edad menor de 5 años. Se considera la Edad de un autor 
al número de años transcurridos desde la fecha de su primera publicación hasta la última registrada. */

     
db.collection_publication.aggregate([
    {$unwind:"$authors"},
    {$group: {
        _id: "$authors",
        Minimo: { $min: "$year" },  
        Maximo: { $max: "$year" }}},
     {$addFields:{ Edad: { $subtract: ["$Maximo", "$Minimo"] }}},
     {$match:{Edad: {$lt: 5}}},
     {$count : "Número_autores_novatos"},
     {$project : {_id: "$Número_autores_novatos"}}
     ],{allowDiskUse:true})


/* 10. Porcentaje de publicaciones en revistas con respecto al total de publicaciones. */

db.collection_publication.aggregate([
     {$facet:
         {
             "Numero_articulos": [{$match:{type:"article"}}, {$count:"Num_articles"}],
             "Numero_total": [ {$count : "Num_total"}]
         }
     },
     {$unwind:"$Numero_articulos"},
     {$unwind:"$Numero_total"},
     {$addFields:{ Porcentaje: { $divide: ["$Numero_articulos.Num_articles", "$Numero_total.Num_total"] }}}
     ],{allowDiskUse:true})
     


