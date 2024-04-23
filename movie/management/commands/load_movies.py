import json
from django.core.management.base import BaseCommand
import os
from movie.models import Genres, Movies

class Command(BaseCommand):
    help = 'Load data from JSON file'
    def handle(self, *args,  **optional):
        # read json data
        with open(os.path.join('movie', 'management', 'commands', 'movies.json')) as filename:
            movies_data = json.load(filename)
            genre_set = set()

            # save movies and gather unique genres
            for movie in movies_data:
                movie_save = Movies(
                    id = movie['id'],
                    name = movie['name'],
                    description = movie['description'],
                    imgPath = movie['imgPath'],
                    duration = movie['duration'],
                    language = movie['language'],
                    mpaaRatingTypto = movie['mpaaRating']['type'],
                    mpaaRatingLabel = movie['mpaaRating']['label'],
                    userRating = movie['userRating']
                )
                movie_save.save()
                for genre in movie['genre']:
                    genre = genre.strip().replace("'", "").replace('"', "").replace(',', "")
                    genre_set.add(genre)

        # save unique genres
        for i, genre in enumerate(sorted(genre_set), start=1):
            genreSave = Genres(
                id = i,
                genre = genre
            )
            genreSave.save()

        # save movies and genres
        for movie in movies_data:
            dataMovie, create = Movies.objects.get_or_create(name=movie['name'])
            for genre in movie['genre']:
                genre = genre.strip().replace("'", "").replace('"', "").replace(',', "")
                dataGenre = Genres.objects.filter(genre=genre).values()
                dataMovie.genre.add(dataGenre[0]['id'])

        self.stdout.write(self.style.SUCCESS('Movies data loaded successfully'))    
            
    
        