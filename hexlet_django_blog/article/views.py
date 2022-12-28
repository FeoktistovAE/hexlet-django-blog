from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

# Create your views here.
class IndexView(View):
    def get(self, request, tags='', article_id = 0):
        return render(request, 'article/index.html', context={'article_id': article_id, 'tags': tags})

