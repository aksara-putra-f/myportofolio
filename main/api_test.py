import uuid

from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Education, Skill, Project

class BaseAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com",
        )
        self.editor = User.objects.create_user(username="editor", password="test-password")
        self.editor.is_staff = True  # sesuaikan dengan aturan IsPortfolioOwnerOrEditorOrReadOnly
        self.editor.save()
        self.editor.groups.add(Group.objects.get_or_create(name="Editor")[0])
        self.visitor = User.objects.create_user(username="visitor", password="test-password")

# -------------------------------------------------------------------------
# Project
# -------------------------------------------------------------------------
class ProjectAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com",
        )
        self.visitor = User.objects.create_user(username="visitor", password="test-password")
        self.project = Project.objects.create(
            project_name="Portfolio", project_desc="My website"
        )
        self.list_url = reverse("api:project_list")
        self.detail_url = reverse("api:project_detail", args=[self.project.id])
        self.star_url = reverse("api:project_star", args=[self.project.id])
        self.payload = {
            "project_name": "New project", "project_desc": "A game made by myself", "ext_link_provided" : True, "ext_link" : "https://aksaindo1834.itch.io/butter-fly-fly-to-the-toast"
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], str(self.project.id))
        self.assertFalse(response.data[0]["is_starred"])
        self.assertNotIn("fields", response.data[0])
        self.assertEqual(self.client.get(self.detail_url).status_code, status.HTTP_200_OK)

    def test_search_and_empty_results(self):
        response = self.client.get(self.list_url, {"project_type": "game project"})
        self.assertEqual(len(response.data), 1)
        response = self.client.get(self.list_url, {"project_type": "not exist"})
        self.assertEqual(response.data, [])

    def test_missing_project(self):
        url = reverse("api:project_detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.patch(self.detail_url, {"title": "Changed"}, format="json").status_code, 403)
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(Project.objects.count(), 1)
        self.project.refresh_from_db()
        self.assertEqual(self.project.project_name, "Portfolio")

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Project.objects.filter(pk=response.data["id"]).exists())

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)
        for changes, field in [
            ({"project_name": "   "}, "project_name"),
            ({"project_name": '<img src="x" onerror="alert(1)">'}, "project_name"),
            ({"ext_link": "javascript:alert(1)"}, "ext_link"),
        ]:
            response = self.client.post(self.list_url, {**self.payload, **changes}, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn(field, response.data)
        self.assertEqual(Project.objects.count(), 1)

    def test_patch_put_and_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.detail_url, {"project_name": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.project_desc, "My website")
        response = self.client.put(self.detail_url, {"project_name": "Incomplete"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(Project.objects.filter(pk=self.project.id).exists())

    def test_star_requires_login_and_toggles(self):
        self.assertEqual(self.client.post(self.star_url).status_code, status.HTTP_403_FORBIDDEN)
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)
        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload, "star_count": 99, "is_starred": True,
            "starred_by_names": "forged", "starred_by": [self.visitor.id],
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

    def test_staff_and_editor_cannot_manage_tutorial_projects(self):
        self.visitor.is_staff = True
        self.visitor.save()
        self.visitor.groups.add(Group.objects.create(name="Editor"))
        self.client.force_authenticate(user=self.visitor)
        response = self.client.patch(self.detail_url, {"project_name": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)
        self.assertEqual(self.client.delete(self.list_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Project.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)
        client.login(username="owner", password="test-password")
        # The Browsable API form renders a real CSRF token into the response.
        page = client.get(self.list_url, HTTP_ACCEPT="text/html")
        self.assertEqual(page.status_code, status.HTTP_200_OK)
        token = client.cookies["csrftoken"].value
        response = client.post(
            self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# -------------------------------------------------------------------------
# Education
# -------------------------------------------------------------------------
class EducationAPITest(BaseAPITest):
    def setUp(self):
        super().setUp()
        # Sesuaikan field wajib dengan model Education kamu.
        self.education = Education.objects.create(
            institution_name="Universitas Indonesia",
            year_start=2022,
            activities="Asisten dosen, Himpunan",
        )
        self.older = Education.objects.create(
            institution_name="SMA Negeri 1", year_start=2018, activities="OSIS",
        )
        self.list_url = reverse("api:education_list")
        self.detail_url = reverse("api:education_detail", args=[self.education.id])
        self.payload = {
            "institution_name": "Institut Teknologi Bandung",
            "year_start": 2024,
            "activities": "Lomba coding, Kepanitiaan",
        }
 
    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(self.client.get(self.detail_url).status_code, status.HTTP_200_OK)
 
    def test_list_ordered_by_year_start_desc(self):
        response = self.client.get(self.list_url)
        names = [item["institution_name"] for item in response.data]
        self.assertEqual(names, ["Universitas Indonesia", "SMA Negeri 1"])
 
    def test_activities_returned_as_list(self):
        response = self.client.get(self.detail_url)
        self.assertIsInstance(response.data["activities"], list)
        self.assertIn("OSIS", self.client.get(
            reverse("api:education_detail", args=[self.older.id])
        ).data["activities"])
 
    def test_search_by_institution_name(self):
        response = self.client.get(self.list_url, {"institution_name": "indonesia"})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["institution_name"], "Universitas Indonesia")
 
    def test_search_without_result_and_blank_query(self):
        response = self.client.get(self.list_url, {"institution_name": "tidak ada"})
        self.assertEqual(response.data, [])
        response = self.client.get(self.list_url, {"institution_name": "   "})
        self.assertEqual(len(response.data), 2)
 
    def test_missing_education(self):
        url = reverse("api:education_detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)
 
    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.patch(self.detail_url, {"institution_name": "X"}, format="json").status_code, 403)
            self.assertEqual(self.client.put(self.detail_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(Education.objects.count(), 2)
        self.education.refresh_from_db()
        self.assertEqual(self.education.institution_name, "Universitas Indonesia")
 
    def test_owner_and_editor_can_create(self):
        for user in (self.owner, self.editor):
            self.client.force_authenticate(user=user)
            payload = {**self.payload, "institution_name": f"Kampus {user.username}"}
            response = self.client.post(self.list_url, payload, format="json")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertTrue(Education.objects.filter(pk=response.data["id"]).exists())
 
    def test_create_validation_error(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {**self.payload, "institution_name": "   "}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("institution_name", response.data)
        self.assertEqual(Education.objects.count(), 2)
 
    def test_patch_put_and_delete_by_editor(self):
        self.client.force_authenticate(user=self.editor)
 
        response = self.client.patch(self.detail_url, {"institution_name": "UI Depok"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.education.refresh_from_db()
        self.assertEqual(self.education.institution_name, "UI Depok")
        self.assertEqual(self.education.year_start, 2022)  # PATCH tidak menghapus field lain
 
        response = self.client.put(self.detail_url, {"institution_name": "Tidak lengkap"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 
        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.education.refresh_from_db()
        self.assertEqual(self.education.institution_name, self.payload["institution_name"])
 
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(Education.objects.filter(pk=self.education.id).exists())
 
    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)
        self.assertEqual(self.client.delete(self.list_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
 
    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Education.objects.count(), 2)
 
 
# -------------------------------------------------------------------------
# Skill
# -------------------------------------------------------------------------
class SkillAPITest(BaseAPITest):
    def setUp(self):
        super().setUp()
        # Sesuaikan field wajib dengan model Skill kamu.
        self.hard = Skill.objects.create(name="Python", skill_category="hardskill")
        self.hard2 = Skill.objects.create(name="Django", skill_category="hardskill")
        self.soft = Skill.objects.create(name="Teamwork", skill_category="softskill")
        self.list_url = reverse("api:skill_list")
        self.detail_url = reverse("api:skill_detail", args=[self.hard.id])
        self.payload = {"name": "Docker", "skill_category": "hardskill"}
 
    def test_public_list_is_grouped_by_category(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(response.data.keys()), {"hardskills", "softskills"})
        self.assertEqual(len(response.data["hardskills"]), 2)
        self.assertEqual(len(response.data["softskills"]), 1)
        self.assertEqual(response.data["softskills"][0]["name"], "Teamwork")
 
    def test_public_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Python")
 
    def test_search_by_skill_name(self):
        response = self.client.get(self.list_url, {"skill_name": "pyth"})
        self.assertEqual(len(response.data["hardskills"]), 1)
        self.assertEqual(response.data["softskills"], [])
 
    def test_search_without_result_and_blank_query(self):
        response = self.client.get(self.list_url, {"skill_name": "tidak ada"})
        self.assertEqual(response.data, {"hardskills": [], "softskills": []})
        response = self.client.get(self.list_url, {"skill_name": "   "})
        self.assertEqual(len(response.data["hardskills"]), 2)
 
    def test_missing_skill(self):
        url = reverse("api:skill_detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)
 
    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.patch(self.detail_url, {"name": "X"}, format="json").status_code, 403)
            self.assertEqual(self.client.put(self.detail_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(Skill.objects.count(), 3)
        self.hard.refresh_from_db()
        self.assertEqual(self.hard.name, "Python")
 
    def test_owner_and_editor_can_create(self):
        for user in (self.owner, self.editor):
            self.client.force_authenticate(user=user)
            payload = {**self.payload, "name": f"Skill {user.username}"}
            response = self.client.post(self.list_url, payload, format="json")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertTrue(Skill.objects.filter(pk=response.data["id"]).exists())
 
    def test_create_validation_error(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {**self.payload, "name": "   "}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)
        self.assertEqual(Skill.objects.count(), 3)
 
    def test_patch_updates_existing_skill(self):
        # CATATAN: akan GAGAL sampai bug di skill_detail diperbaiki (lihat penjelasan).
        self.client.force_authenticate(user=self.editor)
        response = self.client.patch(self.detail_url, {"name": "Python 3"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.hard.refresh_from_db()
        self.assertEqual(self.hard.name, "Python 3")
        self.assertEqual(self.hard.skill_category, "hardskill")
        self.assertEqual(Skill.objects.count(), 3)  # tidak membuat skill baru
 
    def test_put_updates_existing_skill(self):
        # CATATAN: akan GAGAL sampai bug di skill_detail diperbaiki.
        self.client.force_authenticate(user=self.editor)
        response = self.client.put(self.detail_url, {"name": "Incomplete"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.put(
            self.detail_url, {"name": "Python 3", "skill_category": "hardskill"}, format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.hard.refresh_from_db()
        self.assertEqual(self.hard.name, "Python 3")
        self.assertEqual(Skill.objects.count(), 3)
 
    def test_delete(self):
        self.client.force_authenticate(user=self.editor)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(Skill.objects.filter(pk=self.hard.id).exists())
 
    def test_wrong_method_on_list(self):
        self.client.force_authenticate(user=self.owner)
        self.assertEqual(self.client.delete(self.list_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
 
    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Skill.objects.count(), 3)