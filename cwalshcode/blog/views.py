from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category
from .forms import PostForm

# Create your views here.


def post(request):
	posts = Post.objects.filter(draft=False)[::-1]
	categories = Category.objects.all()
	object_dict = {'posts':posts, 'categories':categories}
	return render(request, 'blog/index.html', object_dict)


def detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/detail.html', {'post':post})


def drafts(request):
	posts = Post.objects.filter(draft=True).order_by('-created_date')

	return render(request, 'blog/drafts.html',
		{'posts':posts},
		)

def create_new(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog:detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/create_new.html', {"form": form})


def publish(request, pk):
	post = Post.objects.get(pk=pk)
	post.publish()
	return redirect('blog:post')
