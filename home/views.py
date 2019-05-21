from django.shortcuts import render, redirect, get_object_or_404
from home.models import Post
from home.forms import PostForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    posts = Post.objects.all()
    title = "전체 포스팅"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    post_count = posts.count()
    is_home = True
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:   
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, "home/home.html", {
        'post_count': post_count,
        "title": title,
        'post_list': post_list,
        'is_home': is_home,
        })

def projects(request):
    posts = Post.objects.all().filter(category="Projects")
    title = "Projects"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    post_count = posts.count()
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, "home/home.html", {
        'post_count': post_count,
        "title": title,
        'post_list': post_list,
    })

def study(request):
    posts = Post.objects.all().filter(category="Study")
    title = "Study"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    post_count = posts.count()
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.page(paginator.num_pages)
    return render(request, "home/home.html", {
        'post_count': post_count,
        'title': title,
        'post_list': post_list,
    })

def study_c(request):
    posts = Post.objects.all().filter(category="Study").filter(sub_category="C언어")
    title = "Study"
    sub_category = "C 언어"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    post_count = posts.count()
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.page(paginator.num_pages)
    return render(request, "home/home.html", {
        'post_count': post_count,
        'title': title,
        'post_list': post_list,
        'sub_category': sub_category,
    })

def study_django(request):
    posts = Post.objects.all().filter(category="Study").filter(sub_category="Django")
    title = "Study"
    sub_category = "Django"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    post_count = posts.count()
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.page(paginator.num_pages)
    return render(request, "home/home.html", {
        'post_count': post_count,
        'title': title,
        'post_list': post_list,
        'sub_category': sub_category,
    })

def study_front(request):
    posts = Post.objects.all().filter(category="Study").filter(sub_category="Front-End")
    title = "Study"
    sub_category = "Front-End"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    post_count = posts.count()
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.page(paginator.num_pages)
    return render(request, "home/home.html", {
        'post_count': post_count,
        'title': title,
        'post_list': post_list,
        'sub_category': sub_category,
    })

def articles(request):
    posts = Post.objects.all().filter(category="Article")
    title = "Articles"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    post_count = posts.count()
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, "home/home.html", {
        'post_count': post_count,
        'title': title,
        'post_list': post_list,
    })

def articles_it(request):
    posts = Post.objects.all().filter(category="Article").filter(sub_category="IT")
    title = "Articles"
    sub_category = "IT"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    post_count = posts.count()
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.page(paginator.num_pages)
    return render(request, "home/home.html", {
        'post_count': post_count,
        'title': title,
        'post_list': post_list,
        'sub_category': sub_category,
    })

def articles_affair(request):
    posts = Post.objects.all().filter(category="Article").filter(sub_category="시사")
    title = "Articles"
    sub_category = "시사"
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 3)
    post_count = posts.count()
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.page(paginator.num_pages)
    return render(request, "home/home.html", {
        'post_count': post_count,
        'title': title,
        'post_list': post_list,
        'sub_category': sub_category,
    })

@login_required
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

@login_required
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

@login_required
def post_delete(request, slug_url):
    post = get_object_or_404(Post, slug=slug_url)
    post.delete()
    return redirect("home:main")

