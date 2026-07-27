from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    synopsis = models.TextField()
    poster = models.ImageField(upload_to='movies/posters/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.release_year})"

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    
    #review de 1 a 5
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} ({self.rating}/5)"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'review')

    def __str__(self):
        return f"{self.user.username} curtiu a review de {self.review.user.username}"