from django.http import HttpResponse # only used in class (see comment below)
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Movie, Director
from .forms import MovieForm

# Create your views here.
def home(request):
    return render(request, 'movies/home.html')

def movie_list(request):
    all_movies = Movie.objects.all()
    context = {
        'movies': all_movies,
    }
    return render(request, 'movies/movie_list.html', context)

def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/movie_details.html', context)

def movie_form(request):
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            # validate etc here....
            # use movie_form.cleaned_data['field_name']
            movie_form.save()
            return redirect(reverse('movies:home'))
    else:  # unbound
        movie_form = MovieForm()
        context = {
            'movie_form': movie_form
        }
        return render(request, 'movies/movie_form.html', context)


# example without template (only used in class -- always use templates in real life):
# def home(request):
#     return HttpResponse("Welcome to Awesome Movies!")

# example with template (normal Django approach)
# def home(request):
#     context = { 'message': "Welcome to Awesome Movies!" }
#     return render(request, 'movies/home.html', context)
