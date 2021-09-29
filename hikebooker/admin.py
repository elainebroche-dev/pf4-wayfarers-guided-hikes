from django.contrib import admin
from .models import Hike, Comment, Schedule, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Hike)
class HikeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'difficulty', 'distance_km', 'est_duration_hrs',
                    'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'difficulty', 'created_on')
    summernote_fields = ('content')
    actions = ['publish_hikes']

    def publish_hikes(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('message', 'hike', 'username', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('username__username', 'message')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('hike', 'starts', 'meeting_point')
    list_filter = ('hike', 'starts',)
    search_fields = ('hike__title', 'meeting_point')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('hike', 'username', 'places_reserved', 'approved')
    list_filter = ('hike', 'username__username', 'approved')
    search_fields = ('hike__hike__title', 'username__username',)
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
