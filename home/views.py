from django.shortcuts import render, redirect
from home.models import Post
from home.forms import PostForm
# Create your views here.

def home(request):
    qs = Post.objects.all().first()
    return render(request, "home/home.html", {'tmp': qs})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid() :
            form.save()
        return redirect('home:main')
    else :
        form = PostForm()
        return render(request, "home/post_create.html", {'form': form})