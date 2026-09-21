from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.forms import EducationForm, ExperienceForm, ProjectForm, SkillForm
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


# ---------- #
# Experience #
# ---------- #
def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize("json", json_response.content.decode("utf-8"))
    experiences = [experience.object for experience in experiences]
    experience_category = Experience.EXPERIENCE_CHOICES
    on_going_query = request.GET.get("on_going", "").strip()
    experience_category_query = request.GET.get("experience_category", "").strip()

    context = {
        "name": "Aksara Putra Fachruddin",
        "experience_list": Experience.objects.all(),
        "experience_category": Experience.EXPERIENCE_CHOICES,
        "on_going_query": on_going_query,
        "experience_category": experience_category_query,
        "experience_category": experience_category
    }
    return render(request, "experience.html", context)


def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience Data Has Been Added Successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Aksara Putra Fachruddin",
        "form": form,
    }
    return render(request, "form-templates/experience_form.html", context)


def get_experience_json(request):
    on_going_query = request.GET.get("on_going", "").strip()
    experience_category_query = request.GET.get("experience_category", "").strip()
    experiences = Experience.objects.all()

    if on_going_query:
        if on_going_query.lower() == "on going":
            experiences = experiences.filter(ended_at__isnull = True)
        elif on_going_query.lower() == "finished":
            experiences = experiences.filter(ended_at__isnull = False)
    elif experience_category_query:
        experiences = experiences.filter(category = experience_category_query)

    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")


def delete_experience(request, experience_id):
    experience = get_object_or_404(Education, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "The Experience data has been deleted successfully!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


def experience_delete_page(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize('json', json_response.content.decode("utf-8"))
    experiences = [experience.object for experience in experiences]

    context = {
        "name": "Aksara Putra Fachruddin",
        "experience_list": experiences
    }
    return render(request, "delete-templates/experience_delete.html", context)


# --------- #
#  project  #
# --------- #
def show_project(request):
    json_response = get_project_json(request)

    projects = serializers.deserialize("json", json_response.content.decode("utf-8"))
    projects = [project.object for project in projects]
    project_type_query = request.GET.get("project_type", "").strip()

    context = {
        "name" : "Aksara Putra Fachruddin",
        "project_list" : projects,
        "project_type_query" : project_type_query,
        "project_types": Project.PROJECT_TYPE
    }
    return render(request, "project.html", context)


def create_project(request):
    form = ProjectForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "The Project Item Has Been Added Successfully!")
        return redirect("main:show_project")

    context = {
        "name": "Aksara Putra Fachruddin",
        "form": form
    }

    return render(request, "form-templates/project_form.html", context)


def get_project_json(request):
    project_type_query = request.GET.get("project_type","").strip()
    projects = Project.objects.all()

    if project_type_query:
        projects = projects.filter(project_type = project_type_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == "POST":
        project.delete()
        messages.success(request, "The Project item has been deleted successfully!")
        return redirect("main:show_project")

    return redirect("main:show_project")


# --------- #
# Education #
# --------- #
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
    return render(request, "form-templates/education_form.html", context)


def get_education_json(request):
    institution_name_query = request.GET.get("institution_name", "").strip()
    educations = Education.objects.all().order_by("-year_start")

    if institution_name_query:
        educations = educations.filter(institution_name=institution_name_query)

    education_json = serializers.serialize("json", educations)
    return HttpResponse(education_json, content_type="application/json")


def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "The Education has been deleted successfully!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def education_delete_page(request):
    json_response = get_education_json(request)
    
    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]

    context = {
    "name": "Aksara Putra Fachruddin",
    "education_list": educations,
    }
    return render(request, "delete-templates/education_delete.html", context)

# --------- #
#   Skill 
# --------- #
def show_skill(request):
    json_response = get_skill_json(request)
    
    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    skills = [skill.object for skill in skills]
    hardskill_list = [skill for skill in skills if skill.skill_category=='hardskill']
    softskill_list = [skill for skill in skills if skill.skill_category=='softskill']
    skill_name_query = request.GET.get("skill_name", "").strip()

    context = {
        "name": "Aksara Putra Fachruddin",
        "skill_list": skills,
        "hardskill_list" : hardskill_list,
        "softskill_list" : softskill_list,
        "skill_name_query": skill_name_query,
    }
    return render(request, "skill.html", context)



def create_skill(request):
    form = SkillForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Skill has been added successfully!")
        return redirect("main:show_skill")

    context = {
        "name": "Aksara Putra Fachruddin",
        "form": form
    }

    return render(request, "form-templates/skill_form.html", context)


def get_skill_json(request):
    skill_name_query = request.GET.get("skill_name", "").strip()
    skills = Skill.objects.all()

    if skill_name_query:
        skills = skills.filter(name__icontains=skill_name_query)

    skill_json = serializers.serialize("json", skills)
    return HttpResponse(skill_json, content_type="application/json")


def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "The Skill item has been deleted successfully!")
        return redirect("main:show_skill")

    return redirect("main:show_skill")