from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
DIFFICULTY = ((0, "Easy"), (1, "Moderate"), (2, "Difficult"))


class Hike(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    difficulty = models.IntegerField(choices=DIFFICULTY)
    distance_km = models.DecimalField(max_digits=6, decimal_places=2)
    est_duration_hrs = models.DecimalField(max_digits=4, decimal_places=2)
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='hike_likes', blank=True)

    class Meta:
        ordering = ['difficulty']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE,
                             related_name='hike_comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_comments")
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.message} by {self.username}'


class Schedule(models.Model):
    hike = models.ForeignKey(Hike, on_delete=models.CASCADE,
                             related_name='scheduled_hikes')
    starts = models.DateTimeField()
    meeting_point = models.CharField(max_length=200)

    class Meta:
        ordering = ['starts']
        constraints = [
            models.UniqueConstraint(fields=['hike', 'starts'],
                                    name='unique_hike'),
        ]

    def __str__(self):
        return f'Hike {self.hike} is scheduled for {self.starts}'


class Booking(models.Model):
    hike = models.ForeignKey(Schedule, on_delete=models.CASCADE,
                             related_name='hike_bookings')
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_bookings")
    places_reserved = models.IntegerField(validators=[MinValueValidator(1), ])
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Hike {self.hike} is booked by {self.username}'
