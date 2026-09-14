from django.shortcuts import render
from main.models import *

# Create your views here.
def show_main(request):
    context = {
        "name" : "Aksara Putra Fachruddin",
        "npm" : "2506597284",
        "study_program" : "S1 Ilmu Komputer",
        "bio" : (
            "My name is Aksara Putra Fachruddin, and I'm a computer science student at Universitas Indonesia. "
            "Currently, I have an interest in game development and artificial intelligence. "
            "Throughout my academic years, I've seeking opportunities to learn, grow, and collaborate through personal and team projects, organization, competition, courses, and the technology community."
        ),
        "recent_education" : Education.objects.order_by('year_start').reverse().first(),
        "highlight_experience_list" : Experience.objects.all().filter(highlite_experience = True),
        "highlight_experience_count" : Experience.objects.all().filter(highlite_experience = True).count(),
        "highlited_project_list" : Project.objects.all().filter(highlight_project = True),
        "highlited_skill_list" : Skill.objects.all().filter(highlight_skill = True)
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Aksara Putra Fachruddin",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_education(request):
    context = {
        "name" : "Aksara Putra Fachruddin",
        "education_list" : Education.objects.all()
    }
    return render(request, "education.html", context)


def show_project(request):
    context = {
        "name" : "Aksara Putra Fachruddin",
        "project_list" : Project.objects.all()
    }
    return render(request, "project.html", context)


def show_skill(request):
    context = {
        "name" : "Aksara Putra Fachruddin",
        "hardskill_list" : Skill.objects.all().filter(skill_category='hardskill'),
        "softskill_list" : Skill.objects.all().filter(skill_category='softskill')
    }
    return render(request, "skill.html", context)

