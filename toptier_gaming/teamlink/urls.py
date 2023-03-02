from django.urls import path
from . import views


app_name = "teamlink"
urlpatterns = [
    path('', views.team_post_list, name="team_post_list"),
    path("<int:id>/", views.team_post_detail, name="team_post_detail"),
]
