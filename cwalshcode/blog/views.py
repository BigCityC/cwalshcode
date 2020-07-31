from django.shortcuts import render
from .models import Post, Category
# Create your views here.


def post(request):
	posts = Post.objects.all()
	categories = Category.objects.all()
	object_dict = {'posts':posts, 'categories':categories}
	return render(request, 'blog/index.html', object_dict)


def detail(request):
	return render(request, 'blog/detail.html', {})


def btest(request):
	posts = Post.objects.all()
	categories = Category.objects.all()
	return render(request, 'blog/b-test.html',
		{'categories':categories},
		{'posts':posts},

		)
