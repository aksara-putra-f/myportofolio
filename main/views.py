from django.shortcuts import get_object_or_404, redirect, render

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse

from main.forms import EducationForm, ExperienceForm, ProjectForm, SkillForm
from main.models import *

import datetime

# Create your views here.
def show_main(request):
    last_login = request.COOKIES.get("last_login", "No login session has been found / no cookie found")

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
        "highlited_skill_list" : Skill.objects.all().filter(highlight_skill = True),
        "last_login" : last_login
    }
    return render(request, "index.html", context)


def register(request):
    form = UserCreationForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account has been created successfully! Please login")
        return redirect("main:login")
    
    context = {
        "name": "Aksara Putra Fachruddin",
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect("main:show_main")
        response.set_cookie("last_login", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Aksara Putra Fachruddin",
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie("last_login")
    return response


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


@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience Data Has Been Added Successfully!")
        return redirect("main:show_experience")

    context = {
        "name": "Aksara Putra Fachruddin",
        "title": "Create Experience",
        "form": form,
        "is_updating_item": False
    }
    return render(request, "form-templates/experience_form.html", context)


def get_experience_json(request):
    on_going_query = request.GET.get("on_going", "").strip()
    experiences = Experience.objects.all()

    if on_going_query:
        if on_going_query.lower() == "on going":
            experiences = experiences.filter(ended_at__isnull = True)
        elif on_going_query.lower() == "finished":
            experiences = experiences.filter(ended_at__isnull = False)

    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Education, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "The Experience data has been deleted successfully!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")


@login_required(login_url="/login/")
def update_experience(request, experience_id):
    update_experience_obj = get_object_or_404(Experience, pk=experience_id)
    data = {
        "title" : update_experience_obj.title,
        "place" : update_experience_obj.place,
        "description" : update_experience_obj.description,
        "responsibilities_list" : update_experience_obj.responsibilities_list,
        "category" : update_experience_obj.category,
        "started_at" : update_experience_obj.started_at,
        "ended_at" : update_experience_obj.ended_at,
        "highlight_experience" : update_experience_obj.highlight_experience
    }

    form = ExperienceForm(request.POST or None, initial=data, instance=update_experience_obj)

    if request.method == "POST" and form.is_valid():
            form.save()
            messages.success(request, "The Project Item Has Been Updated Successfully!")
            return redirect("main:show_experience")
    
    context = {
        "name": "Aksara Putra Fachruddin",
        "title": "Update Project",
        "form": form,
        "is_updating_item" : True
    }
    
    return render(request, "form-templates/experience_form.html", context)


def edit_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize('json', json_response.content.decode("utf-8"))
    experiences = [experience.object for experience in experiences]

    context = {
        "name": "Aksara Putra Fachruddin",
        "experience_list": experiences
    }
    return render(request, "edit-templates/experience_edit.html", context)


@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")


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


@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
            raise PermissionDenied
    
    form = ProjectForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "The Project Item Has Been Added Successfully!")
        return redirect("main:show_project")

    context = {
        "name": "Aksara Putra Fachruddin",
        "title": "Add New Project",
        "form": form,
        "is_updating_item" : False
    }

    return render(request, "form-templates/project_form.html", context)


def get_project_json(request):
    project_type_query = request.GET.get("project_type","").strip()
    projects = Project.objects.all()

    if project_type_query:
        projects = projects.filter(project_type = project_type_query)

    projects_json = serializers.serialize(
                        "json", 
                        projects,
                        use_natural_foreign_keys=True
                    )
    return HttpResponse(projects_json, content_type="application/json")


@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == "POST":
        project.delete()
        messages.success(request, "The Project item has been deleted successfully!")
        return redirect("main:show_project")

    return redirect("main:show_project")


@login_required(login_url="/login/")
def update_project(request, project_id):
    update_project_obj = get_object_or_404(Project, pk=project_id)
    data = {
        "project_name" : update_project_obj.project_name,
        "project_desc" : update_project_obj.project_desc,
        "project_type" : update_project_obj.project_type,
        "media" : update_project_obj.media,
        "media_type" : update_project_obj.media_type,
        "highlight_project" : update_project_obj.highlight_project,
        "ext_link_provided" : update_project_obj.ext_link_provided,
        "ext_link" : update_project_obj.ext_link,
        "starred_by" : update_project_obj.starred_by
    }

    form = ProjectForm(request.POST or None, request.FILES or None, initial=data, instance=update_project_obj)

    if request.method == "POST" and form.is_valid():
            form.save()
            messages.success(request, "The Project Item Has Been Updated Successfully!")
            return redirect("main:show_project")
    
    context = {
        "name": "Aksara Putra Fachruddin",
        "title": "Update Project",
        "form": form,
        "is_updating_item" : True
    }
    
    return render(request, "form-templates/project_form.html", context)


