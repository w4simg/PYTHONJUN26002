# Task 10: Create a Movie Class
# Requirements:
# - Store: movie name, hero name, release year.
# - Use a constructor.
# - Create a display method.

class Movie:
    def __init__(self, name, hero, release_year):
        self.name = name
        self.hero = hero
        self.release_year = release_year

    def display(self):
        print("Movie Details:")
        print("Movie Name:", self.name)
        print("Hero:", self.hero)
        print("Release Year:", self.release_year)

# Create object
movie1 = Movie("Inception", "Leonardo DiCaprio", 2010)

# Display details
movie1.display()
