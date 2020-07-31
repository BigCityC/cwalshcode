from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
	path("posts/", views.post, name="post"),
	path("posts/title/", views.detail, name="detail"),
	path("posts/test/", views.btest, name="btest"),
]
