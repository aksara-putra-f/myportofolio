from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("projects/", api_views.project_list, name="project_list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name='project_detail'),
    path("projects/<uuid:project_id>/stars/", api_views.project_star, name="project_star"),

    path("educations/", api_views.education_list, name="education_list"),
    path("educations/<uuid:education_id>/", api_views.education_detail, name="education_detail"),
]