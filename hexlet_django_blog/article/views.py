from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from hexlet_django_blog.article.models import Article
from .forms import ArticleForm
from django.contrib import messages


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'article/index.html',
            context={'articles': articles}
        )


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(
            request,
            'article/show.html',
            context={'article': article})


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'article/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Article succesfully created')
            return redirect('articles')
        messages.add_message(request, messages.ERROR, "Something went wrong")
        return render(request, 'article/create.html', {'form': form})
    

class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'article/update.html', {'form': form, 'article_id': article_id})
    
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Article succesfully updated')
            return redirect('articles')
        messages.add_message(request, messages.ERROR, "Something went wrong")
        return render(request, 'article/update.html', {'form': form, 'article_id': article_id})
    

class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.add_message(request, messages.SUCCESS, "Article succesfully deleted")
        return redirect('articles')
