from django.test import SimpleTestCase
from django.http import response
from django.urls import reverse
# Create your tests here.


class SnakesTests(SimpleTestCase):

    def test_snakes_page(self):
        url = reverse("home")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'home.html')

    def test_about_page(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_about_template(self):
        url = reverse('about')
        res = self.client.get(url)
        self.assertTemplateUsed(res, "about.html")
