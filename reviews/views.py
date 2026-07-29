from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Movie, Review, Like
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, CustomSignupForm, ProfileUpdateForm

def movie_list(request):

    query = request.GET.get('q')
    
    if query:
        movies = Movie.objects.filter(title__icontains=query)
    else:
        movies = Movie.objects.all()
        
    return render(request, 'reviews/movie_list.html', {'movies': movies, 'query': query})

def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomSignupForm()
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

def user_profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    
    user_reviews = profile_user.reviews.all().order_by('-created_at')
    
    return render(request, 'reviews/user_profile.html', {
        'profile_user': profile_user,
        'user_reviews': user_reviews
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'reviews/edit_profile.html', {'form': form})