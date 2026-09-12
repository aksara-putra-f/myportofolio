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


class Education(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year_start = models.CharField(default="Present", max_length=7, null=False, blank=False)
    year_end = models.CharField(default="Present", max_length=7, null=False, blank=False)
    institution_name = models.CharField(max_length=250, null=False, blank=False)
    major = models.CharField(default="", max_length=250, null=False, blank=True)
    activities = models.JSONField(default=list, null=False, blank=True)

    def __str__(self):
        return self.institution_name