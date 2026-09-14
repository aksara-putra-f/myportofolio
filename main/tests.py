from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import *


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Staf Akademik dan Pengajar",
            place="Betis Fasilkom UI",
            description="Membantu persiapan siswa menghadapi UTBK subtes PU.",
            responsibilities_list = ['Membuat soal tryout', 'Membuat modul', 'Mengajar kelas'],
            category="part-time",
            highlight_experience = True
        )

        self.education = Education.objects.create(
            institution_name = 'Universitas Indonesia',
            major = 'Ilmu Komputer',
            year_start = '2025',
            year_end = 'Present',
            activities = ['Panitia Betis Fasilkom UI', 'Staff Panitia DDP-0']
        )

        self.skill = Skill.objects.create(
            name = "Godot",
            short_desc = "Kemampuan untuk menggunakan Godot engine",
            skill_category = "hardskill",
            highlight_skill = True
        )

        self.project = Project.objects.create(
            project_name = 'Med Rush',
            project_type = 'game project',
            project_desc = 'Sebuah Game 2D yang dibuat saat gamejam compfest UI',
            highlight_project = True,
            ext_link_provided = True,
            ext_link = 'https://aksaindo1834.itch.io/med-rush'
        )

    ## Tes Apakah URL untuk main, education-page, skill-page, experience-page, dan project-page dapat diakses atau tidak
    ## dan memiliki perilaku yang diharapkan
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.project.get_project_type_display())
        self.assertContains(response, self.education.institution_name)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')


    def test_education_url_is_accessible(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, self.education.institution_name)
        self.assertContains(response, self.education.major)
        self.assertContains(response, f'href="{reverse("main:show_education")}"')

        
    def test_project_url_is_accessible(self):
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, self.project.project_name)
        self.assertContains(response, self.project.project_desc)
        self.assertContains(response, f'href="{reverse("main:show_project")}"')


    def test_skill_url_is_accessible(self):
        response = self.client.get(reverse("main:show_skill"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertContains(response, self.skill.name)
        self.assertContains(response, self.skill.short_desc)
        self.assertContains(response, self.skill.skill_category)
        self.assertContains(response, f'href="{reverse("main:show_skill")}"')


    def test_experience_url_is_accessible(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.place)
        self.assertContains(response, self.experience.get_category_display())
        self.assertContains(response, self.experience.description)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')


    ## Tes jika url yang dimasukkan tidak pernah terdaftar
    ## Status request seharusnya '404'
    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)


    ## Tes untuk menguji model education, project, experience, dan skill
    ## Apakah atribut masing-masing bekerja semestinya
    def test_experience_model(self):
        self.assertEqual(self.experience.title, "Staf Akademik dan Pengajar")
        self.assertEqual(self.experience.place, "Betis Fasilkom UI")
        self.assertEqual(self.experience.category, "part-time")
        self.assertEqual(self.experience.responsibilities_list, ['Membuat soal tryout', 'Membuat modul', 'Mengajar kelas'])
        self.assertIsInstance(self.experience.responsibilities_list, list)
        self.assertTrue(self.experience.is_ongoing)
        self.assertTrue(self.experience.highlight_experience)


    def test_education_model(self):
        self.assertEqual(self.education.institution_name, 'Universitas Indonesia')
        self.assertEqual(self.education.major, 'Ilmu Komputer')
        self.assertEqual(self.education.year_start, '2025')
        self.assertEqual(self.education.year_end, 'Present')
        self.assertEqual(self.education.activities, ['Panitia Betis Fasilkom UI', 'Staff Panitia DDP-0'])
        self.assertIsInstance(self.education.activities, list)


    def test_skill_model(self):
        self.assertEqual(self.skill.name, "Godot")
        self.assertEqual(self.skill.skill_category, "hardskill")
        self.assertEqual(self.skill.short_desc, "Kemampuan untuk menggunakan Godot engine")
        self.assertTrue(self.skill.highlight_skill)


    def test_project_model(self):
        self.assertEqual(self.project.project_name, "Med Rush")
        self.assertEqual(self.project.project_desc, 'Sebuah Game 2D yang dibuat saat gamejam compfest UI')
        self.assertEqual(self.project.project_type, 'game project')


    ## Tes page untuk masing-masing section (education, skill, project, dan experience)
    ## Apakah masing-masing page sudah memiliki data yang sesuai 
    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')


    def test_education_page(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "education.html")
        self.assertContains(response, self.education.institution_name)
        self.assertContains(response, self.education.major)
        self.assertContains(response, self.education.year_start)
        self.assertContains(response, self.education.year_end)


    def test_education_page_activity_list(self):
        response = self.client.get(reverse("main:show_education"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"<li>Panitia Betis Fasilkom UI</li>")
        self.assertContains(response, f"<li>Staff Panitia DDP-0</li>")


    def test_skill_page(self):
        response = self.client.get(reverse("main:show_skill"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertContains(response, self.skill.name)
        self.assertContains(response, self.skill.short_desc)


    def test_skill_page_skill_container(self):
        temp_softskill_obj = Skill.objects.create(
            name = "Teamwork",
            short_desc = "Kemampuan untuk bekerja sama dengan anggota tim",
            skill_category = "softskill",
            highlight_skill = True
        )
        response = self.client.get(reverse("main:show_skill"))

        self.assertContains(response, f"<p class=\"skill-name\">Godot</p>")
        self.assertContains(response, f"<p class=\"skill-name\">Teamwork</p>")


    def test_project_page(self):
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, self.project.project_name)
        self.assertContains(response, self.project.project_desc)
        self.assertContains(response, f'href="{self.project.ext_link}"')


    ## Tes page setiap section (education, project, skill, dan experience) jika belum ada data yang ditambahkan
    ## Output seharusnya menampilkan pesan "belum ada data"-nya masing-masing
    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "No experience has been added.")


    def test_empty_education_page(self):
        Education.objects.all().delete()
        response = self.client.get(reverse("main:show_education"))

        self.assertContains(response, "No education background has been added.")


    def test_empty_project_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_project"))

        self.assertContains(response, "No project has been added.")


    def test_empty_skill_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skill"))

        self.assertContains(response, "No skill has been added.")


    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Finished")