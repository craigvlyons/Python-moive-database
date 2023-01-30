from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a movie, 
- 'l' to see your movies, 
- 's' mark movie as seen, 
- 'q' to quit

Your choice: """

# - add movie to list
def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    
    database.add_movie(title, director)


# - listing movies
def show_movies():
    movies = database.get_all_movies()
    for movie in movies:
        seen = 'Yes' if movie['seen'] else 'NO'
        print(f"Movie: {movie['name']}, Director: {movie['director']}, Seen: {seen}")


# - change movie to seen
def seen_movie():
    search_title = input("Enter movie title you have seen: ")
    database.mark_movie_as_seen(search_title)

# - Delete movie
def delete():
    search_title = input("Enter movie title you would like to delete: ")
    database.delete(search_title)

# dictionary for user options.
user_options = {
    "a": add_movie,
    "l": show_movies,
    "s": seen_movie,
    "d": delete,
}


def menu():    
    database.create_movie_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        # checks user options dictionary 
        if user_input in user_options:
            # returns the dictionary value
            selected_function = user_options[user_input]
            # add brackets to return option for function name.
            selected_function()
        else:
            print('Unknown command. Please try again.')

        user_input = input(USER_CHOICE)


menu()