from django.forms import ModelForm, TextInput, Textarea, FileInput, Select, CheckboxInput
from main.models import Education, Skill

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


class SkillForm(ModelForm):
    class Meta:
        model = Skill

        fields = [
            "name",
            "short_desc",
            "skill_category",
            "highlight_skill"
        ]

        labels = {
            "name" : "Skill Name",
            "short_decs" : "Skill Short Description",
            "skill_category" : "Skill Category",
            "highlight_skill" : "Show Skill on Front Page"
        }

        widgets = {
            "name" : TextInput(
                attrs={
                    "placeholder": "Name of the skill",
                    "maxlength": 255,
                }
            ),

            "short_desc" : Textarea(
                attrs={
                    "placeholder": "Short description about the skill",
                    "rows": 2
                }
            ),

            "skill_category" : Select(
                attrs={
                    "choices": [
                        ('softskill', 'Softskill'),
                        ('hardskill', 'Hardskill')
                    ]
                }
            ),

            "highlight_skill" : CheckboxInput()
    }