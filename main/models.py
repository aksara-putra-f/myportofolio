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

    #
    def __str__(self):
        return self.title

    #
    @property
    def is_ongoing(self):
        return self.ended_at is None