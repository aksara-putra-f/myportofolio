from django.forms import ModelForm, TextInput, Textarea, FileInput
from main.models import Education

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "year_start",
            "year_end",
            "institution_name",
            "major",
            "activities",
            "institution_logo"
        ]

        labels = {
            "year_start": "Year Education Began",
            "year_end": "Year Graduated",
            "institution_name": "Name of the School or University",
            "major": "Educational Major Pursued",
            "activities": "Activities Taken During the Education",
            "institution_logo": "File of the Institution Logo"
        }

        widgets = {
            "year_start": TextInput(
                attrs={
                    "placeholder": "Year I began the education",
                    "maxlength": 255,
                }
            ),
            "year_end": TextInput(
                attrs={
                    "placeholder": "Year I graduated from the education",
                    "maxlength": 255,
                }
            ),
            "institution_name": TextInput(
                attrs={
                    "placeholder": "Name of the school/university",
                    "maxlength": 255,
                }
            ),
            "major": TextInput(
                attrs={
                    "placeholder": "Major I pursued",
                    "maxlength": 255,
                }
            ),
            "activites": Textarea(
                attrs={
                    "placeholder": "Activity",
                    "rows": 8,
                }
            ),
            "institution_logo": FileInput(
                {"accept": ".png,.jpg,.jpeg"}
            )
        }