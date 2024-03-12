# In blog/views.py

from django.shortcuts import render, redirect
from .forms import BlogPostForm, CommentForm
from .models import BlogPost, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from googletrans import Translator


def add_comment(request, blog_id):
    blog = BlogPost.objects.get(pk=blog_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user']
            content = form.cleaned_data['content']
            comment = Comment.objects.create(blog_post=blog, user=user_name, content=content)
            return redirect('blog:view_blogs')
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})


def translate_blog(request, blog_id, target_language):
    # Fetch blog post to translate
    blog = get_object_or_404(BlogPost, pk=blog_id)
    
    # Initialize translator
    translator = Translator()

    # Translate text content
    translated_text = translator.translate(blog.text_content, dest=target_language)
    
    # Render template with translated text
    return render(request, 'blog/translated_blog.html', {'blog': blog, 'translated_text': translated_text.text, 'target_language': target_language})



def view_blogs(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog/view_blogs.html', {'blogs': blogs})

@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    if request.user == blog.created_by:  # Check if the current user created the blog
        # Handle editing logic here
        return render(request, 'blog/edit_blog.html', {'blog': blog})
    else:
        # Redirect or display an error message
        return redirect('blog:view_blogs')

@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    if request.user == blog.created_by:  # Check if the current user created the blog
        # Handle deleting logic here
        blog.delete()
        return redirect('blog:view_blogs')
    else:
        # Redirect or display an error message
        return redirect('blog:view_blogs')

@login_required
def post_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:view_blogs')
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_blog.html', {'form': form})

