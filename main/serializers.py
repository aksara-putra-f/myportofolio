from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Project, Education, Skill

class ComaSeparatedList(serializers.Field):
    def to_representation(self, value):
        if not value:
            return []

        return [item.strip() for item in value.split(",")]

    def to_internal_value(self, data):
        if isinstance(data, list):
            items = data
        elif isinstance(data, str):
            items = data.split(",")
        else:
            raise serializers.ValidationError("Activities input must be in the form of string or list.")

        return ", ".join([item.strip() for item in items])


# Serializer untuk data-data project
class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id", "project_name", "project_desc", "project_type",
            "media", "media_type", "highlight_project", "ext_link_provided", "ext_link",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id", "star_count", "is_starred", "starred_by_names"]

    def validate_project_name(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_project_desc(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())


# Serializer untuk data-data education
class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = [
            "id", "year_start", "year_end", "institution_name", "major",
            "activities", "institution_logo"
        ]
        read_only_fields = ["id"]

    activities = ComaSeparatedList()

    def validate_institution_name(self, value):
        cleaned_value = value.strip()
        if not cleaned_value:
            raise serializers.ValidationError("Institution name cannot be empty.")
        
        return cleaned_value

    def validate_major(self, value):
        if not value.strip():
            raise serializers.ValidationError("Major cannot be empty.")

        return value.strip()

    def validate(self, value):
        year_start = value.get('year_start').strip()
        year_end = value.get('year_end').strip()

        if not (year_start and year_end):
            raise serializers.ValidationError("Education year cannot be empty.")

        if int(year_end) < int(year_start):
            raise serializers.ValidationError("Education finish year cannot be less than start year.")

        value['year_start'] = year_start
        value['year_end'] = year_end
        return value        


# Serializer untuk data-data skill
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'id', 'name', 'short_desc', 'skill_category', 'highlight_skill'
        ]
        read_only_fields = ['id']

    def validate_name(self, data):
        data = strip_tags(data).strip()
        if not data:
            raise serializers.ValidationError("Skill name cannot be empty.")

        return data

    def validate_short_desc(self, data):
        data = data.strip()
        if not data:
            raise serializers.ValidationError("Skill short description cannot be empty.")

        return data