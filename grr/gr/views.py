from django.shortcuts import render
from django.views import generic

from .models import Gr

# Create your views here.

# def home(request):
#     return render(request, 'grr/home.html', {'message': 'Hello from the view!!!'})

class IndexView(generic.ListView):
    template_name = 'grr/home.html'
    context_object_name = 'gr_list'

    def get_queryset(self):
        return Gr.objects.order_by('-created_on')[:20]

class DetailView(generic.DetailView):
    model = Gr
    template_name = 'grr/detail.html'
    context_object_name = 'gr'
