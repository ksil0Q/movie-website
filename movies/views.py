from django.shortcuts import render
from .models import Movie
from django.views.generic.base import View


class MoviesView(View):
    """Movies list"""

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movie/movies_list.html", {'movies_list': movies})


class MovieDetailView(View):
    """Full description of the film"""

    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, "movie/movie_detail.html", {'movie': movie})
