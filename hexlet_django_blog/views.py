from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse


class RedirectView(View):
    def get(self, request):
        return redirect(reverse('articles'))


def about(request):
    return render(request, 'about.html')
