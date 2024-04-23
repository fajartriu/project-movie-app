from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from movie.models import Movies
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
import json
# Create your views here.
def paginate_movies(request, movies_list):
    paginator = Paginator(movies_list, 8)
    page_number = request.GET.get('page')
    try:
        movies = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        movies = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results.
        movies = paginator.page(paginator.num_pages)
    return movies, page_number

def movies(request):
    # get requested movies
    search = request.GET.get('search')
    # if search is not empty
    if search:
        movies_list = Movies.objects.filter(name__icontains=search)
    else:
    # if search is empty
        movies_list = Movies.objects.all()
    # get movies and page numbers
    movies, page_number = paginate_movies(request, movies_list)
    context = {
        'movies': movies,
        'page_number': page_number,
        'search': search,
    }

    if search and not movies:
        return render(request, 'noResult.html', context)
    else:
        return render(request, 'home.html', context)

# def search(request):
#     if request.is_ajax():
#         movie = request.GET.get('movie')
#         print(movie)
#         return JsonResponse({'data': movie})
#     else:
#         print('gada')
#     return JsonResponse({})

def movieDetails(request, id):
    movie = get_object_or_404(Movies, pk=id)
    genres = movie.genre.all()
    return render(request, 'movieDetails.html', {'movie': movie, 'genres': genres})


# def get_context_data(request):
#     movies_data = list(Movies.objects.values())  # Ambil data dari model Movies
#     qs_json = json.dumps(movies_data)  # Serialize data menjadi JSON

#     context = {'qs_json': qs_json}  # Masukkan data JSON ke dalam context

#     return JsonResponse(context)  # Return response JSON dengan context