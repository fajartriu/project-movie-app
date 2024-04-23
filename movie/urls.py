from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies, name='home'),
    path('movie_details/<int:id>', views.movieDetails, name='movieDetails'),
    # path('search/', views.get_context_data, name='searchMovie'),
]
