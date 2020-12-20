from django.shortcuts import render
from .models import Movie, Comment

# Create your views here.
def index(request):
    """The home page"""
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'doubanmovie/index.html', context)

def comment(request, movie_id):
    """The comments page"""
    movie = Movie.objects.get(Id = movie_id)

    comments = Comment.objects.filter(movie_id = movie_id, rate__gt = 30)
    context = {'movie': movie.title, 'comments': comments}
    return render(request, 'doubanmovie/comment.html', context)