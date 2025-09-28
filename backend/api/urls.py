from django.urls import path
from . import views

urlpatterns = [
    path("team/", views.CreateTeamView.as_view(), name="team-list"),
    path("team/delete/<int:pk>/", views.DeleteTeamView.as_view(), name="delete-team"),
]