from django.shortcuts import render
from main.models import *

# Create your views here.
def show_main(request):
    context = {
        "name" : "Aksara Putra Fachruddin",
        "npm" : "2506597284",
        "study_program" : "S1 Ilmu Komputer",
        "bio" : (
            "My name is Aksara Putra Fachruddin, and I'm a computer science student at Universitas Indonesia ."
            "Currently, I have an interest in game development and artificial intelligence. "
            "Throughout my academic years, I've seeking opportunities to learn, grow, and collaborate through personal and team projects, organization, competition, courses, and the technology community."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Aksara Putra Fachruddin",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_education(request):
    return render(request, "education.html", {"education_list" : Education.objects.all()})