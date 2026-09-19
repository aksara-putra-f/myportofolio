from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.forms import EducationForm
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
        "highlight_experience_list" : Experience.objects.all().filter(highlight_experience = True),
        "highlight_experience_count" : Experience.objects.all().filter(highlight_experience = True).count(),
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


def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    institution_name_query = request.GET.get("institution_name", "").strip()

    context = {
        "name": "Aksara Putra Fachruddin",
        "education_list": educations,
        "institution_name_query": institution_name_query,
    }
    return render(request, "education.html", context)


def create_education(request):
    form = EducationForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education Has Been Added Successfully!")
        return redirect("main:show_education")

    context = {
        "name": "Aksara Putra Fachruddin",
        "form": form,
    }
    return render(request, "education_form.html", context)


def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.all()

    if title_query:
        educations = educations.filter(title__icontains=title_query)

    education_json = serializers.serialize("json", educations)
    return HttpResponse(education_json, content_type="application/json")


def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "The Education has been deleted successfully!")
        return redirect("main:show_education")

    return redirect("main:show_education")