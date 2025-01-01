from django.test import TestCase
from django.urls import reverse
from drugs.models import Drug

class DrugListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_drug_list_view(self):
        response = self.client.get(reverse('drugs:drug_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'drugs/drug_list.html')
