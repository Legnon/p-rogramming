from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

# Create your views here.
def introduce(request):
    return render(request, 'blog/introduce.html', {})

post_list = ListView.as_view(model=Post)
post_detail = DetailView.as_view(model=Post)
