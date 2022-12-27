from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', context={
            'who': 'Django',
        })


def about(request):
    return render(request, 'about.html')