from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from blog.models import ArticleModel
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


class Home(View):

    def get(self, request):
        articles = ArticleModel.objects.all()
        return render(request, "home.html", {"articles":articles})


    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/articles/')
        else:
            messages.warning(request, 'invalid credentials')
            return redirect('/')


class Article(View):
    def get(self, request):
        articles = ArticleModel.objects.all()
        return render(request, "article.html", {"articles":articles})


class AddArticle(View):

    def get(self, request):
        articles = ArticleModel.objects.all()
        return render(request, "add_article.html")

    def post(self, request):
        title = request.POST["title"]
        category = request.POST["category"]
        #author = request.POST["author"]
        author = request.user
        content = request.POST["content"]
        
        ArticleModel.objects.create(title = title, category=category.upper(), author=author, content=content, created_at=datetime.now())
        return redirect("/articles/") 