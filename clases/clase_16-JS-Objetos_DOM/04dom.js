/*
Acceder a elementos:

- Acceder a un elemento por su id
const elemento = document.getElementById('mi-elemento');

- Acceder al primer elemento que coincida con un selector CSS
const elemento = document.querySelector('.mi-clase');

- Acceder a todos los elementos que tengan una clase específica
const elementos = document.getElementsByClassName('mi-clase');

- Acceder a todos los elementos de una etiqueta específica
const elementos = document.getElementsByTagName('p');
*/

/* 
Modificar contenido:
- Cambiar el contenido HTML de un elemento
elemento.innerHTML = '<p>Nuevo contenido HTML</p>';

- Cambiar el contenido de texto de un elemento
elemento.textContent = 'Nuevo texto';

*/

/* 
Modificar atributos
- Cambiar un atributo usando setAttribute()
elemento.setAttribute('id', 'nuevo-id');

- Cambiar un atributo accediendo directamente a la propiedad
elemento.id = 'nuevo-id';
*/
/*
Crear elementos
- Crear un nuevo elemento <p>
const nuevoParrafo = document.createElement('p')
*/

/*
Agregar elementos al DOM

- Agregar un elemento como hijo de otro
padre.appendChild(nuevoParrafo);

- Insertar un elemento antes de otro
padre.insertBefore(nuevoParrafo, elementoExistente);

- Insertar HTML en una posición específica
elemento.insertAdjacentHTML('beforeend', '<p>Nuevo contenido HTML</p>');

*/