from django.shortcuts import render
from django.views import generic
from .models import Hike


class HikeList(generic.ListView):
    model = Hike
    queryset = Hike.objects.filter(status=1).order_by('difficulty',
                                                      '-created_on')
    template_name = 'index.html'
    paginate_by = 6
