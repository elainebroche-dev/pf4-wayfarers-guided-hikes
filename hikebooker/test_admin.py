from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Comment, Hike, Schedule, Booking
import pytz
import datetime


class TestAdmin(TestCase):
    
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
                est_duration_hrs=2
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


    def test_approve_comments(self):
        user = User.objects.create_superuser(
            username='superstar', email='test@example.com', password='password',
        )
        self.client.login(username='superstar', password='password')

        # count how many comments are currently approved
        approved = Comment.objects.filter(approved=True).count()
        self.assertFalse(self.comment.approved)
        
        data = {
            'action': 'approve_comments',
            '_selected_action': [self.comment.id, ]}
        change_url = reverse('admin:hikebooker_comment_changelist')
        response = self.client.post(change_url, data, follow=True)
        
        self.assertEqual(response.status_code, 200)

        # check number of approved comments has increased by one
        self.assertEqual(Comment.objects.filter(approved=True).count(), approved+1)


    def test_approve_bookings(self):
        user = User.objects.create_superuser(
            username='superstar', email='test@example.com', password='password',
        )
        self.client.login(username='superstar', password='password')

        # count how many bookings are currently approved
        approved = Booking.objects.filter(approved=True).count()
        self.assertFalse(self.comment.approved)
        
        data = {
            'action': 'approve_bookings',
            '_selected_action': [self.booking.id, ]}
        change_url = reverse('admin:hikebooker_booking_changelist')
        response = self.client.post(change_url, data, follow=True)
        
        self.assertEqual(response.status_code, 200)
        
        # check number of approved bookings has increased by one
        self.assertEqual(Booking.objects.filter(approved=True).count(), approved+1)

    
    def test_publish_hikes(self):
        user = User.objects.create_superuser(
            username='superstar', email='test@example.com', password='password',
        )
        self.client.login(username='superstar', password='password')

        # count how many hikes are published
        published = Hike.objects.filter(status=1).count()
        self.assertEqual(self.hike.status, 0)
        
        data = {
            'action': 'publish_hikes',
            '_selected_action': [self.hike.id, ]}
        change_url = reverse('admin:hikebooker_hike_changelist')
        response = self.client.post(change_url, data, follow=True)
        
        self.assertEqual(response.status_code, 200)
        
        # check number of published hikes has increased by one
        self.assertEqual(Hike.objects.filter(status=1).count(), published+1)
        