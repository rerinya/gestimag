from django.test import TestCase
from myapp.models import Image

class ImageTestCase(TestCase):
    def setUp(self):
        Image.objects.create(name="lion", url="https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg")
        Image.objects.create(name="cat", url="https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg")
    
    def test_images(self):
        lion = Image.objects.get(name="lion")
        cat = Image.objects.get(url="https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg")
        self.assertEqual(lion.url, "https://upload.wikimedia.org/wikipedia/commons/7/73/Lion_waiting_in_Namibia.jpg")
        self.assertEqual(cat.name, "cat")