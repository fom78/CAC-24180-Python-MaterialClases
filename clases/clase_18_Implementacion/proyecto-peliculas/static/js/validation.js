
// Haremos algunas validaciones, pero antes practicaremos

// Agregar un texto (2024) al lado  del corazon ❤️
const h2Anio = document.querySelector('h2') 

h2Anio.insertAdjacentText('beforeend','2024')

/*
- Implementar una funcion para validar el formulario
- validar el nombre no vacio
- validar al enviar
- Dar un feedback del error

*/ 

const validarFormulario= (evento) => {
    evento.preventDefault()
    const primerNombre = document.getElementById("firstname")
    const divErrorPrimerNombre = document.querySelector("#error-firstname")
    divErrorPrimerNombre.innerHTML = ""

    if (primerNombre.value === "") {
        
        divErrorPrimerNombre.insertAdjacentText("afterbegin","El nombre no puede ser vacio!!!")
    }

    // password
    const clave = document.getElementById("password")
    const divErrorClave = document.querySelector("#error-password")
    divErrorClave.innerHTML = ""
    
    if (clave.value.length < 6) {
        
        divErrorClave.insertAdjacentText("afterbegin","La pass debe superar los 6 caracteres ")
    }
}

// agregar el listener al formulario

const formularioRegistro = document.querySelector("#formRegister")
formularioRegistro.addEventListener('submit',validarFormulario)