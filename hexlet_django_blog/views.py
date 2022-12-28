from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse


class RedirectView(View):
    def get(self, request):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))

def about(request):
    return render(request, 'about.html')