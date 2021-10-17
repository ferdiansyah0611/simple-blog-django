from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from blog.models import Blog, Category, Comment

# Create your views here.
def index(request):
	return render(request, 'blog/index.html', {
		"blog": Blog.objects.all(),
		"category": Category.objects.all()
	})

def show(request, blog):
	return render(request, 'blog/show.html', {
		"blog": Blog.objects.get(id=blog),
		"category": Category.objects.all(),
		"comment": Comment.objects.order_by('created').filter(blog_id=blog)
	})
def addcomment(request, blog):
	post = request.POST
	print(post.get("comment"))
	datablog = Blog.objects.get(id=blog)
	Comment.objects.create(user=request.user, blog=datablog, comment=post.get("comment"), created=timezone.now())
	return redirect("/blog/{}".format(blog))