from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Hike, Comment, Booking, Schedule
import pytz
import datetime


class TestViews(TestCase):

    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.hike = Hike.objects.create(
                title='test hike A',
                slug='test-hike-slug-A',
                content='this is the test hike A content',
                difficulty=1,
                distance_km=5,
                est_duration_hrs=2,
                status=1
        )
        self.comment = Comment.objects.create(
            hike=self.hike,
            username=self.user,
            message='this is a comment for hike A'
        )
        self.schedule = Schedule.objects.create(
            hike=self.hike,
            starts=datetime.datetime(2018, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
        )
        self.booking = Booking.objects.create(
            hike=self.schedule,
            username=self.user,
            places_reserved=1
        )

    def test_get_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'index.html')

    def test_get_hike_detail_page(self):
        response = self.client.get(reverse('hike_detail', args=[self.hike.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'hike_detail.html')

    def test_get_mybookings_page(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('hike_mybookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'hike_mybookings.html')

    def test_can_toggle_like_hike(self):
        self.client.login(username='testuser', password='12345')
        numlikes = self.hike.likes.count()
        response = self.client.post(reverse('hike_like', args=[self.hike.slug]))
        self.assertRedirects(response, reverse('hike_detail', args=[self.hike.slug]))
        self.assertEqual(self.hike.likes.count(), numlikes+1)
        response = self.client.post(reverse('hike_like', args=[self.hike.slug]))
        self.assertRedirects(response, reverse('hike_detail', args=[self.hike.slug]))
        self.assertEqual(self.hike.likes.count(), numlikes)

    def test_can_comment_on_hike(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('hike_detail', args=[self.hike.slug]), data={'message': 'new comment'})
        self.assertRedirects(response, reverse('hike_detail', args=[self.hike.slug]))

    def test_can_book_a_hike(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('hike_book'), data={'places_reserved': '1', 'sched_id': '1'})
        self.assertRedirects(response, reverse('hike_mybookings'))

    def test_can_cancel_booking(self):
        self.client.login(username='testuser', password='12345')
        booking = Booking.objects.create(
            hike=self.schedule,
            username=self.user,
            places_reserved=1
        )
        matching_bookings = Booking.objects.filter(id=booking.id)
        self.assertEqual(len(matching_bookings), 1)
        response = self.client.post(reverse('hike_mybookings'), data={'cancel_booking_id': f'{booking.id}'})
        self.assertRedirects(response, reverse('hike_mybookings'))
        matching_bookings = Booking.objects.filter(id=booking.id)
        self.assertEqual(len(matching_bookings), 0)
