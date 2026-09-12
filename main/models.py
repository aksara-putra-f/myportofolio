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
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)

    #
    def __str__(self):
        return self.title

    #
    @property
    def is_ongoing(self):
        return self.ended_at is None


class Skill(models.Model):
    SKILL_CATEGORY = [
        ('softskill', 'Softskill'),
        ('hardskill', 'Hardskill')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, blank=False)
    short_desc = models.CharField(max_length=250, null=False, blank=True)
    skill_category = models.CharField(choices=SKILL_CATEGORY)