from django.urls import path, include
from . import views

app_name = "blog"
urlpatterns = [
	path("blog/", include([
		path("",  views.post, name="post"),
		path("posts/<int:pk>/", views.detail, name="detail"),
		path("drafts/", views.drafts, name="drafts"),
		path("create-post/", views.create_new, name="create_new")
	])),
]
