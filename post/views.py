from django.shortcuts import render, get_object_or_404
from .models import Article  # Import the Article model

def all_post(request):
    articles = Article.objects.all()  # Change from Post to Article
    return render(request, 'post/all_post.html', {'articles': articles})

def post_details(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'post/post_details.html', {'article': article})
