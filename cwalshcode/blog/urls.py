from django.urls import path, include
from django.conf.urls import url
from . import views


app_name = "blog"
urlpatterns = [
	path("blog/", include([
		path("",  views.post, name="post"),
		path("posts/<int:pk>/", views.detail, name="detail"),
		path("drafts/", views.drafts, name="drafts"),
		path("create-post/", views.create_new, name="create_new"),
		path("posts/<int:pk>/publish/", views.publish, name="publish"),
		path("posts/<int:pk>/delete/", views.delete, name="delete"),
		path("posts/<int:pk>/edit/", views.edit_post, name='edit_post'),

	])),
]