def edit_project(request):
    json_response = get_project_json(request)
    
    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]

    context = {
    "name": "Aksara Putra Fachruddin",
    "project_list": projects,
    }
    return render(request, "edit-templates/project_edit.html", context)


@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

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


@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = EducationForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education Has Been Added Successfully!")
        return redirect("main:show_education")

    context = {
        "name": "Aksara Putra Fachruddin",
        "title": "Create Education",
        "form": form,
        "is_updating_item": False
    }
    return render(request, "form-templates/education_form.html", context)


def get_education_json(request):
    institution_name_query = request.GET.get("institution_name", "").strip()
    educations = Education.objects.all().order_by("-year_start")

    if institution_name_query:
        educations = educations.filter(institution_name=institution_name_query)

    education_json = serializers.serialize("json", educations)
    return HttpResponse(education_json, content_type="application/json")


@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "The Education has been deleted successfully!")
        return redirect("main:show_education")

    return redirect("main:show_education")


@login_required(login_url="/login/")
def update_education(request, education_id):
    update_education_obj = get_object_or_404(Education, pk=education_id)
    data = {
        "year_start" : update_education_obj.year_start,
        "year_end" : update_education_obj.year_end,
        "institution_name" : update_education_obj.institution_name,
        "major" : update_education_obj.major,
        "activities" : update_education_obj.activities,
        "institution_logo" : update_education_obj.institution_logo
    }

    form = EducationForm(request.POST or None, request.FILES or None, initial=data, instance=update_education_obj)

    if request.method == "POST" and form.is_valid():
            form.save()
            messages.success(request, "The Project Item Has Been Updated Successfully!")
            return redirect("main:show_education")
    
    context = {
        "name": "Aksara Putra Fachruddin",
        "title": "Update Education",
        "form": form,
        "is_updating_item" : True
    }
    
    return render(request, "form-templates/education_form.html", context)


def edit_education(request):
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
    return render(request, "edit-templates/education_edit.html", context)

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



@login_required(login_url="/login/")
def create_skill(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = SkillForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Skill has been added successfully!")
        return redirect("main:show_skill")

    context = {
        "name": "Aksara Putra Fachruddin",
        "title": "Add New Skill",
        "form": form,
        "is_updating_item": False
    }

    return render(request, "form-templates/skill_form.html", context)


def get_skill_json(request):
    skill_name_query = request.GET.get("skill_name", "").strip()
    skills = Skill.objects.all()

    if skill_name_query:
        skills = skills.filter(name__icontains=skill_name_query)

    skill_json = serializers.serialize("json", skills)
    return HttpResponse(skill_json, content_type="application/json")


@login_required(login_url="/login/")
def delete_skill(request, skill_id):
    if not request.user.is_superuser:
            raise PermissionDenied
    
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "The Skill item has been deleted successfully!")
        return redirect("main:show_skill")

    return redirect("main:show_skill")


@login_required(login_url="/login/")
def update_skill(request, skill_id):
    if not request.user.is_superuser:
            raise PermissionDenied
    
    update_skill_obj = get_object_or_404(Skill, pk=skill_id)
    data = {
        "name" : update_skill_obj.name,
        "short_desc" : update_skill_obj.short_desc,
        "skill_category" : update_skill_obj.skill_category,
        "highlight_skill" : update_skill_obj.highlight_skill
    }

    form = SkillForm(request.POST or None, initial=data, instance=update_skill_obj)

    if request.method == "POST" and form.is_valid():
            form.save()
            messages.success(request, "The Project Item Has Been Updated Successfully!")
            return redirect("main:show_skill")
    
    context = {
        "name": "Aksara Putra Fachruddin",
        "title": "Update Skill",
        "form": form,
        "is_updating_item" : True
    }
    
    return render(request, "form-templates/skill_form.html", context)


def edit_skill(request):
    json_response = get_skill_json(request)
    
    skills = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    skills = [skill.object for skill in skills]

    context = {
    "name": "Aksara Putra Fachruddin",
    "skill_list": skills,
    }
    return render(request, "edit-templates/skill_edit.html", context)