from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse


class IndexView(View):
    def get(self, request):
        user = request.user
        return render(request, 'index.html', {'who': user})


def about(request):
    return render(request, 'about.html')
