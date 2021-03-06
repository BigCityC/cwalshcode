from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=200)
	slug=models.SlugField()
	parent=models.ForeignKey(
		'self', blank=True, null=True, related_name="children", on_delete=models.CASCADE)


	class Meta:
		# there cannot be two categories under a parent with the same slug
		unique_together=('slug', 'parent',)
		verbose_name_plural="categories"

	def __str__(self):
		full_path=[self.name]
		k=self.parent
		while k is not None:
			full_path.append(k.name)
			k=k.parent
		return ' --> '.join(full_path[::-1])


class Post(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=100)
	body = models.TextField()
	category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
	created_date = models.DateTimeField(default=timezone.now)
	draft = models.BooleanField(default=True)
	publish_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.publish_date = timezone.now()
		self.draft = False
		self.save()

	def __str__(self):
		return self.title

	def get_category_list(self):
		k = self.category
		breadcrumb = ["dummy"]
		while k is not None:
			breadcrumb.append(k.slug)
			k = k.parent
		for i in range(len(breadcrumb) - 1):
			breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
		return breadcrumb[-1:0:-1]
