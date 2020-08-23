from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
	path("posts/", views.post, name="post"),
	path("posts/<int:pk>/", views.detail, name="detail"),
	path("posts/drafts/", views.drafts, name="drafts"),
]
