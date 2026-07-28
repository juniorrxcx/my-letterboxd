from django.contrib import admin
from .models import Movie, Review, Like, Profile

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year')
    search_fields = ('title',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Like)
admin.site.register(Profile)