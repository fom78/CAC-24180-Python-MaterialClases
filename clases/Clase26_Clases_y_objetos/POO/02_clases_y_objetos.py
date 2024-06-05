# Clases, objetos y atributos
# Una clase es un plano para crear objetos. Un objeto es una instancia de una clase.
# Los atributos son variables que pertenecen a una clase o a los objetos creados a partir de la clase.

# Definición de la clase Movie
class Movie:
    # Atributos de clase (compartidos por todas las instancias)
    total_movies = 0

    def __init__(self, title, release_year, adult=False):
        self.title = title           
        self.release_year = release_year  
        self.adult = adult
        Movie.total_movies += 1

    def obtener_titulo(self):
        # Este método devuelve el valor del atributo title de la instancia.
        return self.title

# Crear objetos (instancias) de la clase Movie
movie1 = Movie("Inception", 2010)
movie2 = Movie("Toy Story", 1995, adult=False)

# Acceder a atributos de instancia
print("Título:", movie1.title)  # Salida: Título: Inception
print("Año de estreno:", movie2.release_year)  # Salida: Año de estreno: 1995

# Acceder a atributos de clase
print("Total de películas:", Movie.total_movies)  # Salida: Total de películas: 2
