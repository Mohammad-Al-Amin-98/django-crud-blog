from django.urls import path
from Blog.views import home, post_a_blog, show_blog, edit_blog, delete_blog

urlpatterns = [
        path('', home, name="homepage"),
        path('post_a_blog/', post_a_blog, name="post_a_blog"),
        path('show_blog/', show_blog, name="show_blog"),
        path('edit_blog/<int:id>', edit_blog, name="edit_blog"),
        path('delete_blog/<int:id>', delete_blog, name="delete_blog"),
]
