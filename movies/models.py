from django.db import models
from datetime import date


class Category(models.Model):
    """Categories model for db"""
    name = models.CharField('Category', max_length=150)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    """Actors model for db"""
    name = models.CharField('Actor', max_length=150)
    description = models.TextField('Description')
    age = models.PositiveSmallIntegerField('Age', default=0)
    image = models.ImageField('Image', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actors & Directors'
        verbose_name_plural = 'Actors & Directors'


class Genre(models.Model):
    """Genre model for db"""
    name = models.CharField('Genre', max_length=150)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    """Movie model for db"""
    title = models.CharField('Title', max_length=100)
    tag = models.CharField('Tagline', max_length=100, default='')
    description = models.TextField('Description')
    poster = models.ImageField('Poster', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Release date', default=date.today)
    country = models.CharField('Country', max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name='Director',
                                       related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Actors',
                                    related_name='film_actors')
    genres = models.ManyToManyField(Genre, verbose_name='Genres')
    world_premiere = models.DateField('World premiere date',
                                      default=date.today)
    budget = models.PositiveIntegerField('Budget', default=0,
                                         help_text='Specify the amount in dollars')
    fees_in_Russia = models.PositiveIntegerField(
        'Fees in Russia', default=0, help_text='Specify the amount in dollars')
    fees_in_world = models.PositiveIntegerField(
        'Fees in World', default=0, help_text='Specify the amount in dollars')
    category = models.ForeignKey(
        Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class MovieShots(models.Model):
    """Movie shots model for db"""
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Film',
                              on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie shot'
        verbose_name_plural = 'Movie shots'


class RatingStar(models.Model):
    """Rating star model for db"""
    value = models.PositiveSmallIntegerField('Value', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Rating star'
        verbose_name_plural = 'Rating stars'


class Rating(models.Model):
    """Rating model for db"""
    user_ip = models.CharField('User IP', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE,
                             verbose_name='Star')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              verbose_name='Film')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class Reviews(models.Model):
    """Reviews model for db"""
    email = models.EmailField()
    name = models.CharField('User name', max_length=100)
    text = models.TextField('Review', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Parent', on_delete=models.SET_NULL,
        blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name='Film',
                              on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
