from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, DetailView
from blog.models import Post, Comment
from .forms import PostForm, CommentForm
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


def comments_new(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()
    return render(request, 'blog/comment.html', {
        'form': form,
    })


def comments_edit(request, **kwargs):
    comment = Comment.objects.get(pk=kwargs['pk'])
    if request.method == "POST":
        form = CommentForm(request.POST, instance = comment)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm(instance = comment)
    return render(request, 'blog/comment.html', {
        'form': form,
    })


# y나 z가 있으면 그걸 받고 아니면 기본값 0
def sum1(request, x, y=0, z=0):
    return HttpResponse(int(x)+int(y)+int(z))


def sum2(request, x):
    result = sum(int(i) for i in x.split('/'))
    return HttpResponse(result)
