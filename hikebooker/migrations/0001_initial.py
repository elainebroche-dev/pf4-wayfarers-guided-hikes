# Generated by Django 3.2.7 on 2021-09-16 11:57

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('content', models.TextField()),
                ('difficulty', models.IntegerField(choices=[(0, 'Easy'), (1, 'Moderate'), (2, 'Difficult')])),
                ('distance_km', models.DecimalField(decimal_places=2, max_digits=6)),
                ('est_duration_hrs', models.DecimalField(decimal_places=2, max_digits=4)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('likes', models.ManyToManyField(blank=True, related_name='hike_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['difficulty'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts', models.DateTimeField()),
                ('meeting_point', models.CharField(max_length=200)),
                ('hike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_hikes', to='hikebooker.hike')),
            ],
            options={
                'ordering': ['starts'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('hike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hike_comments', to='hikebooker.hike')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('places_reserved', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('approved', models.BooleanField(default=False)),
                ('hike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hike_bookings', to='hikebooker.schedule')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='schedule',
            constraint=models.UniqueConstraint(fields=('hike', 'starts'), name='unique_hike'),
        ),
    ]