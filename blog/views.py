from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog, Category

# Create your views here.
def index(request):
	return render(request, 'blog/index.html', {
		"blog": Blog.objects.all(),
		"category": Category.objects.all()
	})

def show(request, blog):
	return render(request, 'blog/show.html', {
		"blog": Blog.objects.get(id=blog),
		"category": Category.objects.all()
	})