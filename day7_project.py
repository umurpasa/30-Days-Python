movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

movie_add = input("Please enter a movie name and budget: ")

movies.append(tuple(movie_add.split(", ")))

# 1. Calculate the average budget of the movies 

total_budget = 0

for movie in movies:
    total_budget += movie[1]

average_budget = total_budget / len(movies)

print(f"Average budget of the movies: {average_budget}")

# 2. How many movies have a budget above average budget

count = 0

for movie in movies:
    if movie[1] > average_budget:
        print(f"{movie[0]} is {movie[1] - average_budget} above average budget.")
        count += 1

print(f"There are {count} movies above average budget.")



