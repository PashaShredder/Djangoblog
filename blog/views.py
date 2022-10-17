from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from blog.models import Post
from blog.forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    context = {'items': posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def post_new(request,):
    form =PostForm
    return render(request, 'blog/post_new.html',{"form": form})
