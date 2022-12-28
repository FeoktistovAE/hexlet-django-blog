from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):
    def get(self, request):
        tags = 'Articles page'
        return render(request, 'article/index.html', context={'tags': tags})
