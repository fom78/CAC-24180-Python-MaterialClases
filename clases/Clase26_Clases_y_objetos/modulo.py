def lenCaserito (secuencia):
    """
    Return the number of items in a container.
    Hola clase!!! Comision campeona
    """
    contador = 0
    for iterable in secuencia:
        contador = contador + 1
    return contador


movies=[]

class Movie:
    # Atributos de clase (compartidos por todas las instancias)
    total_movies = 0

    def __init__(self, title, release_year, adult=False):
        self.title = title           
        self.release_year = release_year  
        self.adult = adult
        Movie.total_movies =Movie.total_movies + 1

    def obtener_titulo(self):
        # Este método devuelve el valor del atributo title de la instancia.
        return self.title.upper()
