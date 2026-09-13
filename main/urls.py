from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education")
    path("project/", show_project, name="show_project")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)