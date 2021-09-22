from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Hike, Booking, Schedule
from .forms import CommentForm
from datetime import date


class HikeList(generic.ListView):
    model = Hike
    queryset = Hike.objects.filter(status=1).order_by('difficulty',
                                                      '-created_on')
    template_name = 'index.html'
    paginate_by = 6


class HikeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Hike.objects.filter(status=1)
        hike = get_object_or_404(queryset, slug=slug)
        comments = hike.comments.filter(approved=True).order_by('-created_on')
        scheduled_hikes = Schedule.objects.filter(hike=hike).filter(
                            starts__gt=date.today()).order_by('starts')
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
        queryset = Hike.objects.filter(status=1)
        hike = get_object_or_404(queryset, slug=slug)
        comments = hike.comments.filter(approved=True).order_by('-created_on')
        scheduled_hikes = Schedule.objects.filter(hike=hike).filter(
                                starts__gt=date.today()).order_by('starts')
        liked = False
        if hike.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.username = request.user
            comment = comment_form.save(commit=False)
            comment.hike = hike
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "hike_detail.html",
            {
                "hike": hike,
                "comments": comments,
                "scheduled_hikes": scheduled_hikes,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class HikeLike(View):

    def post(self, request, slug):
        hike = get_object_or_404(Hike, slug=slug)

        if hike.likes.filter(id=request.user.id).exists():
            hike.likes.remove(request.user)
        else:
            hike.likes.add(request.user)

        return HttpResponseRedirect(reverse('hike_detail', args=[slug]))


class HikeMyBookings(View):

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(username=self.request.user).filter(
                    hike__starts__gt=date.today()).order_by('hike__starts')

        return render(
            request,
            "hike_mybookings.html",
            {
                "bookings": bookings,
            }
        )

    def post(self, request, *args, **kwargs):
        id = request.POST.get('cancel_booking_id')
        booking = get_object_or_404(Booking, id=id)
        booking.delete()

        bookings = Booking.objects.filter(username=self.request.user).filter(
                    hike__starts__gt=date.today()).order_by('hike__starts')

        return render(
            request,
            "hike_mybookings.html",
            {
                "bookings": bookings,
            }
        )





class HikeBook(View):

    def post(self, request):

        user = request.user
        places_reserved = request.POST.get('places_reserved')
        sched_id = request.POST.get('sched_id')
        sched_hike = get_object_or_404(Schedule, id=sched_id)
        Booking.objects.create(hike=sched_hike, username=user,
                               places_reserved=places_reserved)

        bookings = Booking.objects.filter(username=self.request.user).filter(
                    hike__starts__gt=date.today()).order_by('hike__starts')
        return render(
            request,
            "hike_mybookings.html",
            {
                "bookings": bookings,
            }
        )
