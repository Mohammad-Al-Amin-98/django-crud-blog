from django.contrib import admin
from Blog.models import BlogPostModel

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'content']

admin.site.register(BlogPostModel, BlogPostAdmin)
