movies = [("the matrix", "wachowski's", "1999", "3melyun")]

title = input("Enter the title of the movie: ")
director = input("Enter the director of the movie: ")
release_year = input("Enter the release year of the movie: ")
budget = input("Enter the budget of the movie: ")

movie = (title, director, release_year, budget)

print(f"{title} ({release_year})")

movies.append(movie)

print(movies[0])

del movies[0]

print(movies)

