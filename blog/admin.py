from django.contrib import admin
from blog.models import Blog, Category

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("name", "created")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created")