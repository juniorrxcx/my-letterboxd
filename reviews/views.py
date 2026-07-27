from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all().order_by('-release_year')
    return render(request, 'reviews/movie_list.html', {'movies': movies})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})