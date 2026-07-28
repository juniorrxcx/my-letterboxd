from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('signup/', views.signup, name='signup'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('review/<int:review_id>/like/', views.toggle_like, name='toggle_like'),
    path('profile/<str:username>/', views.user_profile, name='user_profile'),
]