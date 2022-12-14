from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Comments, Category
from blog.forms import PostForm


def post_list(request):
    posts = Post.objects.all().filter(published=True)
    category = Category.objects.all()
    context = {'items': posts,
               'category': category,
               }
    return render(request, 'blog/post_list.html', context)


def categories(request, category_pk):
    posts = Post.objects.filter(category=category_pk)
    category = Category.objects.all()
    counter = posts.count()
    context = {'items': posts,
               'category': category,
               'counter': counter}
    return render(request, 'blog/post_list.html', context)


def post_draft(request):
    posts = Post.objects.all().filter(published=False)
    context = {'items': posts}
    return render(request, 'blog/post_list.html', context)


def published_post(request, post_pk):
    posts = Post.objects.get(pk=post_pk)
    posts.published = True
    posts.save()
    context = {'post': posts}
    return render(request, 'blog/post_detail.html', context)


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comments = Comments.objects.filter(post=post_pk)
    counter = comments.count()
    context = {'post': post,
               'comments': comments,
               'counter': counter,
               }
    return render(request, 'blog/post_detail.html', context)


def post_new(request, ):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'blog/post_new.html', {"form": form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)


def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    # post =Post.objects.filter(pk=post_pk)#.first() ???????? ???????? ???????? ???????????? ??????????????
    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {"form": form})
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)


def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk).delete()
    return redirect('post_list')
