from django.test import TestCase
from .models import Character

# Create your tests here.


class CharacterTest(TestCase):
    def setUp(self):
        self.character = Character.objects.create(
            id="5cd99d4bde30eff6ebccfbd6",
            height="",
            race="Human",
            birth="2000-01-01",
            death="F0 120",
            realm="Reunited Kingdom",
            hair="dark",
            name="Aragorn",
            wikiUrl="http://lotr.wikia.com//wiki/Aragorn_II_Elessar",
        )

    def test_post_model(self):
        d = self.character
        self.assertTrue(isinstance(d, Character))
