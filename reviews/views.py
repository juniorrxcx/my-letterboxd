from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Movie, Review, Like
from .forms import ReviewForm

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


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    reviews = movie.reviews.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie = movie
                review.user = request.user 
                review.save()
                return redirect('movie_detail', movie_id=movie.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'form': form
    })

def toggle_like(request, review_id):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, id=review_id)
        
        like = Like.objects.filter(user=request.user, review=review).first()
        
        if like:
            like.delete()
        else:
            Like.objects.create(user=request.user, review=review)
            
        return redirect('movie_detail', movie_id=review.movie.id)
        
    return redirect('login')