from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from blog.models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.
def introduce(request):
    return render(request, 'blog/introduce.html', {})

post_list = ListView.as_view(model=Post)
post_detail = DetailView.as_view(model=Post)

def post_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('blog:post_list')
    else:
        form = PostForm()
        content = {'form':form}
        return render(request, 'blog/post_form.html', content)
