from django.forms import ModelForm, TextInput, Textarea, FileInput, Select, CheckboxInput, URLInput
from main.models import Education, Project

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


class ProjectForm(ModelForm):
    class Meta:
        model = Project

        fields = [
            "project_name",
            "project_type",
            "project_desc",
            "media",
            "media_type",
            "highlight_project",
            "ext_link_provided",
            "ext_link",
        ]

        labels = {
            "project_name": "Name of the project",
            "project_desc": "Description of the project",
            "project_type": "Type of the project",
            "media": "A media of the project",
            "media_type": "Type of the project's media",
            "ext_link_provided": "Project has link to access it",
            "ext_link": "The link to access the project",
            "highlight_project": "Show project on front page"
        }

        widgets = {
            "project_name" : TextInput(
                attrs={
                    "placeholder": "The name of the project",
                    "maxlength": 225
                }
            ),

            "project_desc" : Textarea(
                attrs={
                    "placeholder": "Tell what's the project is about and what's your role",
                }
            ),

            "project_type" : Select(),

            "media" : FileInput(
                attrs={
                    "accept": ".jpg,.jpeg,.png,.mp4,.ogg,.webm"   
                }
            ),

            "media_type" : Select(),

            "highlight_project" : CheckboxInput(),

            "ext_link_provided" : CheckboxInput(),

            "ext_link" : URLInput()
        }