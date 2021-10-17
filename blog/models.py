from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	created = models.DateTimeField('date published')
	def __str__(self):
		return self.name

class Blog(models.Model):
	name = models.CharField(max_length=200)
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
	description = models.TextField()
	thumbnail = models.FileField(upload_to='image/%Y/%m/%d', blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
	created = models.DateTimeField('date published')
	def __str__(self):
		return self.name

class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True, default=None)
	comment = models.TextField()
	created = models.DateTimeField('date published')