# In blog/urls.py

from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('post/', views.post_blog, name='post_blog'),
    path('', views.view_blogs, name='view_blogs'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('translate/<int:blog_id>/<str:target_language>/', views.translate_blog, name='translate_blog'),
    path('add_comment/<int:blog_id>/', views.add_comment, name='add_comment'),
]