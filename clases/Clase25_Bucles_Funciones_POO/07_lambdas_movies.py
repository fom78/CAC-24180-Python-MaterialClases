# Lista de películas con sus ratings
movies = [
    {"title": "Inception", "rating": 8.8},
    {"title": "Toy Story", "rating": 8.3},
    {"title": "Avatar", "rating": 7.8},
    {"title": "The Dark Knight", "rating": 9.0}
]

# Ordenar las películas por rating usando una función lambda
# La clave (key) para la ordenación es el valor de "rating" en cada diccionario de la lista
movies_sorted_by_rating = sorted(movies, key=lambda movie: movie["rating"], reverse=True)

# Mostrar las películas ordenadas por rating
print("Películas ordenadas por rating:", movies_sorted_by_rating)
# Salida: [{'title': 'The Dark Knight', 'rating': 9.0}, {'title': 'Inception', 'rating': 8.8}, {'title': 'Toy Story', 'rating': 8.3}, {'title': 'Avatar', 'rating': 7.8}]

# Calcular el rating promedio de las películas
ratings = list(map(lambda movie: movie["rating"], movies))
average_rating = sum(ratings) / len(ratings)
print("Rating promedio:", average_rating)  # Salida: Rating promedio: 8.475

# Filtrar las películas con rating mayor o igual a 8.5 usando una función lambda
high_rated_movies = list(filter(lambda movie: movie["rating"] >= 8.5, movies))
print("Películas con rating mayor o igual a 8.5:", high_rated_movies)
# Salida: Películas con rating mayor o igual a 8.5: [{'title': 'Inception', 'rating': 8.8}, {'title': 'The Dark Knight', 'rating': 9.0}]
