# In blog/models.py

from django.db import models

from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text_content = models.TextField()
    voice_content = models.FileField(upload_to='voice_content/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
