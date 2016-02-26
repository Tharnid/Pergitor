from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'grr/home.html', {'message': 'Hello from the view!!!'})
