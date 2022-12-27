from django.shortcuts import render

# Create your views here.
def index(request):
    tags = 'Articles'
    return render(request, 'article/index.html', context={'tags': tags})
