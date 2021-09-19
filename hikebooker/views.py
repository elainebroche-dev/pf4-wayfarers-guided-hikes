from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Hike


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
        comments = hike.comments.filter(approved=True).order_by('created_on')
        liked = False
        if hike.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "hike_detail.html",
            {
                "hike": hike,
                "comments": comments,
                "liked": liked
            }
        )
