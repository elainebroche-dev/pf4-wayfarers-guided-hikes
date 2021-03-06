from django.test import TestCase
from .models import Hike, Comment, Schedule, Booking
import pytz
import datetime
from unittest import mock
from django.contrib.auth.models import User


class TestModels(TestCase):

    # set up test hike, comment, schedule and booking
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

    # test the __str__ method for Hike
    def test_hike_str(self):
        self.assertEqual(str(self.hike), 'test hike A')

    # test default values working as expected for Hike status and image fields
    def test_hike_defaults(self):
        self.assertEqual(self.hike.status, 0)
        self.assertEqual(self.hike.featured_image, 'placeholder')

    # test default values working as expected for Hike date fields
    def test_hike_dates_default(self):
        mocked = datetime.datetime(2018, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now',
                        mock.Mock(return_value=mocked)):
            hike = Hike.objects.create(
                title='test hike B',
                slug='test-hike-slug-B',
                content='this is the test hike B content',
                difficulty=2,
                distance_km=7,
                est_duration_hrs=4
            )
            self.assertEqual(hike.created_on, mocked)
            self.assertEqual(hike.updated_on, mocked)

    # test the __str__ method for Comment
    def test_comment_str(self):
        self.assertEqual(
            str(self.comment),
            f'Comment this is a comment for hike A by {self.user.username}')

    # test default value working as expected for Comment approved field
    def test_comment_approved_default(self):
        self.assertFalse(self.comment.approved)

    # test default values working as expected for Comment date field
    def test_comment_date_default(self):
        mocked = datetime.datetime(2018, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now',
                        mock.Mock(return_value=mocked)):
            comment = Comment.objects.create(
                 hike=self.hike,
                 username=self.user,
                 message='this is another comment for hike A'
            )
            self.assertEqual(comment.created_on, mocked)

    # test the __str__ method for Schedule
    def test_schedule_str(self):
        self.assertEqual(
            str(self.schedule), 'Hike test hike A is scheduled '
                                'for 2018-04-04 00:00:00+00:00')

    # test the __str__ method for Booking
    def test_booking_str(self):
        self.assertEqual(
            str(self.booking),
            f'{str(self.schedule)} is booked by {self.user.username}')

    # test default value working as expected for Booking approved field
    def test_booking_approved_default(self):
        self.assertFalse(self.booking.approved)
