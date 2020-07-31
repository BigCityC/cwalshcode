from django.shortcuts import render

# Create your views here.


def blog(request):
    return render(request, 'blog/index.html', {})


def detail(request):
    return render(request, 'blog/detail.html', {})
