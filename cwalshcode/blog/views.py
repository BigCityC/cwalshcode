from django.shortcuts import render
from .models import Post, Category
# Create your views here.


def post(request):
	posts = Post.objects.all()[::-1]
	categories = Category.objects.all()
	object_dict = {'posts':posts, 'categories':categories}
	return render(request, 'blog/index.html', object_dict)


def detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/detail.html', {'post':post})


def drafts(request):
	posts = Post.objects.filter(draft=True)

	return render(request, 'blog/drafts.html',
		{'posts':posts},
		)

def create_new(request):
	pass
