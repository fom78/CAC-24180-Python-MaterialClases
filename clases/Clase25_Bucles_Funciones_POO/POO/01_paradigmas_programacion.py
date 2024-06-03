# Paradigmas de programación
# La programación estructurada se basa en la división de un programa en funciones y módulos. 
# En cambio, la Programación Orientada a Objetos (POO) organiza el código en objetos que combinan datos y comportamiento.

class Persona():
    nom=""
    edad=0

per1 = Persona()
print(">>>>>",per1.edad)

# Definición de la clase Movie
class Movie:
    # El método __init__ es el constructor de la clase.
    # Se llama automáticamente cuando se crea una nueva instancia de Movie.
    def __init__(self, title, release_year, adult=False):
        # Se definen los atributos de la instancia (objetos).
        # 'self' es una referencia a la instancia actual del objeto.
        self.title = title           # Se asigna el parámetro title al atributo de instancia self.title.
        self.release_year = release_year  # Se asigna el parámetro release_year al atributo de instancia self.release_year.
        self.adult = adult
    # Definición de un método de instancia.
    # Los métodos son funciones que pertenecen a una clase.
    def obtener_titulo(self):
        # Este método devuelve el valor del atributo title de la instancia.
        return self.title

# Ejemplo de uso de la clase Movie:

# Crear una nueva instancia de Movie
mi_pelicula = Movie("Inception", 2010)

# Llamar al método obtener_titulo() para obtener el título de la película
titulo = mi_pelicula.obtener_titulo()

# Imprimir el título de la película
print("El título de la película es:", titulo)
if mi_pelicula.adult:
    print("Es para adultos")
else:
    print("Apta todo publico")

