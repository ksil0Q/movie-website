from django.shortcuts import render
from .models import Movie
from django.views.generic.base import View


class MoviesView(View):
    """Movies list"""

    @staticmethod
    def get(request):
        movies = Movie.objects.all()
        return render(request, "movies/movies_list.html", {'movies_list': movies})
