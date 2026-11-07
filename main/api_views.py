from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Project, Education, Skill
from main.permissions import IsPortfolioOwnerOrReadOnly, IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import ProjectSerializer, EducationSerializer, SkillSerializer

# -------------------------------------------------------------------------
# Project Section
# -------------------------------------------------------------------------
@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def project_list(request: HttpRequest):
    if request.method in ("GET", "HEAD"):
        projects = Project.objects.prefetch_related("starred_by").order_by("project_name", "id")
        project_type = request.query_params.get("project_type", "").strip()
        if project_type:
            projects = projects.filter(project_type__icontains=project_type)

        sort_project = request.query_params.get("sort_project", "").strip()
        if sort_project:
            if sort_project == "star-count":
                projects = projects.order_by("-star_count")
            elif sort_project == "name":
                projects = projects.order_by("-project_name")


        serializer = ProjectSerializer(
            projects, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = ProjectSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def project_detail(request: HttpRequest, project_id):
    project = get_object_or_404(
        Project.objects.prefetch_related("starred_by"), pk=project_id,
    )
    if request.method in ("GET", "HEAD"):
        serializer = ProjectSerializer(project, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = ProjectSerializer(
        project, data=request.data, partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def project_star(request: HttpRequest, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if project.starred_by.filter(pk=request.user.pk).exists():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
    serializer = ProjectSerializer(project, context={"request": request})
    return Response(serializer.data)


# -------------------------------------------------------------------------
# Education Section
# -------------------------------------------------------------------------
@api_view(['GET', 'HEAD', 'POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def education_list(request: HttpRequest):
    if request.method in ('GET', 'HEAD'):
        educations = Education.objects.all().order_by("-year_start")

        search_query = request.query_params.get("institution_name", "").strip()
        if search_query:
            educations = educations.filter(institution_name__icontains = search_query)

        serializer = EducationSerializer(
            educations,
            many=True
        )

        return Response(serializer.data)

    serializer = EducationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'HEAD', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def education_detail(request: HttpRequest, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method in ('GET', 'HEAD'):
        serializer = EducationSerializer(education, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method in ('DELETE'):
        education.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = EducationSerializer(
        education, data=request.data, partial=request.method == "PATCH"
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


# -------------------------------------------------------------------------
# Skill Section
# -------------------------------------------------------------------------
@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def skill_list(request: HttpRequest):
    if request.method in ("GET", "HEAD"):
        skills = Skill.objects.all()

        search_query = request.query_params.get("skill_name","").strip()
        if search_query:
            skills = skills.filter(name__icontains=search_query)

        hardskill = SkillSerializer(
            skills.filter(skill_category="hardskill"), many=True
        )
        softskill = SkillSerializer(
            skills.filter(skill_category="softskill"), many=True
        )

        return Response({"hardskills" : hardskill.data, "softskills" : softskill.data}, status=status.HTTP_200_OK)

    serializer = SkillSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def skill_detail(request: HttpRequest, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    
    if request.method in ("GET", "HEAD"):  
        serializer = SkillSerializer(skill, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method in ("DELETE"):
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = SkillSerializer(request.data, partial=request.method == "PATCH")
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)