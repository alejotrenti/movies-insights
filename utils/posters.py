POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500"


POSTERS = {
    19995: "/6EiRUJpuoeQPghrs3YNktfnqOVh.jpg",  # Avatar
    157336: "/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg", # Interstellar
    293660: "/zq8Cl3PNIDGU3iWNRoc5nEZ6pCe.jpg", # Deadpool
    118340: "/y31QB9kn3XSudA15tV7UWQ9XLu.jpg", # Guardians
    76341: "/8tZYtuWezp8JbcsvHYO0O46tFbo.jpg"  # Mad Max
}


def get_poster(movie_id):

    poster_path = POSTERS.get(int(movie_id))

    if poster_path:
        return f"{POSTER_BASE_URL}{poster_path}"

    return "https://placehold.co/300x450?text=No+Poster"