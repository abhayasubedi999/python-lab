# Get input of list of movies that was released in 2025. Also get input of movies watched by user (any year). Display following.​

# Movies of 2025 that are watched by user​

# Movies of 2025 that are yet to be watched by user​

# Total list of movies watched by user combining to movies of 2025

list_of_movies_released_in_2025 = {"rrr", "kgf", "titanic", "buried in barstow"}
movie_watched_by_user = set(
    input("enter the movie you watched separated by comma: ").split(",")
)


print(f"Movie Watched: {list_of_movies_released_in_2025 & movie_watched_by_user}")
print(f"Movie To watch: {list_of_movies_released_in_2025 - movie_watched_by_user}")
print(f"Total: {list_of_movies_released_in_2025 | movie_watched_by_user}")
