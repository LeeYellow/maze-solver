from django.urls import path
from . import views

urlpatterns = [
    path("maze/new/", views.new_maze, name="new_maze"),
    path("maze/<int:pk>/", views.maze_detail, name="maze_detail"),
    path("api/maze/<int:pk>/", views.maze_api, name="maze_api"),
]