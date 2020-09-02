from django.shortcuts import render
from blog.models import Category
# Create your views here.


def index(request):
	# category = Category.objects.get(pk=1)
	return render(request, 'home/index.html', {})
