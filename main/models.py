import uuid
from django.db import models

# Create your models here.
class Experience(models.Model):
    # Kategori-kategori dari 5experience yang ada
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    # Atribut-atribut untuk data yang tergolong ke dalam Experience
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(default="", max_length=255)
    place = models.CharField(default="", max_length=225)
    description = models.TextField()
    responsibilities_list = models.JSONField(default=list, blank=True)
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    started_at = models.DateField(blank=True, null=True)
    ended_at = models.DateField(blank=True, null=True)
    highlite_experience = models.BooleanField(default=False)

    #
    def __str__(self):
        return self.title

    #
    @property
    def is_ongoing(self):
        return self.ended_at is None


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year_start = models.CharField(default="Present", max_length=7, null=False, blank=False)
    year_end = models.CharField(default="Present", max_length=7, null=False, blank=False)
    institution_name = models.CharField(max_length=250, null=False, blank=False)
    major = models.CharField(default="", max_length=250, null=False, blank=True)
    activities = models.JSONField(default=list, null=False, blank=True)
    institution_logo = models.ImageField(default="no_image_square.png", upload_to='institution_logo/', blank=False)

    def __str__(self):
        return self.institution_name


class Project(models.Model):
    MEDIA_TYPE = [
        ('image', 'Image'),
        ('video', 'Video')
    ]

    PROJECT_TYPE = [
        ('game project', "Game Project"),
        ('ai project', "AI Project"),
        ('web project', "Web Project"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.CharField(max_length=250, null=False, blank=False)
    project_type = models.CharField(choices=PROJECT_TYPE, default='game project')
    project_desc = models.TextField()
    media = models.FileField(upload_to="project-media/", default="no_image_square.png", blank=False, null=True)
    media_type = models.CharField(blank=False, choices=MEDIA_TYPE, default='image')
    ext_link_provided = models.BooleanField()
    ext_link = models.URLField()
    highlight_project = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.project_name


class Skill(models.Model):
    SKILL_CATEGORY = [
        ('softskill', 'Softskill'),
        ('hardskill', 'Hardskill')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, blank=False)
    short_desc = models.CharField(max_length=250, null=False, blank=True)
    skill_category = models.CharField(choices=SKILL_CATEGORY)
    highlight_skill = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.name