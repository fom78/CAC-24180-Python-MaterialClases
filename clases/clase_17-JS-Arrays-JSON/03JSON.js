const pelis = 
`{
    "peliculas": [
      {
        "id": 1,
        "nombre": "El sexto sentido",
        "director": "M. Night Shyamalan",
        "clasificacion": "Drama"
      },
      {
        "id": 2,
        "nombre": "Pulp Fiction",
        "director": "Tarantino",
        "clasificacion": "Acción"
      },
      {
        "id": 3,
        "nombre": "Todo Sobre Mi Madre",
        "director": "Almodobar",
        "clasificacion": "Drama"
      },
      {
        "id": 4,
        "nombre": "300",
        "director": "Zack Snyder",
        "clasificacion": "Acción"
      },
      {
        "id": 5,
        "nombre": "El silencio de los corderos",
        "director": "Jonathan Demme",
        "clasificacion": "Drama"
      },
      {
        "id": 6,
        "nombre": "Forrest Gump",
        "director": "Robert Zemeckis",
        "clasificacion": "Comedia"
      },
      {
        "id": 7,
        "nombre": "Las Hurdes",
        "director": "Luis Buñuel",
        "clasificacion": "Documental"
      }
    ],
    "clasificaciones": [
      {
        "nombre": "Drama",
        "id": 1
      },
      {
        "nombre": "Comedia",
        "id": 2
      },
      {
        "nombre": "Documental",
        "id": 3
      },
      {
        "nombre": "Acción",
        "id": 4
      }
    ],
    "page": 3
  }`


const peliculasObjeto = JSON.parse(pelis)

console.log(peliculasObjeto,typeof(peliculasObjeto))
console.log(peliculasObjeto.peliculas.length)