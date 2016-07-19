from django.shortcuts import render, redirect, HttpResponse
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

# y나 z가 있으면 그걸 받고 아니면 기본값 0
def sum1(request, x, y=0, z=0):
    return HttpResponse(int(x)+int(y)+int(z))

def sum2(request, x):
    result = sum(int(i) for i in x.split('/'))
    return HttpResponse(result)
