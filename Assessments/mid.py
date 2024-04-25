# Define a class to represent a movie
class Movie:
    def __init__(self, movie_id, title, director, year):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.year = year

# Function to perform case insensitive search on movies and print the results
def search_movies(movies, query):
    results = []
    for movie in movies:
        if query.lower() in movie.title.lower() or query.lower() in movie.director.lower():
            results.append(movie)
    return results

# Main function to input movies and perform search
def main():
    movies = []
    
    # Input movies until "STOP" is entered
    while True:
        movie_info = input()
        if movie_info == "STOP":
            break
        else:
            movie_id, title, director, year = movie_info.split(";")
            movie = Movie(movie_id, title, director, year)
            movies.append(movie)
    
    # Perform search
    query = input()
    results = search_movies(movies, query)
    
    # Print results
    for movie in results:
        print(f"{movie.movie_id};{movie.title};{movie.director};{movie.year}")

if __name__ == "__main__":
    main()
