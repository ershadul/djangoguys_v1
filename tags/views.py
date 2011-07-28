# Create your views here.

from django.shortcuts import render_to_response

from tags.models import Tag

def show_tag(request, slug):
    tag = Tag.objects.get(slug=slug)

    return render_to_response('show_tag.html', {'tag': tag})

def index(request):
    tags = Tag.objects.order_by('name').all()
    return render_to_response('index.html', {'tags': tags})
