from django.contrib import admin
from movie.models import Movies, Genres

# Register your models here.
class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'genre')
    search_fields = ('genre',)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'imgPath', 'duration', 'get_genres_display', 'language', 'mpaaRatingTypto', 'mpaaRatingLabel', 'userRating')
    list_filter = ('language', 'userRating')
    search_fields = ('name', 'description')
    
    def get_genres_display(self, obj):
        return ", ".join([genre.genre for genre in obj.genre.all()])
    get_genres_display.short_description = 'Genres'

# Register models
admin.site.register(Genres, GenresAdmin)
admin.site.register(Movies, MoviesAdmin)