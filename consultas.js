

db.collection_publication.aggregate([
    {$count:"Total_Publicaciones"},
    {$project:{_id:"$Total_Publicaciones"}}
    ])
    

/* 1. Listado de todas las publicaciones de un autor determinado. */
    
db.collection_publication.aggregate([
    {$match:{authors:"Robert Demolombe"}},
    {$project:{_id:"$title"}}
    ])


/* 2. N�mero de publicaciones de un autor determinado. */

db.collection_publication.aggregate([
    {$match:{authors:"Robert Demolombe"}},
    {$count:"Numero_publicaciones"},
    {$project:{_id:"$Numero_publicaciones"}}
    ])
    

/* 3. N�mero de art�culos en revista para el a�o 2018. */

db.collection_publication.aggregate([
    {$match:{type:"article"}},
    {$match:{year:"2018"}},
    {$count:"Numero_articles_2018"},
    {$project:{_id:"$Numero_articles_2018"}}
    ])


/* 4. N�mero de autores ocasionales, es decir, que tengan menos de 5 publicaciones en total. */

db.collection_publication.aggregate([
    {$unwind:"$authors"},
    {$sortByCount:"$authors"},
    {$count:"N�mero_autores_con_menos_de_5_publicaciones"},
    {$match:{count: {$lt: 5}}},
    {$count:"N�mero_autores_con_menos_de_5_publicaciones"},
    {$project:{_id:"$N�mero_autores_con_menos_de_5_publicaciones"}}
    ])
    
/* 5. N�mero de art�culos de revista (article) y n�mero de art�culos en congresos (inproceedings) de los diez autores con m�s publicaciones totales. */

/* 6. N�mero medio de autores de todas las publicaciones que tenga en su conjunto de datos. */

/* 7. Listado de coautores de un autor (Se denomina coautor a cualquier persona que haya firmado una publicaci�n). */

/* 8. Edad de los 5 autores con un periodo de publicaciones m�s largo (Se considera la Edad de un autor al n�mero de a�os transcurridos 
desde la fecha de su primera publicaci�n hasta la �ltima registrada). */

/* 9. N�mero de autores novatos, es decir, que tengan una Edad menor de 5 a�os. Se considera la Edad de un autor 
al n�mero de a�os transcurridos desde la fecha de su primera publicaci�n hasta la �ltima registrada. */

/* 10. Porcentaje de publicaciones en revistas con respecto al total de publicaciones. */


