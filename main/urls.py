from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),

    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("api/experiences/", get_experience_json, name="get_experience_json"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),

    path("project/", show_project, name="show_project"),
    path("project/add/", create_project, name="create_project"),
    path("api/projects/", get_project_json, name="get_project_json"),
    path("project/<uuid:project_id>/delete/", delete_project, name="delete_project"),

    path("skill/", show_skill, name="show_skill"),
    path("skill/add/", create_skill, name="create_skill"),
    path("api/skills/", get_skill_json, name="get_skill_json"),
    path("skill/<uuid:skill_id>/delete/", delete_skill, name="delete_skill"),
    
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("api/educations/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("education/delete/page", education_delete_page, name="education_delete_page")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
