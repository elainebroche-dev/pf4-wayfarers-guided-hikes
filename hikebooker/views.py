from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Hike
from .forms import CommentForm


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
        liked = False
        if hike.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "hike_detail.html",
            {
                "hike": hike,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Hike.objects.filter(status=1)
        hike = get_object_or_404(queryset, slug=slug)
        comments = hike.comments.filter(approved=True).order_by('created_on')
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
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )
