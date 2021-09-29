from django.test import TestCase
from django.urls import reverse

from .models import Hike


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'index.html')

    def test_get_hike_detail_page(self):
        hike = Hike.objects.create(
            title='test hike',
            slug='test-hike-slug',
            content='this is the test hike content',
            difficulty=1,
            distance_km=5,
            est_duration_hrs=2,
            status=1
        )
        response = self.client.get(reverse('hike_detail', args=[hike.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'hike_detail.html')


        
 
    
