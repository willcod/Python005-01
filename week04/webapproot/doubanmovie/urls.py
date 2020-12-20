from django.urls import path
from . import views

app_name = 'doubanmovie'
urlpatterns = [
    path('', views.index, name='index'),
    path('comments/<int:movie_id>', views.comment, name='comment'),
]