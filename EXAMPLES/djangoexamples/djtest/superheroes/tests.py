from django.test import TestCase, tag
from django.urls import reverse   #   {% url ... %}

from superheroes.models import Superhero, Power, City, Enemy

class SuperheroTests(TestCase):

    fixtures = ['superheroes']  #  APP/fixtures/superheroes.json

    def setUp(self):
        self.sm = Superhero.objects.get(name="Superman")
        self.sm_response = self.client.get(
            reverse('superheroes:hero', args=('Superman',))
            #  http://127.0.0.1/superheroes/hero/Superman
        )

    def test_clark_kent_is_supermans_secret_identity(self):
        self.assertEquals('Clark Kent', self.sm.secret_identity)

    def test_kal_el_is_supermans_real_name(self):
        self.assertEquals('Kal-el', self.sm.real_name)

    def test_fetch_superhero_ok(self):
        self.assertEqual(self.sm_response.status_code, 200)

    @tag('goofy')
    def test_superhero_has_good_content(self):
        self.assertIn(b'Superman', self.sm_response.content)

    @tag('goofy')
    @tag('silly')
    def test_two_plus_two_is_four(self):
        self.assertEqual(2 + 2, 4)

class OtherTests(TestCase):
    def test_something(self):
        self.assertEqual(2, 2)

#TODO: add form test
