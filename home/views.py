from django.shortcuts import render, redirect, get_object_or_404
from home.models import Post
from home.forms import PostForm
from django.http import HttpResponse
# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, "home/home.html", {'posts': posts})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('home:main')
        else :
            return HttpResponse("404")
    else :
        form = PostForm()
        return render(request, "home/post_create.html", {'form': form})

def post_detail(request, slug_url):
    post = get_object_or_404(Post, slug=slug_url)
    return render(request, "home/post_detail.html", {'post': post})

def post_update(request, slug_url):
    post = get_object_or_404(Post, slug=slug_url)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(post)
        else :
            return HttpResponse("404")
    else :
        form = PostForm(instance=post)
        return render(request, "home/post_create.html", {'form': form})