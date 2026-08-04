from services.tmdb import (
    get_trending,
    search_movie,
    get_movie_details
)


print("\n🔥 TRENDING MOVIES\n")

trending = get_trending(5)

print(
    trending[
        ["title", "popularity", "vote_average"]
    ]
)


print("\n\n🔎 SEARCH BATMAN\n")

results = search_movie("Batman", 5)

print(
    results[
        ["title", "release_date", "vote_average"]
    ]
)


print("\n\n🎬 MOVIE DETAILS\n")

movie = get_movie_details(27205)

print(movie[
    [
        "title",
        "overview",
        "runtime",
        "vote_average"
    ]
])