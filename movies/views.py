from django.shortcuts import render, redirect
from .models import Movie
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import ReviewForm


class MoviesView(View):
    """Movies list"""

    # model = Movie
    # queryset = Movie.objects.filter(draft=False)

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movie_list.html', {'movies_list': movies})


class MovieDetailView(DetailView):
    """Full description of the film"""

    model = Movie
    slug_field = 'url'

    # def get(self, request, slug):
    #     movie = Movie.objects.get(url=slug)
    #     return render(request, "movie/movie_detail.html", {'movie': movie})


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
