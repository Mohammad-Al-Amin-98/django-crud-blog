from django.shortcuts import render, redirect
from Blog.forms import BlogPostForm
from Blog.models import BlogPostModel

# Create your views here.
def home(request):
    return render(request, "base.html")

def post_a_blog(request):
    if request.method == 'POST':
        post = BlogPostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect("show_blog")
    else:
        post = BlogPostForm()
        return render(request, './Blog/post_a_blog.html', {'form':post})

def show_blog(request):
    posts = BlogPostModel.objects.all()
    return render(request, 'Blog/show_blog.html', {'data':posts})

def edit_blog(request, id):
    blog = BlogPostModel.objects.get(pk=id)
    if request.method == 'POST':
        post = BlogPostForm(request.POST, instance=blog)
        if post.is_valid():
            post.save()
            return redirect("show_blog")
    else:
        post = BlogPostForm(instance=blog)
        return render(request, 'Blog/post_a_blog.html', {'form':post})

def delete_blog(request, id):
    BlogPostModel.objects.get(pk=id).delete()
    return redirect("show_blog")
