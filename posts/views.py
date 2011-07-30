# Create your views here.

from django.shortcuts import render_to_response

from posts.models import Post

def show_post(request, year, month, day, slug):
    post = Post.objects.filter(is_published=True).get(slug=slug)

    return render_to_response('show_post.html', {'post': post})

def index(request):
    posts = Post.objects.filter(is_published=True).order_by('-pub_date').all()
    return render_to_response('index.html', {'posts': posts})
