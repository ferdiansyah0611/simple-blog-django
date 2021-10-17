from django.contrib import admin
from blog.models import Blog, Category, Comment

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("name", "created")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "created")