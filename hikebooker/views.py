from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Hike, Booking, Schedule
from .forms import CommentForm
import datetime
import pytz


class HikeList(generic.ListView):
    """
    Retrieve the hike summaries and set pagination
    """

    model = Hike
    queryset = Hike.objects.filter(status=1).order_by('difficulty',
                                                      '-created_on')
    template_name = 'index.html'
    paginate_by = 6


class HikeDetail(View):
    """
    Display Hike Details for selected hike

    get method : retrieve hike details including comments and likes
                 and render hike detail page

    post method : validate comment input, store and re-load detail page
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Hike.objects.filter(status=1)
        hike = get_object_or_404(queryset, slug=slug)
        comments = hike.comments.filter(approved=True).order_by('-created_on')
        scheduled_hikes = Schedule.objects.filter(hike=hike).filter(
                            starts__gt=datetime.datetime.now(
                                        pytz.utc)).order_by('starts')
        liked = False
        if hike.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "hike_detail.html",
            {
                "hike": hike,
                "comments": comments,
                "scheduled_hikes": scheduled_hikes,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = Hike.objects.filter(status=1)
            hike = get_object_or_404(queryset, slug=slug)
            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():
                comment_form.instance.username = request.user
                comment = comment_form.save(commit=False)
                comment.hike = hike
                comment.save()
                messages.success(request, 'Thank you for your comment !')

        # User HttpResponseRedirect here instead of render to ensure comment
        # is not re-submitted on page re-load
        return HttpResponseRedirect(reverse('hike_detail', args=[slug]))


class HikeLike(View):
    """
    Allow user to like/unlike the current hike

    post method : toggle 'like' setting for hike for this user
    """

    def post(self, request, slug):
        hike = get_object_or_404(Hike, slug=slug)

        if hike.likes.filter(id=request.user.id).exists():
            hike.likes.remove(request.user)
        else:
            hike.likes.add(request.user)

        return HttpResponseRedirect(reverse('hike_detail', args=[slug]))


class HikeMyBookings(View):
    """
    Display booking information for current user

    get method : retrieve past and upcoming bookings for user
                 and render my bookings page

    post method : cancel selected booking and reload page
    """

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(username=self.request.user).filter(
                    hike__starts__gt=datetime.datetime.now(
                                        pytz.utc)).order_by('hike__starts')
        past_bookings = Booking.objects.filter(
                    username=self.request.user).filter(
                    hike__starts__lte=datetime.datetime.now(
                                        pytz.utc)).order_by('hike__starts')

        return render(
            request,
            "hike_mybookings.html",
            {
                "bookings": bookings,
                "past_bookings": past_bookings,
            }
        )

    def post(self, request, *args, **kwargs):
        id = request.POST.get('cancel_booking_id')
        booking = get_object_or_404(Booking, id=id)
        booking.delete()

        # Used HttpResponseRedirect here instead of render to ensure
        # delete request is not re-submitted on bookings page re-load
        messages.success(request, 'Your booking has been cancelled.')
        return HttpResponseRedirect(reverse('hike_mybookings'))


class HikeBook(View):
    """
    Book hike currently displayed on Hike Detail page

    post method : check input, create new booking for current user
                  for selected schedulded hike then redirect to
                  bookings page
    """

    def post(self, request):

        user = request.user
        places_reserved = request.POST.get('places_reserved')
        # validate number of places reserved
        if places_reserved in ['1', '2', '3', '4', '5']:
            sched_id = request.POST.get('sched_id')
            sched_hike = get_object_or_404(Schedule, id=sched_id)
            Booking.objects.create(hike=sched_hike, username=user,
                                   places_reserved=places_reserved)
            messages.success(request, 'Thank you for your booking request !')
            # Used HttpResponseRedirect here instead of render to ensure
            # booking is not re-submitted on bookings page re-load

        return HttpResponseRedirect(reverse('hike_mybookings'))
