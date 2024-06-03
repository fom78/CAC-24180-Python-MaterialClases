# Metodos magicos

class Movie:
    total_movies = 0

    def __init__(self, title, release_year, adult=False):
        self.title = title
        self.release_year = release_year
        self.adult = adult
        Movie.total_movies = Movie.total_movies + 1

    def __del__(self):
        # Método destructor que se llama cuando el objeto es destruido
        Movie.total_movies -= 1
        print(f"La película '{self.title}' ha sido eliminada.")

    def __str__(self):
        # Método especial para devolver una representación en forma de cadena del objeto
        return f"'{self.title}' (Año: {self.release_year}, Adulto: {'Sí' if self.adult else 'No'})"

    @classmethod
    def total_peliculas(cls):
        # Método de clase que accede a la clase en lugar de a la instancia
        return cls.total_movies

# Crear objetos de la clase Movie
movie1 = Movie("Inception", 2010)
movie2 = Movie("Toy Story", 1995, adult=False)

# Usar el método __str__
print(">>>>",movie1)  # Salida: 'Inception' (Año: 2010, Adulto: No)
print(">>>>",movie2)  # Salida: 'Toy Story' (Año: 1995, Adulto: No)

# Usar el método de clase
print("Total de películas:", Movie.total_peliculas())  # Salida: Total de películas: 2

# Eliminar un objeto para llamar al método __del__
del movie1  # Salida: La película 'Inception' ha sido eliminada.
print("Total de películas después de eliminar:", Movie.total_peliculas())  # Salida: Total de películas después de eliminar: 1
